#Import Libraries
import os,argparse,filetype
from PDFNetPython3.PDFNetPython import PDFDoc, Optimizer, SDFDoc, PDFNet

def compress_file(input_file: str,output_file:str):
    """
    Compress the inputted PDF file
    """
    #Initialize output file
    if not output_file:
       output_file = input_file

    #Get the size of the file before compression
    size_initial = os.path.getsize(input_file)
    try:
      # --------------------------------------------
      # Initialize the library
      PDFNet.Initialize()
      doc = PDFDoc(input_file)
      # Optimize PDF with the default settings
      doc.InitSecurityHandler()
      # Reduce PDF size by removing redundant information and compressing data streams
      Optimizer.Optimize(doc)
      doc.Save(output_file, SDFDoc.e_linearized)
      # --------------------------------------------
    except Exception as e:
      print("Error compress_file=", e)
      return False
    else:
      doc.Close()

    # Get the size after compression
    size_compressed = os.path.getsize(output_file)
    # Compute the compression ration
    compression_ratio = 1 - (size_compressed / size_initial)

    summary = {
         "Input File": input_file
       , "Initial Size": "{0:.4f} MB".format(size_initial / 1000000)
       , "Output File": output_file
       , "Compressed Size": "{0:.4f} MB".format(size_compressed / 1000000)
       , "Compression Ratio": "{0:.4%}.".format(compression_ratio)
    }
    # Printing Summary
    print("## Summary ########################################################")
    print("\n".join("{}:{}".format(i, j) for i, j in summary.items()))
    print("###################################################################")

    return True

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
                      , help="Enter a valid output file")


    args = vars(parser.parse_args())

    #To Display The Command Line Arguments
    print("## Command Arguments #################################################")
    print("\n".join("{}:{}".format(i,j) for i,j in args.items()))
    print("######################################################################")

    return args

if __name__ == "__main__":
    # Parsing command line arguments entered by user
    args = parse_args()

    compress_file(input_file=args['input_file']
                , output_file=args['output_file']
                 )

