#Import libraries
import os,argparse,filetype
from PyPDF4 import PdfFileReader, PdfFileWriter

def shuffle_pdf_pages(input_file:str
                   ,output_file:str
                   ,pages:list=None):
    """
    Shuffle pages in a PDF file based on a page sequence presented
    """
    pdf_in  = PdfFileReader(open(input_file,'rb'),strict=False)
    pdf_out = PdfFileWriter()
    try:
        for pg in pages:
            if (pg-1) in range(pdf_in.getNumPages()):
               page = pdf_in.getPage((pg-1))
               pdf_out.addPage(page)
    except Exception as e:
        print("Exception",e)
    else:
        with open(output_file, 'wb') as pdf_output_file:
             pdf_out.write(pdf_output_file)
        pdf_output_file.close()
        pdf_in.stream.close()

def is_valid_path(path):
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
                       ,type=is_valid_path
                       ,required=True
                       ,help = "Enter the path of the file to process")

    parser.add_argument('-o'
                      , '--output_file'
                      , dest='output_file'
                      , type=str
                      , required=True
                      , help="Enter the path of an output file")

    parser.add_argument('-p'
                      , '--pages'
                      , dest='pages'
                      , type=str
                      , required=True
                      , help="Enter the pages to consider e.g.: 0,1 or 2-3")

    args = vars(parser.parse_args())

    #To Display The Command Line Arguments
    print("## Command Arguments #################################################")
    print("\n".join("{}:{}".format(i,j) for i,j in args.items()))
    print("######################################################################")

    return args

if __name__ == "__main__":
   # Parsing command line arguments entered by user
   args = parse_args()

   pages_list = [int(i) for i in args['pages'] if i.isdigit()]
   shuffle_pdf_pages(input_file  = args['input_file']
                   , output_file = args['output_file']
                   , pages = pages_list
                    )
