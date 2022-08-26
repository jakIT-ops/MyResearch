#Import Libraries
import OpenSSL
import os,time, argparse, filetype
from PDFNetPython3.PDFNetPython import *

PATH_TO_CERTIFICATE = os.path.join(os.path.dirname(os.path.abspath(__file__)),"static","certificate")
PATH_TO_SIGNATURE   = os.path.join(os.path.dirname(os.path.abspath(__file__)),"static","signature")

def build_range(rangeval:str):
    """
    Build the range of pages based on the parameter inputted rangeval
    """
    result=set()
    for part in rangeval.split(','):
        x=part.split('-')
        result.update(range(int(x[0]),int(x[-1])+1))
    return list(sorted(result))

#Create a public/private key pair
def create_key_pair(type,bits):
    """
    Create a public and private key pair

    Arguments: Type refers to the key Type (TYPE_RSA or TYPE_DSA)
               bits number of bits used in the key (1024 or 2048 or 4096)
    """
    key_pair = OpenSSL.crypto.PKey()
    key_pair.generate_key(type,bits)
    return key_pair

#Create a self signed certificate
def create_self_signed_cert(key_pair):
    """
    Create a self signed certificate.
    This local certificate will not necessitate being signed by a Certificate Authority.
    """
    #Create a self signed certificate
    cert = OpenSSL.crypto.X509()
    # Common Name (example Company Name or Your Name)
    cert.get_subject().CN = "Educative"
    #Serial Number
    cert.set_serial_number(int(time.time() * 10))
    #Starting point not before
    cert.gmtime_adj_notBefore(0)
    #Lifespan - Expire after 10 years
    cert.gmtime_adj_notAfter(10 * 365 * 24 * 60 * 60)
    #Identify issue
    cert.set_issuer((cert.get_subject()))
    cert.set_pubkey(key_pair)
    # Cryptography algorithm (i.e.'sha256')
    cert.sign(key_pair, 'md5')
    return cert

def configure():
    """
    Configure the setup for the tool and generate a client self signed certificate
    """
    #Initialize an output summary
    summary = {}
    summary['OpenSSL Version'] = OpenSSL.__version__

    print('Generating and saving the private Key...')
    key_pair = create_key_pair(OpenSSL.crypto.TYPE_RSA,1024)

    with open(os.path.join(PATH_TO_CERTIFICATE,'private_key.pem') ,'wb') as pk:
        pk_str = OpenSSL.crypto.dump_privatekey(OpenSSL.crypto.FILETYPE_PEM
                                               ,key_pair
                                               )
        pk.write(pk_str)
        summary['Private Key'] = pk_str

    print('Generating the client self-signed client certificate...')
    ss_certificate = create_self_signed_cert(key_pair=key_pair)
    with open(os.path.join(PATH_TO_CERTIFICATE,'certificate.cer'),'wb') as cer:
        cer_str = OpenSSL.crypto.dump_certificate(OpenSSL.crypto.FILETYPE_PEM,ss_certificate)
        cer.write(cer_str)
        summary['Client Self Signed Certificate'] = cer_str

    print('Generating and saving the public Key...')
    with open(os.path.join(PATH_TO_CERTIFICATE,'public_key.pem'),'wb') as pub_key:
        pub_key_str = OpenSSL.crypto.dump_publickey(OpenSSL.crypto.FILETYPE_PEM
                                                     ,ss_certificate.get_pubkey())
        pub_key.write(pub_key_str)
        summary['Public Key'] = pub_key_str

    print('Generating a container file englobing the private key and the certificate...')
    p12 = OpenSSL.crypto.PKCS12()
    p12.set_privatekey(key_pair)
    p12.set_certificate(ss_certificate)
    open(os.path.join(PATH_TO_CERTIFICATE,'container.pfx'),'wb').write(p12.export())

    #To Display A Summary
    print("## Initialization Summary ##################################################")
    print("\n".join("{}:{}".format(i,j) for i,j in summary.items()))
    print("############################################################################")
    return True

