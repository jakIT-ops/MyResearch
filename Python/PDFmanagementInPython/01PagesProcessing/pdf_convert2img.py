#Import Libraries
import os,argparse,filetype
import fitz

def build_range(rangeval:str):
    """
    Build the range of pages based on the parameter inputted rangeval
    """
    result=set()
    for part in rangeval.split(','):
        x=part.split('-')
        result.update(range(int(x[0]),int(x[-1])+1))
    return list(sorted(result))

def convert_pdf2img(input_file:str
                   ,output_type:str
                   ,pages:list =None):
    """
    Converts pdf to image and generates an image file by page
    """
    #Open the document
    pdfIn = fitz.open(input_file)
    output_files = []

    #Iterate throughout the pages
    for pg in range(pdfIn.pageCount):
        pageID = pg+1

        if pages:
            if pageID not in pages:
                continue

        #Select a page
        page = pdfIn[pg]
        rotate = int(0)

        # PDF Page is converted into a whole picture 1056*816 and then for each picture a screenshot is taken.
        # zoom = 1.33333333 -----> Image size = 1056*816
        # zoom = 2 ---> 2 * Default Resolution (text is clear, image text is hard to read)    = filesize small / Image size = 1584*1224
        # zoom = 4 ---> 4 * Default Resolution (text is clear, image text is barely readable) = filesize large
        # zoom = 8 ---> 8 * Default Resolution (text is clear, image text is readable) = filesize large
        zoom_x = 2
        zoom_y = 2
        # The zoom factor is equal to 2 in order to make text clear
        # Pre-rotate is to rotate if needed.
        mat = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)

        pix = page.getPixmap(matrix=mat, alpha=False)

        output_file = os.path.join(os.path.dirname(input_file)
                                , (os.path.splitext(os.path.basename(input_file))[0]) + '_Page' + str(pg+1) + '.' + output_type)
        pix.writePNG(output_file)

        output_files.append(output_file)
    pdfIn.close()

    summary = {
        "File":input_file
       ,"Pages":str(pages)
       ,"Output File(s)":str(output_files)
    }
    #Printing Summary
    print("## Summary ########################################################")
    print("\n".join("{}:{}".format(i,j) for i,j in summary.items()))
    print("###################################################################")

    return output_files

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
                       ,'--input_path'
                       ,dest='input_path'
                       ,type=is_valid_file_path
                       ,required=True
                       ,help = "Enter the path of the file or the folder to process")

    parser.add_argument('-t'
                      , '--type'
                      , dest='type'
                      , choices=['jpg','png']
                      , type=str
                      , required=True
                      , help="Choose the output type")

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

    convert_pdf2img(input_file  = args['input_path']
                  , output_type = args['type']
                  , pages = pages_list
                   )
