import fitz,os,filetype,argparse

BLUE_COLOR = (0,0,1)

def build_range(rangeval:str):
    """
    Build the range of pages based on the parameter inputted rangeval
    """
    result=set()
    for part in rangeval.split(','):
        x=part.split('-')
        result.update(range(int(x[0]),int(x[-1])+1))
    return list(sorted(result))

def comment_pdf(input_file:str
              , search_text:str
              , comment_title:str
              , comment_info:str
              , output_file:str
              , pages:list=None
              ):
    """
    Search for a particular string value in a PDF file and add comments to it.
    """
    pdfIn = fitz.open(input_file)
    found_matches = 0
    # Iterate throughout the document pages
    for pg,page in enumerate(pdfIn):
        pageID = pg+1
        # If required for specific pages
        if pages:
           if pageID not in pages:
              continue

        # Use the search for function to find the text
        matched_values = page.searchFor(search_text,hit_max=20)
        found_matches += len(matched_values) if matched_values else 0

        #Loop through the matches values
        #item will contain the coordinates of the found text
        for item in matched_values:
            # Enclose the found text with a bounding box
            annot = page.addRectAnnot(item)
            annot.setBorder({"dashes":[2],"width":0.2})
            annot.setColors({"stroke":BLUE_COLOR})

            # Add comment to the found match
            info = annot.info
            info["title"]   = comment_title
            info["content"] = comment_info
            #info["subject"] = "Educative subject"
            annot.setInfo(info)

            annot.update()

    #Save to output file
    pdfIn.save(output_file,garbage=3,deflate=True)
    pdfIn.close()

    #Process Summary
    summary = {
         "Input File": input_file
       , "Matching Instances": found_matches
       , "Output File": output_file
       , "Comment Title": comment_title
       , "Comment Info":  comment_info
    }

    # Print process Summary
    print("## Summary ########################################################")
    print("\n".join("{}:{}".format(i, j) for i, j in summary.items()))
    print("###################################################################")

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
                       , '--search_str'
                       , dest='search_str'
                       , type=str
                       , required=True
                       , help="Enter a valid search string")

    parser.add_argument('-t'
                       , '--comment_title'
                       , dest='comment_title'
                       , type=str
                       , required=True
                       , help="Enter a title for the comment")

    parser.add_argument('-c'
                       , '--comment_info'
                       , dest='comment_info'
                       , type=str
                       , required=True
                       , help="Enter the comment info")

    args = vars(parser.parse_args())

    #To Display The Command Line Arguments
    print("## Command Arguments #################################################")
    print("\n".join("{}:{}".format(i,j) for i,j in args.items()))
    print("######################################################################")

    return args


if __name__ == "__main__":
    # Parsing command line arguments entered by user
    args = parse_args()

    pages_list = build_range(args['pages']) if args['pages'] else None
    output_file = args['output_file'] if args['output_file'] \
        else os.path.join(os.path.dirname(args['input_file']),
                          os.path.splitext(os.path.basename(args['input_file']))[0] + "_commented.pdf")

    comment_pdf(input_file     = args['input_file']
               , search_text   = args['search_str']
               , comment_title = args['comment_title']
               , comment_info  = args['comment_info']
               , output_file   = output_file
               , pages         = pages_list
                )
