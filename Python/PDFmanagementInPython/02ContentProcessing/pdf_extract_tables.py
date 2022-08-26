#Import Libraries
import os,argparse,filetype
import tabula

def build_range(rangeval:str):
    """
    Build the range of pages based on the parameter inputted rangeval
    """
    result=set()
    for part in rangeval.split(','):
        x=part.split('-')
        result.update(range(int(x[0]),int(x[-1])+1))
    return list(sorted(result))

def extract_tables(input_file:str
                  ,output_path:str
                  ,pages:str):
    """
    Extract tabular data from a PDF document and save it as CSV to the output path
    """
    #Open the document
    dfs = tabula.read_pdf(input_file,pages=pages,stream=True,multiple_tables=True)
    #Display the length of dataframes collected
    print (f"{len(dfs)} tables extracted..." )
    #Convert each data frame to CSV and save it to the output folder
    for i,df in enumerate(dfs,start=1):
        csv_name = os.path.join(output_path
                               ,os.path.splitext(os.path.basename(input_file))[0] + "_" + str(i) + ".csv")
        df.to_csv(csv_name,index=False)

def is_valid_file_path(path):
    """
    Validate the path inputted and make sure it is a file path
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
                      , help="Enter the path of an output folder")

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
    # Building a page range
    pages_list  = build_range(args['pages']) if args['pages'] else "all"
    # If the output path is empty, initialize it with path of the input file
    output_path = args['output_path'] if args['output_path'] else os.path.dirname(args['input_file'])

    extract_tables(input_file  = args['input_file']
                 , output_path = output_path
                 , pages = pages_list
                   )
