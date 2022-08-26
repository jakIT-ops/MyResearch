#Import libraries
import pikepdf
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

def extract_links(input_file:str
                 ,pages:list=None):
    """
    Extract the links from a PDF file and save them to an output text file
    """
    # Open the PDF
    pdfDoc = pikepdf.Pdf.open(input_file)

    pdf_urls=[]

    # Iterate through the PDF pages
    for pg, page in enumerate(pdfDoc.pages):
        pageID = pg+1
        #If required for specific pages
        if pages:
            if pageID not in pages:
                continue

        # Annotations found
        if page.get("/Annots"):
           for annots in page.get("/Annots"):
               if annots.get("/A") is not None:
                  #URL found
                  uri = annots.get("/A").get("/URI")
                  uri = str(uri).replace(" ","%20")
                  if uri is not None:
                     print(f"Hyperlink Found {uri} in Page {pageID}")
                     pdf_urls.append(uri)

    pdfDoc.close()
    print(f"Total Hyperlinks Extracted = {len(pdf_urls)}")

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
    extract_links(input_file=args['input_file']
                 , pages=pages_list
                 )
