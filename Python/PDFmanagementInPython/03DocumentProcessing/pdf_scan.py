# Import Libraries
import os, re, argparse
import pytesseract
from pytesseract import Output
import cv2
import numpy as np
import fitz
from io import BytesIO
from PIL import Image
import pandas as pd
import filetype

# Tesseract OCR engine Path
TESSERACT_PATH = r"tesseract"

# Include tesseract executable
pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH
################################################################################
def build_range(rangeval:str):
    """
    Build the range of pages based on the parameter inputted rangeval
    """
    result=set()
    for part in rangeval.split(','):
        x=part.split('-')
        result.update(range(int(x[0]),int(x[-1])+1))
    return list(sorted(result))
################################################################################
def pixmap2numpy(pix):
    """
    Convert a screenshot / pixmap into a numpy array
    """
    # pix.samples = sequence of the image pixels like RGBA
    # pix.h = Image height in pixels
    # pix.w = Image width in pixels
    # pix.n = Components per pixel
    im = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.h, pix.w, pix.n)
    try:
        #Convert RGB To BGR
        im = np.ascontiguousarray(im[..., [2, 1, 0]])
    except IndexError:
        # Convert Gray to RGB
        im = cv2.cvtColor(im, cv2.COLOR_GRAY2RGB)
        # Convert RGB To BGR
        im = np.ascontiguousarray(im[..., [2, 1, 0]])
    return im
################################################################################
#Iimproving output accurracy by applying these Pre-Processing Image Functions
def grayscale_image(img):
    """
    Convert image to grayscale
    """
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def threshold_image(img):
    """
    Threshold image
    """
    return cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

################################################################################
def convert_img2bin(img):
    """
    Pre-processes the image and generates a binary output
    """
    # Convert the image into grayscale
    output_img = grayscale_image(img)

    # Invert the grayscale image by flipping pixel values.
    # All pixels that are greater than 0 are set to 0.
    # All pixels that are = to 0 are set to 255
    output_img = cv2.bitwise_not(output_img)

    # Converting the image into binary by thresholding that to distinguish between white and black pixels.
    output_img = threshold_image(output_img)
    return output_img
################################################################################
def convert_img2bytearray(image: Image):
    """
    Converts an image into a byte array
    """
    img_ByteArr = BytesIO()
    image.save(img_ByteArr, format=image.format if image.format else 'JPEG')
    img_ByteArr = img_ByteArr.getvalue()
    return img_ByteArr
################################################################################
def generate_image_text(ss_details):
    """
    Iterate through the captured text of the image and arrange this text line by line.
    """
    parse_text = []
    words_list = []
    last_word = ''

    # Loop through the captured text of the entire page
    for word in ss_details['text']:
        # If the word captured is not empty
        if word != '':
            # Add it to the line word list
            words_list.append(word)
            last_word = word

        if (last_word != '' and word == '') or (word == ss_details['text'][-1]):
            parse_text.append(words_list)
            words_list = []

    return parse_text


################################################################################
def save_page_content(pdfContent, page_id, page_data):
    """
    Append the content of the scanned page to a pandas DataFrame line by line.
    """
    if page_data:
        for idx, line in enumerate(page_data, 1):
            line = ' '.join(line)
            pdfContent = pdfContent.append(
                {'page': page_id, 'line_id': idx, 'line': line}
                , ignore_index=True
            )
    return pdfContent


def save_doc_content(pdfContent, input_file , output_path):
    """
    Save the content of the pandas DataFrame to a CSV file having the same path as the input_file
    but with different extension (.csv)
    """
    content_file = os.path.join(output_path
                 , os.path.splitext(os.path.basename(input_file))[0] + ".csv")
    pdfContent.to_csv(content_file, sep=',', index=False)
    return content_file


