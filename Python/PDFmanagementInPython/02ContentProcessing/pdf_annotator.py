#Import Libraries
from io import BytesIO
import os, argparse, re, fitz , filetype

def build_range(rangeval:str):
    """
    Build the range of pages based on the parameter inputted rangeval
    """
    result=set()
    for part in rangeval.split(','):
        x=part.split('-')
        result.update(range(int(x[0]),int(x[-1])+1))
    return list(sorted(result))

def search_for_str(document_lines,search_value):
    """
    Search for a particular string within the document lines
    """
    for line in document_lines:
        #Find all the matches of the search_value within the referenced line
        results = re.findall( search_value , line, re.IGNORECASE)
        #If multiple matches were found within the referenced line
        for result in results:
            yield result


def add_annotation (input_file:str
                   ,output_file:str
                   ,search_value:str
                   ,pages:list=None
                    #Default the action to Highlight
                   ,action:str = 'Highlight'):
    """
    Process the pages of the PDF File
    """

    # Open the chosen PDF
    pdfIn = fitz.open(input_file)

    # Create a memory buffer for storing the resulting file
    out_buffer = BytesIO()

    # Count of matches
    count_matches = 0

    # Iterate through pages
    for pg in range(pdfIn.pageCount):
        pageID = pg + 1

        # If specific pages to be considered
        if pages:
            if pageID not in pages:
               continue

        # Select the page
        page = pdfIn[pg]

        # Get the Matching Data
        # Split the page line by line
        page_lines = page.getText("text").split('\n')
        matching_values = search_for_str(document_lines=page_lines, search_value=search_value)

        if matching_values:
           if action in ('Highlight','Squiggle','Underline','Strikeout'):
               matches_found = annotate_matched_data(page, matching_values, action)
           else:
               matches_found = annotate_matched_data(page, matching_values, 'Highlight')

           print(f"Total Match(es) Found [{matches_found}] of Search String [{search_value}] In Page [{pageID}]")
           count_matches += matches_found

    print(f"Total Match(es) Found [{count_matches}] of Search String [{search_value}] In Input File: [{input_file}]")

    # Save the input file after processing to the memory buffer
    pdfIn.save(out_buffer)
    pdfIn.close()

    # Save the output buffer to the chosen output file
    with open(output_file, mode='wb') as f:
        f.write(out_buffer.getbuffer())
    f.close()


def annotate_matched_data (page, matched_values,type):
    """
    Annotate matched values
    """
    matches_found = 0
    # Iterate through the matched values
    for val in matched_values:
        matches_found += 1
        # Get the matched value area
        matched_val_area = page.searchFor(val)

        highlight = None
        if type == 'Highlight':
            highlight = page.addHighlightAnnot(matched_val_area)
        elif type == 'Squiggle':
            highlight = page.addSquigglyAnnot(matched_val_area)
        elif type == 'Underline':
            highlight = page.addUnderlineAnnot(matched_val_area)
        elif type == 'Strikeout':
            highlight = page.addStrikeoutAnnot(matched_val_area)
        else:
            highlight = page.addHighlightAnnot(matched_val_area)

        highlight.update()
    return matches_found

def remove_annotation(input_file:str
                     ,output_file:str
                     ,pages:list=None):

    # Open the PDF document
    pdfIn = fitz.open(input_file)

    #Create a memory buffer and save the generated PDF to this buffer
    out_buffer = BytesIO()

    #Initialize an annotations counter
    annot_found = 0

    # Loop through pages
    for pg in range(pdfIn.pageCount):
        pageID = pg + 1

        # If specific pages are to be considered
        if pages:
           if pageID not in pages:
              continue

        # Select a sepicific page
        page = pdfIn[pg]

        # Delete all annotations found
        annot = page.firstAnnot
        while annot:
            annot_found += 1
            page.deleteAnnot(annot)
            annot = annot.next

    # Display a message indicating that annotations were found
    if annot_found >= 0:
       print(f"Annotation(s) Found In The Input File: {input_file}")

    #Save to memory buffer
    pdfIn.save(out_buffer)
    pdfIn.close()

    #Save the memory buffer to the output file
    with open(output_file, mode='wb') as f:
        f.write(out_buffer.getbuffer())
    f.close()

def process_file(**kwargs):
    """
    To process a PDF file
    """
    input_file  = kwargs.get('input_file')
    output_file = kwargs.get('output_file')
    if output_file is None:
        output_file = input_file
    search_value  = kwargs.get('search_value')
    pages         = kwargs.get('pages')

    # Highlight,  Underline, Strikeout, Squiggle
    action        = kwargs.get('action')

    if action == "Remove":
        #Remove the applied annotations
        remove_annotation(input_file=input_file, output_file = output_file, pages=pages)
    else:
        #Apply Annotations
        add_annotation(input_file = input_file, output_file = output_file, search_value = search_value, pages = pages, action = action)

def is_valid_file_path(path):
    """
    Validate the path inputted and make sure it is a file path of type PDF
    """
    if not path:
        raise ValueError(f"Invalid Path")
    if os.path.isfile(path) and 'pdf' in filetype.guess(path).mime:
       return path
    else:
       raise ValueError(f"Invalid Path {path}")

def parse_args():
    """
    Get user command line parameters
    """
    parser = argparse.ArgumentParser(description="Available Options")

    parser.add_argument('-i'
                       ,'--input_file'
                       ,dest='input_file'
                       ,type=is_valid_file_path
                       ,required=True
                       ,help = "Enter the path of the file to process")

    parser.add_argument('-o'
                       , '--output_file'
                       , dest='output_file'
                       , type=str
                       , help="Enter a valid output file")

    parser.add_argument('-a'
                      , '--action'
                      , dest='action'
                      , choices=['Highlight', 'Squiggle', 'Underline', 'Strikeout', 'Remove']
                      , type=str
                      , default='Highlight'
                      , help="Choose whether to Highlight or to Squiggle or to Underline or to Strikeout or to Remove")

    parser.add_argument('-p'
                      , '--pages'
                      , dest='pages'
                      , type=str
                      , help="Enter the pages to consider e.g.: 0,1 or 2-3")

    action = parser.parse_known_args()[0].action
    if action != 'Remove':
        parser.add_argument('-s'
                            , '--search_value'
                            , dest='search_value'
                            , type=str
                            , required=True
                            , help="Enter a valid search value")

    args = vars(parser.parse_args())

    #To Display The Command Line Arguments
    print("## Command Arguments #################################################")
    print("\n".join("{}:{}".format(i,j) for i,j in args.items()))
    print("######################################################################")

    return args

if __name__ == '__main__':
    # Parsing command line arguments entered by user
    args = parse_args()

    # Generate a page range
    pages_list = build_range(args['pages']) if args['pages'] else None

    # Process a chosen file
    process_file (
              input_file=args['input_file']
            , output_file=args['output_file']
            , search_value=args['search_value'] if 'search_value' in (args.keys()) else None
            , pages=pages_list
            , action=args['action']
    )
