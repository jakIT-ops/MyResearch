#Import Libraries
from PyPDF4 import PdfFileReader, PdfFileWriter, utils
import os, argparse,getpass, filetype
from io import BytesIO

def is_pdf_encrypted(input_file:str) -> bool:
    """
    Check if the selected PDF file is encrypted
    """
    with open(input_file,'rb') as pdf_file:
        pdf_reader = PdfFileReader(pdf_file,strict=False)
        return pdf_reader.isEncrypted

#########################################################################################################
def encrypt_pdf_file(input_file:str, password:str):
    """
    Encrypt a PDF file provided that that the latter is not already encrypted.
    """
    pdf_wtr = PdfFileWriter()
    pdf_rdr = PdfFileReader(open(input_file, 'rb'), strict=False)

    if pdf_rdr.isEncrypted:
       print(f"The selected file {input_file} is encrypted")
       return False, None, None

    try:
      #Loop throughout all the pages of the PDF file, encrypt them and add them to the writer.
      for pg in range(pdf_rdr.numPages):
          pdf_wtr.addPage(pdf_rdr.getPage(pg))
    except utils.PdfReadError as e:
      print(f"Error when looping through the PDF File {input_file} = {e}")
      return False, None, None

    #By default 128 bit encryption
    #If use_128bit = False then 40 bit encryption.
    pdf_wtr.encrypt(user_pwd=password,owner_pwd=None,use_128bit=True)

    return True, pdf_rdr , pdf_wtr

def decrypt_pdf_file(input_file:str, password:str):
    """
    Decrypt a PDF file provided that the latter is already encrypted
    """
    pdf_rdr = PdfFileReader(open(input_file,'rb'), strict=False)
    if not pdf_rdr.isEncrypted:
       print(f"The selected file {input_file} is not encrypted")
       return False, None, None

    pdf_rdr.decrypt(password=password)
    pdf_wtr = PdfFileWriter()
    try:
        for pg in range(pdf_rdr.numPages):
            pdf_wtr.addPage(pdf_rdr.getPage(pg))
    except utils.PdfReadError as e:
        print(f"Error when looping through the PDF File {input_file} = {e}")
        return False , None, None

    return True , pdf_rdr , pdf_wtr

def process_file(**kwargs):
    """
    Encrypt/Decrypt a PDF file
    """
    #PDF file to process
    input_file  = kwargs.get('input_file')
    #The password to apply
    password    = kwargs.get('password')
    #The output processed file
    output_file = kwargs.get('output_file')
    # encrypt / decrypt
    action      = kwargs.get('action')

    if not output_file:
       output_file = input_file

    if action == "encrypt":
       result , pdf_rdr , pdf_wtr = encrypt_pdf_file(input_file = input_file, password= password)

       #The encryption process has completed
       if result:
          out_buffer = BytesIO()
          pdf_wtr.write(out_buffer)
          pdf_rdr.stream.close()
          with open(output_file, mode='wb') as f:
               f.write(out_buffer.getbuffer())
          f.close()

    elif action == "decrypt":
         result, pdf_rdr, pdf_wtr = decrypt_pdf_file(input_file=input_file, password=password)

         #The decryption process has completed
         if result:
            out_buffer = BytesIO()
            pdf_wtr.write(out_buffer)
            pdf_rdr.stream.close()
            with open(output_file, mode='wb') as f:
                 f.write(out_buffer.getbuffer())
            f.close()

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


class Password(argparse.Action):
    """
    Hide entry of the password when passed as argument
    """
    def __call__(self,parser,namespace,values,option_string):
        if values is None:
           values = getpass.getpass()
        setattr(namespace,self.dest,values)

def parse_args():
    """
    Get user command line parameters
    """
    parser = argparse.ArgumentParser(description="These options are available")

    parser.add_argument('-i'
                       ,'--input_path'
                       ,dest='input_path'
                       ,type=is_valid_file_path
                       ,required=True
                       ,help = "Enter the path of the file to process")

    parser.add_argument('-a'
                      , '--action'
                      , dest='action'
                      , choices=['encrypt', 'decrypt']
                      , type=str
                      , default='encrypt'
                      , help="Select whether to encrypt or to decrypt")

    parser.add_argument('-p'
                      , '--password'
                      , dest='password'
                      , action=Password
                      , nargs= '?'
                      , type=str
                      , required=True
                      , help="Choose a password")

    parser.add_argument('-o'
                      , '--output_file'
                      , dest='output_file'
                      , type=str
                      , help="Enter a valid output file")

    args = vars(parser.parse_args())

    #To Display Command Arguments Except Password
    print("## Command Arguments #################################################")
    print("\n".join("{}:{}".format(i,j) for i,j in args.items() if i != 'password'))
    print("######################################################################")

    return args


if __name__ == '__main__':
    # Parsing command line arguments entered by user
    args = parse_args()

    process_file(
                 input_file=args['input_path']
               , action=args['action']
               , password=args['password']
               , output_file=args['output_file']
               )
