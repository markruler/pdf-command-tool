import io

# PyMuPDF: A Python binding for the MuPDF 1.14.0 library
import fitz as mupdf
# Python Imaging Library (PIL)
from PIL import Image
# A Python wrapper for Google Tesseract
# https://github.com/madmaze/pytesseract
from pytesseract import pytesseract, image_to_string


# iterate over PDF pages
def read_text(
        page_index: int,
        pdf_file: mupdf.fitz.Document,
        lang: str,
):
    """
    https://stackoverflow.com/questions/20327681/extract-images-from-pdf-using-python-pypdf2
    """
    # get the page itself
    page = pdf_file[page_index - 1]
    image_li = page.get_images()
    # printing number of images found in this page
    # page index starts from 0 hence adding 1 to its content
    if image_li:
        print(f"[+] Found a total of {len(image_li)} images in page {page_index + 1}")
    else:
        print(f"[!] No images found on page {page_index}")
    for image_index, img in enumerate(page.get_images(), start=1):
        # get the XREF of the image
        xref = img[0]
        # extract the image bytes
        base_image = pdf_file.extract_image(xref)
        image_bytes = base_image["image"]

        # get the image extension
        # image_ext = base_image["ext"]

        # load it to PIL
        image = Image.open(io.BytesIO(image_bytes))
        # save it to local disk
        # save_path = f"image{page_index + 1}_{image_index}.{image_ext}"
        # image.save(open(save_path, "wb"))

        # image to korean text
        # https://github.com/tesseract-ocr/tessdata/blob/main/kor.traineddata
        # C:\Program Files\Tesseract-OCR\tessdata\kor.traineddata
        txt: str = image_to_string(image, lang=lang)

        txt = (
            txt
            .strip()
            .replace("\n", "\t")
            .replace(" ", "")
        )
        print(txt)


def main(
        command_path: str,
        pdf_path: str,
        page_index: int,
        lang: str,
):
    # Download Tesseract
    # 테서랙트(Tesseract): Open Source OCR Engine
    # https://github.com/UB-Mannheim/tesseract/wiki
    pytesseract.tesseract_cmd = command_path

    # https://stackoverflow.com/questions/20327681/extract-images-from-pdf-using-python-pypdf2
    # file path you want to extract images from
    pdf_file: mupdf.fitz.Document = mupdf.open(pdf_path)

    read_text(page_index, pdf_file, lang)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="""
    PDF 이미지에서 텍스트를 추출한다.
    """)
    parser.add_argument(
        '-c', '--command-path',
        metavar='<path>',
        required=False,
        default=r"C:\Program Files\Tesseract-OCR\tesseract.exe",
        type=str,
        help='tesseract.exe 경로'
    )
    parser.add_argument(
        '-p', '--pdf',
        metavar='<path>',
        required=False,
        default=r"C:\Users\user\Documents\test.pdf",
        type=str,
        help=r'Text를 추출할 PDF. Windows의 경우 반드시 큰따옴표로 감싸야 한다. "C:\Users\user\Documents\test.pdf"'
    )
    parser.add_argument(
        '-i', '--index',
        metavar='<path>',
        required=False,
        default=0,
        type=int,
        help='Page Index'
    )
    parser.add_argument(
        '-l', '--lang',
        metavar='<lang>',
        required=False,
        default='kor',
        type=str,
        help='Language(eng, kor, etc.): "C:\Program Files\Tesseract-OCR\\tessdata\kor.traineddata"'
    )

    args = parser.parse_args()
    main(
        command_path=args.command_path,
        pdf_path=args.pdf,
        page_index=args.index,
        lang=args.lang,
    )