################################################################################
def calculate_page_confidence(ss_details: dict):
    """
    Calculate the score of confidence of the text grabbed from the scanned page.
    """
    # page_num  --> Page number of the detected text or item
    # block_num --> Block number of the detected text or item
    # par_num   --> Paragraph number of the detected text or item
    # line_num  --> Line number of the detected text or item

    # Convert the dict to dataFrame
    df = pd.DataFrame.from_dict(ss_details)
    # Convert the field conf (confidence) to numeric
    df['conf'] = pd.to_numeric(df['conf'], errors='coerce')
    # Elliminate records with negative confidence
    df = df[df.conf != -1]
    # Calculate the mean confidence by page
    conf = df.groupby(['page_num'])['conf'].mean().tolist()
    return conf[0]


################################################################################
def scan_image(img: np.array
             , comparison_file: str
             , search_str: str
             , highlight_readable_text: bool = False
             , action: str = 'Highlight'
             , show_comparison: bool = False
             , generate_output: bool = True
             ):
    """
    Scan an image buffer.
    Pre-process the image.
    Call the OCR Tesseract engine with pre-defined parameters.
    Calculate the confidence score of the grabbed content of the image.
    Draw a green rectangle around the readable text items having a confidence score > 30.
    Search for a specific text value.
    Highlight or redact found matches of the searched text values.
    Save an  showing the readable text fields or the highlighted or redacted text.
    Generate the text content of the image.
    Print a summary to the console.
    """
    # Maintain a copy of the image for comparison
    original_img    = img.copy()
    highlighted_img = img.copy()

    # Convert image to binary
    bin_img = convert_img2bin(img)

    # Calling Tesseract
    # Tesseract Configuration parameters
    # oem --> The mode of the OCR engine = 3  Legacy + LSTM mode only.
    # psm --> The mode of page segmentation = 6 >> How a page of text can be analyzed

    config_param = r'--oem 3 --psm 6'
    # Feeding image to tesseract
    details = pytesseract.image_to_data(bin_img, output_type=Output.DICT
                                        , config=config_param, lang='eng')
    # The details dictionary will contain all the information of the input image
    # such as text detected, position, information, region, height, width and confidence score.
    pg_confidence = calculate_page_confidence(details)

    boxed_img = None
    # Total page readable items
    pg_readable_items = 0
    # Total page matches found
    pg_matches = 0

    for seq in range(len(details['text'])):
        # Consider only the text fields having a confidence score > 30 (text is readable)
        if float(details['conf'][seq]) > 30.0:
            pg_readable_items += 1

            # Draws a green rectangle around readable text items having a confidence score > 30
            if highlight_readable_text:
                (x, y, w, h) = (
                  details['left'][seq], details['top'][seq]
                , details['width'][seq], details['height'][seq])
                boxed_img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Searches for the string
            if search_str:
                results = re.findall(search_str, details['text'][seq], re.IGNORECASE)
                for result in results:
                    pg_matches += 1

                    if action:
                        # Draw a red rectangle around the searchable text
                        (x, y, w, h) = (
                         details['left'][seq], details['top'][seq]
                        ,details['width'][seq], details['height'][seq])
                        # Details of the rectangle
                        #Coordinates representing the top left corner of the rectangle
                        start_point = (x, y)
                        #Coordinates representing the botton right corner of the rectangle
                        end_point = (x + w, y + h)

                        # Color in BGR -- Blue, Green, Red
                        if action == "Highlight":
                            color = (0, 255, 255)  # Yellow
                        elif action == "Redact":
                            color = (0, 0, 0)  # Black

                        # Thickness in px (-1 will fill the entire shape)
                        thickness = -1
                        boxed_img = cv2.rectangle(img, start_point, end_point, color, thickness)

    if pg_readable_items > 0 \
          and highlight_readable_text \
              and not (pg_matches > 0 and action in ("Highlight", "Redact")):
        highlighted_img = boxed_img.copy()

    # Highlight the found matches of the search string
    if pg_matches > 0 and action == "Highlight":
        cv2.addWeighted(boxed_img, 0.4, highlighted_img, 1 - 0.4, 0, highlighted_img)
    # Redact found matches of the search string
    elif pg_matches > 0 and action == "Redact":
        highlighted_img = boxed_img.copy()
        # cv2.addWeighted(boxed_img, 1, highlighted_img, 0, 0, highlighted_img)

    # Displays window showing readable text fields or the highlighted or redacted data
    if show_comparison and (highlight_readable_text or action):
        conc_img = cv2.hconcat([original_img, highlighted_img])
        cv2.imwrite(filename=comparison_file,img=conc_img)


    # Generates the text content of the image
    output_data = None
    if generate_output and details:
        output_data = generate_image_text(details)

    return highlighted_img, pg_readable_items, pg_matches, pg_confidence, output_data


