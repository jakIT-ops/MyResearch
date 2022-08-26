#Import libraries
import fitz
from PIL import Image
import io,os,argparse,filetype

def build_range(rangeval:str):
    """
    Build the range of pages based on the parameter inputted rangeval
    """
    result=set()
    for part in rangeval.split(','):
        x=part.split('-')
        result.update(range(int(x[0]),int(x[-1])+1))
    return list(sorted(result))

def extract_images(input_file:str
                   ,output_path:str
                   ,pages:list=None):
    """
    Extract the images from a PDF file and save them to the output folder
    """
    # Open the PDF
    pdfDoc = fitz.open(input_file)

    # Iterate through the PDF pages
    for pg in range(pdfDoc.pageCount):
        pageID = pg+1
        #If required for specific pages
        if pages:
            if pageID not in pages:
                continue

        #Select a page
        page = pdfDoc[pg]

        #Extract images in the page
        page_images = page.getImageList()

        images_count = 0
        if page_images:
           images_count = len(page_images)
        print(f"Processing page {pageID} -- {images_count} image(s) exist.")

        #Loop throughout the page images
        for img_idx , img in enumerate(page_images,start=1):
            #access the image xref
            img_xref = img[0]
            #extract the image
            img_content = pdfDoc.extractImage(img_xref)
            #Extract the image content
            img_binary = img_content["image"]
            #Extract the image extension
            img_ext = img_content["ext"]
            #Create the output image
            img_out = Image.open(io.BytesIO(img_binary))
            # Output Base File Name
            output_fileName = os.path.join(output_path, os.path.splitext(os.path.basename(input_file))[0])
            # Save the output image
            img_out.save(open(f"{output_fileName}_Page{pageID}_Image{img_idx}.{img_ext}", "wb"))
            img_out.close()
    pdfDoc.close()

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


def is_valid_folder_path(path):
    """
    Validate the path inputted and make sure it is a folder path
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
                      , required=True
                      , help="Enter the path of the output folder")

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


if __name__ == "__main__":
    # Parsing command line arguments entered by user
    args = parse_args()
    # Generate a page range
    pages_list = build_range(args['pages']) if args['pages'] else None
    extract_images(input_file=args['input_file']
                 , output_path=args['output_path']
                 , pages=pages_list
                 )
