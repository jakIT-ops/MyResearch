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


def redact_matched_values (page, matched_values):
    """
    Redact the matching values
    """
    count_matches = 0
    # Iterates through the matched values
    for val in matched_values:
        count_matches += 1
        # Search for the matched value area
        matched_val_area = page.searchFor(val)
        # Add a black rectangle on top of the area of the matched value
        [page.addRedactAnnot(area, text=" ", fill=(0, 0, 0)) for area in matched_val_area]
    # Set the redaction
    page.apply_redactions()
    return count_matches


def redact_file (input_file:str
                  ,output_file:str
                  ,search_value:str
                  ,pages:list=None
                  ):
    """
    Search and Redact specific text in a PDF file
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
           matches_found = redact_matched_values(page, matching_values)
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

    parser.add_argument('-p'
                      , '--pages'
                      , dest='pages'
                      , type=str
                      , help="Enter the pages to consider e.g.: 0,1 or 2-3")

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

    # Apply to the same input file if no output file is specified
    output_file = args['output_file'] if args['output_file']  else args['input_file']

    redact_file (input_file=args['input_file']
               , output_file=args['output_file'] if 'output_file' in (args.keys()) else args['input_file']
               , search_value=args['search_value'] if 'search_value' in (args.keys()) else None
               , pages=pages_list
               )
