#Import Libraries
import fitz
import os,argparse,filetype,json

#ENCODING = 'utf8'
ENCODING = 'ascii'

def build_range(rangeval:str):
    """
    Build the range of pages based on the parameter inputted rangeval
    """
    result=set()
    for part in rangeval.split(','):
        x=part.split('-')
        result.update(range(int(x[0]),int(x[-1])+1))
    return list(sorted(result))


def sortPageBlocks(page_blocks):
    """
    Sort the page blocks in ascending vertical order then in ascending horizontal order
    """
    blocks = []
    for b in page_blocks:
        # x coordinate in pixels
        x0 = str(int(b["bbox"][0] + 0.99999)).rjust(4,"0")
        # y coordinate in pixels
        y0 = str(int(b["bbox"][1] + 0.99999)).rjust(4, "0")
        sortage_key = y0 + x0
        blocks.append([sortage_key,b])
    blocks.sort(key=lambda x: x[0])
    #Return a list of sorted blocks
    return [b[1] for b in blocks]

def sortBlockLines(block_lines):
    """
    Sort the block lines in ascending vertical order.
    """
    lines = []
    for l in block_lines:
        y0 = str(int(l["bbox"][1] + 0.99999)).rjust(4,"0")
        lines.append([y0,l])
    lines.sort(key=lambda x: x[0])
    #Return a list of sorted lines in block
    return [l[1] for l in lines]

def sortLineSpans(line_spans):
    """
    Sort the spans of a line in an ascending horizontal direction.
    """
    spans = []
    for s in line_spans:
        x0 = str(int(s["bbox"][1] + 0.99999)).rjust(4,"0")
        spans.append([x0,s])
    spans.sort(key=lambda x: x[0])
    return [s[1] for s in spans]


def extract_text_content(input_file:str
                        ,output_path:str
                        ,pages:str):
    """
    Parse text from a pdf document and save output to a text file
    """
    #Open the document
    pdfIn = fitz.open(input_file)

    output_filename = os.path.join(output_path
     , os.path.splitext(os.path.basename(input_file))[0]  + ".txt")
    output_file = open(output_filename,"w",encoding=ENCODING)

    #Iterate through pages
    try:
       for pg in range(pdfIn.pageCount):
           if pages:
              if (pg + 1) not in pages:
                 continue

           page_text = ""
           #Load the page
           page = pdfIn.loadPage(pg)

           #Extract text block dictionaries of the current page
           page_dict = page.getText("dict", flags = 0)

           #Loop through the arranged page blocks
           for b in sortPageBlocks(page_dict["blocks"]):
               #loop through the sorted block lines
               for l in sortBlockLines(b["lines"]):
                   #loop through the sorted line spans
                   for s in sortLineSpans(l["spans"]):
                       if page_text.endswith(" ") or s["text"].startswith(" "):
                          page_text += s["text"]
                       else:
                          page_text += " " + s["text"]
                   #Separate line by line
                   page_text += "\n"

           page_text = page_text.encode(ENCODING,"ignore")
           page_text = page_text.decode(ENCODING)
           output_file.write(page_text)
    except Exception as e:
        print("Exception",e)
    else:
        pdfIn.close()
        output_file.close()

def is_valid_file_path(path):
    """
    Validates the path inputted and validate that it is a file path
    """
    if not path:
        raise ValueError(f"Invalid Path")
    if os.path.isfile(path) and 'pdf' in filetype.guess(path).mime:
       return path
    else:
       raise ValueError(f"Invalid Path {path}")

def is_valid_folder_path(path):
    """
    Validates the path inputted and checks whether it is a folder path
    """
    if not path:
        raise ValueError(f"Invalid Path")
    if os.path.isdir(path):
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
                      , '--output_path'
                      , dest='output_path'
                      , type=is_valid_folder_path
                      , help="Enter the path of an output file")

    parser.add_argument('-p'
                      , '--pages'
                      , dest='pages'
                      , type=str
                      , help="Enter the pages to consider e.g.: 0,1 or 2-3")

    args = vars(parser.parse_args())

    #To Display The Command Line Arguments
    print("## Command Arguments #################################################")
    print("\n".join("{}:{}".format(i,j) for i,j in args.items()))
    print("######################################################################")

    return args

if __name__ == '__main__':
    # Parsing command line arguments entered by user
    args = parse_args()
    pages_list  = build_range(args['pages']) if args['pages'] else None
    output_path = args['output_path'] if args['output_path'] else os.path.dirname(args['input_file'])

    extract_text_content(input_file  = args['input_file']
                       , output_path = output_path
                       , pages = pages_list
                        )
