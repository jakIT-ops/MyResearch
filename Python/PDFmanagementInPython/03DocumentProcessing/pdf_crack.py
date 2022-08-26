#Import Libraries
import pikepdf
import os,argparse,string,random,filetype

MINIMUM_PASSWORD_LENGTH = 1
MAXIMUM_PASSWORD_LENGTH = 4
MAXIMUM_PASSWORD_COUNT  = 100000
PASSWORD_CHARACTERS     = string.digits

def is_pdf_encrypted(input_file:str) -> bool:
    """
    Check if the selected PDF file is encrypted
    """
    is_encrypted = False
    try:
       with pikepdf.open(input_file) as pdf:
            is_encrypted = False
    except pikepdf._qpdf.PasswordError as e:
            is_encrypted = True
    return is_encrypted

def generate_passwords():
    """
    Generate random passwords while respecting the set global parameters.
    """
    for counter in range(0,MAXIMUM_PASSWORD_COUNT):
        password_option = ''
        for chr in random.sample(PASSWORD_CHARACTERS
                                ,random.randint(MINIMUM_PASSWORD_LENGTH,MAXIMUM_PASSWORD_LENGTH)):
            password_option += chr
        yield password_option

def crack_pdf_file(input_file:str, password_generator):
    """
    Crack an encrypted PDF file.
    """
    if not is_pdf_encrypted(input_file=input_file):
       print(f"The file {input_file} is not encrypted.")
       return

    trials = 0
    #Loop through the passwords generated
    for passw in password_generator:
        trials += 1
        try:
            print(f"Trial {trials} / Password {passw}")
            with pikepdf.open(input_file, password=passw) as pdf:
                 print(f"Password found {passw} for file {input_file}.")
                 break
        # if password did not match
        except pikepdf._qpdf.PasswordError as e:
            # wrong password, just continue in the loop
            continue

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

def parse_args():
    """
    Get user command line parameters
    """
    parser = argparse.ArgumentParser(description="This option is available")

    parser.add_argument('-i'
                       ,'--input_file'
                       ,dest='input_file'
                       ,type=is_valid_file_path
                       ,required=True
                       ,help = "Enter the path of the file to process")

    args = vars(parser.parse_args())

    #To Display Command Arguments Except Password
    print("## Command Arguments #################################################")
    print("\n".join("{}:{}".format(i,j) for i,j in args.items() if i != 'password'))
    print("######################################################################")

    return args


if __name__ == '__main__':
    # Parsing command line arguments entered by user
    args = parse_args()

    crack_pdf_file(input_file=args['input_file']
                  ,password_generator = generate_passwords()
                  )
