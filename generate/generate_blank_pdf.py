from pypdf import PdfWriter, PageObject
from pypdf.constants import PageAttributes, Core
from pypdf.generic import NameObject


def main(total_pages: int):
    pdf_writer: PdfWriter = PdfWriter()

    page_object: PageObject = PageObject()
    page_object[NameObject(PageAttributes.TYPE)] = NameObject(Core.PAGE)

    for _ in range(total_pages):
        pdf_writer.add_page(page=page_object)

    pdf_writer.write("../example.pdf")


if __name__ == "__main__":
    """
    https://github.com/py-pdf/pypdf/blob/4fa4cedba42f70d6c0a3aba04cffe5e10f9dc7d5/tests/test_page.py#L1004
    """
    import argparse

    parser = argparse.ArgumentParser(description="""
    빈 페이지의 PDF를 생성한다.
    
    Usage: python generate_blank_pdf.py -p 3
    """, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-p', '--total-pages',
                        metavar='<int>',
                        required=False,
                        default=1,
                        type=int,
                        help='생성할 PDF의 페이지 수')

    args = parser.parse_args()
    main(total_pages=args.total_pages)
