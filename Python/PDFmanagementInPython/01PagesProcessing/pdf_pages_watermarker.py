from PyPDF4 import PdfFileReader, PdfFileWriter
from PyPDF4.pdf import ContentStream
from PyPDF4.generic import TextStringObject, NameObject
from PyPDF4.utils import b_
import os, argparse, filetype
from io import BytesIO
from typing import Tuple

def build_range(rangeval:str):
    """
    Build the range of pages based on the parameter inputted rangeval
    """
    result=set()
    for part in rangeval.split(','):
        x=part.split('-')
        result.update(range(int(x[0]),int(x[-1])+1))
    return list(sorted(result))

def create_watermark(wm_text: str):
    """
    Creates the template for the watermark.
    """
    #Import the reportlab library
    from reportlab.pdfgen import canvas
    #Import the watermark configuration parameters
    import config_watermarker

    if wm_text:
        #Generate the output to a memory buffer
        output_buffer = BytesIO()

        #Default Page Size = A4
        c = canvas.Canvas(output_buffer,pagesize=config_watermarker.PAGESIZE)
        #Select the font type and the font size
        c.setFont(config_watermarker.FONTNAME,config_watermarker.FONTSIZE)
        # Set the color
        c.setFillColor(config_watermarker.COLOR)
        #Rotate according to the configured parameter
        c.rotate(config_watermarker.ROTATION_ANGLE)
        #Position according to the configured parameter
        c.drawString(config_watermarker.X,config_watermarker.Y,wm_text)
        c.save()

        return True, output_buffer

    return False, None

def watermark_file(input_file:str,wm_text: str,pages:list=None):
    """
    Adds a watermark overlay to a pdf file.
    """
    result, wm_buffer = create_watermark(wm_text)
    if result:
       wm_reader = PdfFileReader(wm_buffer)
       pdf_reader = PdfFileReader(open(input_file, 'rb'), strict=False)
       pdf_writer = PdfFileWriter()
       try:

        for pg in range(pdf_reader.getNumPages()):
            page = pdf_reader.getPage(pg)

            # If required to watermark specific pages not all the document pages
            if pages is None or (pg+1) in pages:
               page.mergePage(wm_reader.getPage(0))

            pdf_writer.addPage(page)
       except Exception as e:
         print("Exception = ",e)
         return False, None, None

       return True, pdf_reader , pdf_writer

def unwatermark_file(input_file:str,wm_text: str,pages:list=None):
    """
    Removes watermark from the pdf file.
    """
    pdf_reader = PdfFileReader(open(input_file, 'rb'), strict=False)
    pdf_writer = PdfFileWriter()

    for pg in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(pg)
        # If required for specific pages
        if pages is None or (pg + 1) in pages:
                #Get the page content
                content_object = page["/Contents"].getObject()
                content = ContentStream(content_object,pdf_reader)
                #Loop through all the elements page elements
                for operands, operator in content.operations:
                    #Checks the TJ operator and replaces the corresponding string operand (Watermark text) with ''
                    if operator == b_("Tj"):
                       text = operands[0]
                       if isinstance(text,str) and text.startswith(wm_text):
                          operands[0] = TextStringObject('')
                page.__setitem__(NameObject('/Contents'),content)

        pdf_writer.addPage(page)
    return True, pdf_reader, pdf_writer

def process_file(**kwargs):
    input_file  = kwargs.get('input_file')
    wm_text     = kwargs.get('wm_text')

    # watermark   -> Watermark
    # unwatermark -> Unwatermark
    action      = kwargs.get('action')
    pages       = kwargs.get('pages')

    if action == "watermark":
       result , pdf_reader , pdf_writer = watermark_file(input_file = input_file, wm_text= wm_text, pages=pages)
    elif action == "unwatermark":
       result, pdf_reader, pdf_writer = unwatermark_file(input_file = input_file, wm_text= wm_text, pages=pages)

    #Completed successfully
    if result:
       # Create a memory buffer
       output_buffer = BytesIO()
       pdf_writer.write(output_buffer)
       pdf_reader.stream.close()
       output_file = input_file
       with open(output_file, mode='wb') as f:
            f.write(output_buffer.getbuffer())
       f.close()

def is_valid_path(path):
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
                       ,type=is_valid_path
                       ,required=True
                       ,help = "Enter the path of the file or the folder to process")

    parser.add_argument('-a'
                      , '--action'
                      , dest='action'
                      , choices=['watermark', 'unwatermark']
                      , type=str
                      , default='watermark'
                      , help="Choose whether to watermark or to unwatermark")

    parser.add_argument('-w'
                      , '--watermark_text'
                      , dest='watermark_text'
                      , type=str
                      , required=True
                      , help="Enter a valid watermark text")

    parser.add_argument('-p'
                      , '--pages'
                      , dest='pages'
                      , type=str
                      , help="Enter the pages to consider e.g.: [2,4]")

    #To Porse The Command Line Arguments
    args = vars(parser.parse_args())

    #To Display The Command Line Arguments
    print("## Command Arguments #################################################")
    print("\n".join("{}:{}".format(i,j) for i,j in args.items()))
    print("######################################################################")

    return args

if __name__ == '__main__':
    # Parsing command line arguments entered by user
    args = parse_args()
    pages_list = None
    if args['pages']:
       pages_list = build_range(args['pages'])

    process_file(
              input_file=args['input_file']
            , wm_text=args['watermark_text']
            , action=args['action']
            , pages=pages_list
        )