def scan_file(input_file : str
             ,output_path: str
             ,search_str: str
             ,pages:str = None
             ,highlight_readable_text: bool = False
             ,action: str = 'Highlight'
             ,show_comparison: bool = False
             ,generate_output: bool = False
              ):
    """
    Open the PDF File.
    Open a memory buffer for storing the generated PDF file.
    Create a DataFrame for storing pages statistics
    Iterate throughout the selected pages of the PDF file
    Grab a screen-shot for each page selected.
    Convert the screen-shot pix to a numpy array
    Scan and OCR the grabbed screen-shot.
    Collect the statistics relevant to the screen-shot / page.
    Save the content of the screen-shot/page to a CSV file.
    Add the updated screen-shot (Highlighted, Redacted) to the output file.
    Save the output PDF file if required.
    Print a summary of the process to the console.
    """
    # Opens the selected PDF file
    pdfIn = fitz.open(input_file)

    # Open a memory buffer for storing the output PDF file.
    pdfOut = fitz.open()

    # Create an empty DataFrame for storing the statistics of the pages
    dfResult = pd.DataFrame(columns=['page', 'page_readable_items'
                                      , 'page_matches', 'page_total_confidence'])

    # Creates an empty DataFrame for storing the content of the file
    if generate_output:
        pdfContent = pd.DataFrame(columns=['page', 'line_id', 'line'])

    # Iterate throughout the pages of the PDF file
    for pg in range(pdfIn.pageCount):
        pageID = pg + 1

        #Omit the unselected pages
        if pages:
           if pageID not in pages:
              continue

        # Select a spepcific page
        page = pdfIn[pg]
        # Rotation angle
        rotate = int(0)

        # Page is converted into a whole picture 1056*816 and for each picture a screenshot is taken.
        # zoom = 1.33333333 --> Image size = 1056*816
        # zoom = 2 --> 2 * Default Resolution (text is clear, image text is hard to read)
        # zoom = 4 --> 4 * Default Resolution (text is clear, image text is barely readable)
        # zoom = 8 --> 8 * Default Resolution (text is clear, image text is readable)

        zoom_x = 2
        zoom_y = 2
        # The zoom factor to make the text clearer
        # Pre-rotate if rotating the page is needed.
        mat = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)

        # Grab a screen-shot of the PDF page
        # Colorspace -> represents the color space of the pixmap (csRGB, csGRAY, csCMYK)
        # alpha -> Transparancy indicator
        pix = page.getPixmap(matrix=mat, alpha=False, colorspace="csGRAY")

        # convert the screen-shot pix to numpy array
        img = pixmap2numpy(pix)

        # Generate a file for storing the comparative image
        comparison_file = os.path.join(output_path
                             , (os.path.splitext(os.path.basename(input_file))[0]) + '_Page'
                                       + str(pageID) + '.png')

        #Scan the page screen-shot
        img_np_array, pg_readable_items, pg_matches, pg_total_confidence, pg_output_data \
            = scan_image(img=img
                       , comparison_file = comparison_file
                       , search_str=search_str
                       , highlight_readable_text=highlight_readable_text
                       , action=action
                       , show_comparison=show_comparison
                       , generate_output=generate_output
                       )

        # Collects the statistics of the page
        dfResult = dfResult.append(
            {'page': (pg + 1), 'page_readable_items': pg_readable_items, 'page_matches': pg_matches,
             'page_total_confidence': pg_total_confidence}, ignore_index=True)

        if generate_output:
            pdfContent = save_page_content(pdfContent=pdfContent, page_id=(pg + 1)
                                             , page_data=pg_output_data)

        # Convert the numpy array to image object with mode = RGB
        upd_img = Image.fromarray(img_np_array[..., ::-1])
        # Convert the image to byte array
        upd_array = convert_img2bytearray(upd_img)

        # Get Page Size
        pdfOut_page = pdfOut.newPage(pno=-1, width=page.rect.width, height=page.rect.height)
        pdfOut_page.insertImage(page.rect, stream=upd_array)

    content_file = None
    #Save the ocr content file to a CSV file
    if generate_output:
        content_file = save_doc_content(pdfContent=pdfContent, input_file=input_file
                                            ,output_path=output_path )
    # Set a name for the output PDF file
    output_file = os.path.join(output_path,
                               os.path.splitext(os.path.basename(args['input_file']))[0] + "_ocr.pdf")

    # Summarize the process
    summary = {
        "File": input_file
        , "Total pages": pdfIn.pageCount
        , "Processed pages": dfResult['page'].count()
        , "Total readable words": dfResult['page_readable_items'].sum()
        , "Total matches": dfResult['page_matches'].sum()
        , "Confidence score": dfResult['page_total_confidence'].mean()
        , "Output file": output_file
        , "Content file": content_file
    }

    # Printing Summary
    print("## Summary ########################################################")
    print("\n".join("{}:{}".format(i, j) for i, j in summary.items()))
    print("\nPages Statistics:")
    print(dfResult, sep='\n')
    print("###################################################################")

    #Save and free up resources
    pdfIn.close()
    if output_file:
        pdfOut.save(output_file)
    pdfOut.close()


