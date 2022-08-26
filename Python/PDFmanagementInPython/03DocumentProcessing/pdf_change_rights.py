#Import Libraries
from PyPDF4 import PdfFileReader, PdfFileWriter
import os,argparse,filetype,getpass

def changeAccessRights(pdfWriter
                      ,access_rights
                      ,user_pwd=''
                      ,owner_pwd=None
                      ,use_128bit=True
                       ):
    """
    Encrypt the PDF file while changing its access rights
    """
    from PyPDF4.generic import NameObject, DictionaryObject, ArrayObject, \
        NumberObject, ByteStringObject
    from PyPDF4.pdf import _alg33, _alg34, _alg35
    from PyPDF4.utils import b_
    from hashlib import md5
    import time, random

    #Set the owner password to the user password.
    if owner_pwd == None:
       owner_pwd = user_pwd

    #Set the length of the encryption key 40 or 128 bit
    #V = code specifying the algorithm to be used in encrypting of decrypting the document.
    if use_128bit:
        V = 2
        rev = 3
        keylen = int(128 / 8)
    else:
        V = 1
        rev = 2
        keylen = int(40 / 8)

    #Set User permissions
    P = (-1) * access_rights

    #Computing the encryption key
    O    = ByteStringObject(_alg33(owner_pwd, user_pwd, rev, keylen))
    ID_1 = ByteStringObject(md5(b_(repr(time.time()))).digest())
    ID_2 = ByteStringObject(md5(b_(repr(random.random()))).digest())

    pdfWriter._ID = ArrayObject((ID_1, ID_2))
    if rev == 2:
        U, key = _alg34(user_pwd, O, P, ID_1)
    else:
        assert rev == 3
        U, key = _alg35(user_pwd, rev, keylen, O, P, ID_1, False)

    #Define the specifications dictionary.
    encrypt = DictionaryObject()

    #The name of the preferred document security handler.
    #Standard is the name of the built-in password-based security handler.
    encrypt[NameObject("/Filter")] = NameObject("/Standard")
    encrypt[NameObject("/V")]      = NumberObject(V)

    if V == 2:
       #Length of the encryption key in bits. The value must be multiple of 8. Default=40.
       encrypt[NameObject("/Length")] = NumberObject(keylen * 8)

    #A number specifying the revision of the standard security handler.
    encrypt[NameObject("/R")] = NumberObject(rev)
    # A 32-byte string indicating whether a valid owner password was entered.
    encrypt[NameObject("/O")] = ByteStringObject(O)
    # A 32-byte string used to prompt the user for a password.
    encrypt[NameObject("/U")] = ByteStringObject(U)
    # A set of flags specifying which operations are permitted when the document is opened.
    encrypt[NameObject("/P")] = NumberObject(P)

    # Add the specifications dictionary.
    pdfWriter._encrypt = pdfWriter._addObject(encrypt)
    pdfWriter._encrypt_key = key

def change_rights(input_file:str
                 ,output_file:str
                 ,access_rights:int
                 ,user_pwd:str=''
                 ,owner_pwd:str=None
                 ):
    """
    Change PDF permissions
    """
    pdf_in  = PdfFileReader(open(input_file,'rb'),strict=False)
    pdf_out = PdfFileWriter()
    try:
        pdf_out.appendPagesFromReader(pdf_in)
        changeAccessRights(pdfWriter=pdf_out
                         , access_rights=access_rights
                         , user_pwd=user_pwd
                         , owner_pwd=owner_pwd
                         , use_128bit=True
                         )

    except Exception as e:
        print("Exception",e)
    else:
        with open(output_file, 'wb') as pdf_output_file:
            pdf_out.write(pdf_output_file)
        pdf_output_file.close()
        pdf_in.stream.close()

    #Process Summary
    summary = {
         "Input File": input_file
       , "Access Rights":access_rights
       , "Output File": output_file
    }

    # Print process Summary
    print("## Summary ########################################################")
    print("\n".join("{}:{}".format(i, j) for i, j in summary.items()))
    print("###################################################################")

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

class Password(argparse.Action):
    """
    Hides the password entry
    """
    def __call__(self,parser,namespace,values,option_string):
        if values is None:
           values = getpass.getpass()
        setattr(namespace,self.dest,values)

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

    parser.add_argument('-r'
                      , '--access_rights'
                      , dest='access_rights'
                      , type=int
                      , required=True
                      , help="Enter the appropriate code for access rights")

    parser.add_argument('-o'
                      , '--output_file'
                      , dest='output_file'
                      , type=str  # lambda x: os.path.has_valid_dir_syntax(x)
                      , help="Enter a valid output file")

    parser.add_argument('-a'
                      , '--user_pwd'
                      , dest='user_pwd'
                      , action=Password
                      , nargs= '?'
                      , type=str
                      , default=''
                      , help="Enter a valid user password")

    parser.add_argument('-b'
                      , '--owner_pwd'
                      , dest='owner_pwd'
                      , action=Password
                      , nargs= '?'
                      , type=str
                      , default = None
                      , help="Enter a valid owner password")

    #To Porse The Command Line Arguments
    args = vars(parser.parse_args())

    #To Display The Command Line Arguments
    print("## Command Arguments #################################################")
    print("\n".join("{}:{}".format(i,j) for i,j in args.items()))
    print("######################################################################")

    return args


if __name__ == "__main__":
    #Parsing command line arguments entered by user
    args = parse_args()

    ##Access Rights
    # -0    --> Disable all options.
    # -3904 --> Disable all options.
    # -1    --> Permit all options.
    # -1852 --> Enable only high quality printing.
    # -3376 --> Enable content copying or extraction and Content extraction for Accessibility.
    # -3872 --> Enable Add or modify text annotations, fill in interactive form fields
    #Change PDF rights
    change_rights(input_file    = args['input_file']
                , output_file   = args['output_file']
                , access_rights = args['access_rights']
                , user_pwd      = args['user_pwd']
                , owner_pwd     = args['owner_pwd']
                 )
