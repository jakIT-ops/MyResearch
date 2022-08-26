#Import Libraries
from pdf2docx import parse
import os,argparse,filetype

def build_range(rangeval:str):
    """
    Build the range of pages based on the parameter inputted rangeval
    """
    result=set()
    for part in rangeval.split(','):
        x=part.split('-')
        result.update(range(int(x[0]),int(x[-1])+1))
    return list(sorted(result))

def convert_pdf2docx(input_file:str
                    ,output_file:str
                    ,pages:str = None
                    ):
    """
    Converts pdf to docx
    """
    result = parse(pdf_file=input_file
                  ,docx_with_path=output_file
                  ,pages=pages)
    summary = {
        "File":input_file
       ,"Pages":str(pages)
       ,"Output File":output_file
    }

    #Printing Summary
    print("## Summary ########################################################")
    print("\n".join("{}:{}".format(i,j) for i,j in summary.items()))
    print("###################################################################")
    return result

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
                       , help="Enter the path of the output file")

    parser.add_argument('-p'
                      , '--pages'
                      , dest='pages'
                      , type=str
                      , help="Enter the pages to consider e.g.: [0,1]")

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
    output_file = args['output_file'] if args['output_file'] \
                      else os.path.join(os.path.dirname(args['input_file']),os.path.splitext(os.path.basename(args['input_file']))[0] + ".docx")
    if pages_list:
       pages_list = [i-1 for i in pages_list]
    convert_pdf2docx(input_file  = args['input_file']
                   , output_file = output_file
                   , pages = pages_list
                    )