def is_valid_file_path(path):
    """
    Validate the path inputted and validate that it is a file path
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
                        , '--input_file'
                        , dest='input_file'
                        , type=is_valid_file_path
                        , required=True
                        , help="Enter the path of the file")

    parser.add_argument('-a'
                        , '--action'
                        , dest='action'
                        , choices=['Highlight', 'Redact']
                        , type=str
                        , help="Choose to highlight or to redact")

    parser.add_argument('-s'
                        , '--search_str'
                        , dest='search_str'
                        , type=str
                        , help="Enter a valid string to search for")

    parser.add_argument('-p'
                        , '--pages'
                        , dest='pages'
                        , type=str
                        , help="Enter the pages to consider e.g.: (0,1)")

    parser.add_argument('-g'
                        , '--generate_output'
                        , dest='generate_output'
                        , default=False
                        , type=lambda x: (str(x).lower() in ['true', '1', 'yes'])
                        , help="Generate content in a CSV file")

    parser.add_argument('-o'
                       , '--output_path'
                       , dest='output_path'
                       , type=str
                       , required=True
                       , help="Enter a valid output path")

    parser.add_argument('-t'
                            , '--highlight_readable_text'
                            , dest='highlight_readable_text'
                            , default=False
                            , type=lambda x: (str(x).lower() in ['true', '1', 'yes'])
                            , help="Highlight readable text in the generated image")

    parser.add_argument('-c'
                            , '--show_comparison'
                            , dest='show_comparison'
                            , default=False
                            , type=lambda x: (str(x).lower() in ['true', '1', 'yes'])
                            , help="Show comparison between captured image and the generated image")


    # To Parse The Command Line Arguments
    args = vars(parser.parse_args())

    # To Display The Command Line Arguments
    print("## Command Arguments #################################################")
    print("\n".join("{}:{}".format(i, j) for i, j in args.items()))
    print("######################################################################")

    return args


if __name__ == '__main__':
    # Parsing command line arguments entered by user
    args = parse_args()
    pages_list = build_range(args['pages']) if args['pages'] else None
    scan_file(
                 input_file=args['input_file']
                , output_path=args['output_path']
                , search_str=args['search_str'] if 'search_str' in (args.keys()) else None
                , pages=pages_list
                , highlight_readable_text=args['highlight_readable_text']
                , action=args['action']
                , show_comparison=args['show_comparison']
                , generate_output=args['generate_output']
            )
