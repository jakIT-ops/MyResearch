import hashlib,os,argparse

#Size of chunck
BUFFER_SIZE = 8192

def verify_algorithm(hash_algorithm:str):
    """
    Verify that the selected algorithm is part of the list of algorithms defined in the module
    """
    if hash_algorithm in hashlib.algorithms_guaranteed:
       return True
    print('Select an algorithm out of the guaranteed algorithms list:',hashlib.algorithms_guaranteed)
    return False

def generate_hashfunc(hash_algorithm:str):
    """
    Generate a hashing function depending on the hashing algorithm specified
    """
    if verify_algorithm(hash_algorithm):
       hashfunc = getattr(hashlib,hash_algorithm)
       return hashfunc
    return None

def compute_checksum(input_file:str
                 ,hash_algorithm:str):
    """
    Generate checksum for a file based on the hashing algorithm select
    """
    hash_func = generate_hashfunc(hash_algorithm.lower())
    if hash_func:
       #Instantiate the hashing function
       hash_func = hash_func()
       with open(input_file,'rb') as inp:
            #Read an input file as chunks of bytes
            chunk = inp.read(BUFFER_SIZE)
            while chunk:
                  #Append the chunk of bytes to the secure hash value
                  hash_func.update(chunk)
                  chunk = inp.read(BUFFER_SIZE)

       return hash_func.digest(), hash_func.hexdigest()

    return None, None

def is_valid_path(path):
    """
    Validates the path inputted and checks if it is a file path
    """
    if not path:
        raise ValueError(f"Invalid Path")
    if os.path.isfile(path):
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
                       ,type=is_valid_path
                       ,required=True
                       ,help = "Enter the path of the file to process")

    parser.add_argument('-a'
                      , '--algorithm'
                      , dest='algorithm'
                      , type=str
                      , required=True
                      , help = "Choose an algorithm")
    args = vars(parser.parse_args())

    #To Display The Command Line Arguments
    print("## Command Arguments #################################################")
    print("\n".join("{}:{}".format(i,j) for i,j in args.items()))
    print("######################################################################")

    return args


if __name__ == "__main__":
    # Parsing command line arguments entered by user
    args = parse_args()

    # If File Path
    if os.path.isfile(args['input_path']):
       hash_func_digest, hash_func_hexdigest = compute_checksum(input_file     = args['input_path']
                                                              , hash_algorithm = args['algorithm']
                                                               )

       print('Digest',hash_func_digest)
       print('Hexdigest',hash_func_hexdigest)