def sign_pdf (input_file:str
             ,signature_ID:str
             ,x_coordinate:int
             ,y_coordinate:int
             ,pages:list=None
             ,output_file: str = None
             ):
    """
    Sign a PDF file
    """
    #Initialize the library
    PDFNet.Initialize()
    doc = PDFDoc(input_file)

    #Create a signature widget
    sigWidget = SignatureWidget.Create(doc, Rect(x_coordinate,y_coordinate,x_coordinate+100,y_coordinate+50),signature_ID)

    #Iterate throughout document pages
    for page in range(1, (doc.GetPageCount() + 1)):
        # If required for specific pages
        if pages:
           if page not in pages:
              continue

        pg = doc.GetPage(page)
        # Create a signature text field and push it on the page
        pg.AnnotPushBack(sigWidget)

    #Get the Signature image
    sign_filename = os.path.join(PATH_TO_SIGNATURE, 'signature.jpg')
    #Get the self signed certificate
    pk_filename   = os.path.join(PATH_TO_CERTIFICATE,'container.pfx')

    # Retrieve the signature field.
    approval_field = doc.GetField(signature_ID)
    approval_digital_signature_field = DigitalSignatureField(approval_field)

    #Add appearance to the signature field
    sign_img = Image.Create(doc.GetSDFDoc(), sign_filename)
    found_approval_signature_widget = SignatureWidget(approval_field.GetSDFObj())
    found_approval_signature_widget.CreateSignatureAppearance(sign_img)

    # Prepare the signature and signature handler for signing.
    approval_digital_signature_field.SignOnNextSave(pk_filename,'')

    #The signing will be done during the following incremental save operation.
    doc.Save(output_file, SDFDoc.e_incremental)

    #Compose a Process Summary
    summary = {
         "Input File": input_file
       , "Signature ID": signature_ID
       , "Output File": output_file
       , "Signature File": sign_filename
       , "Certificate File": pk_filename
    }

    # Print process Summary
    print("## Summary ########################################################")
    print("\n".join("{}:{}".format(i, j) for i, j in summary.items()))
    print("###################################################################")

    return True

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
    parser.add_argument('-c'
                       ,'--configure'
                       ,dest='configure'
                       ,action="store_true"
                       ,help = "Apply the required configurations and create the certificate")

    parser.add_argument('-i'
                       ,'--input_file'
                       ,dest='input_file'
                       ,type=is_valid_file_path
                       ,help = "Enter the path of the file to process")

    parser.add_argument('-o'
                      , '--output_file'
                      , dest='output_file'
                      , type=str
                      , help="Enter a valid output file")

    parser.add_argument('-s'
                      ,'--signature_ID'
                      ,dest='signature_ID'
                      ,type=str
                      ,help = "Enter the ID of the signature")

    parser.add_argument('-p'
                      , '--pages'
                      , dest='pages'
                      , type=str
                      , help="Enter the pages to consider e.g.: 0,1 or 2-3")

    parser.add_argument('-x'
                      , '--x_coordinate'
                      , dest='x_coordinate'
                      , type=int
                      , help="Enter the x coordinate.")

    parser.add_argument('-y'
                      , '--y_coordinate'
                      , dest='y_coordinate'
                      , type=int
                      , help="Enter the y coordinate.")

    args = vars(parser.parse_args())

    #To Display The Command Line Arguments
    print("## Command Arguments #################################################")
    print("\n".join("{}:{}".format(i,j) for i,j in args.items()))
    print("######################################################################")

    return args

if __name__ == '__main__':
    # Parsing command line arguments entered by user
    args = parse_args()

    if args['configure'] == True:
       configure()
    else:
        pages_list = build_range(args['pages']) if args['pages'] else None

        output_file = args['output_file'] if args['output_file'] \
            else os.path.join(os.path.dirname(args['input_file']),
                              os.path.splitext(os.path.basename(args['input_file']))[0] + "_signed.pdf")

        sign_pdf(input_file =args['input_file']
                ,signature_ID=args['signature_ID']
                ,x_coordinate=int(args['x_coordinate'])
                ,y_coordinate=int(args['y_coordinate'])
                ,pages=pages_list
                ,output_file=output_file
                )

