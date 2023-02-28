from pypdf import PdfReader, PdfWriter


def main(
        text_path: str,
        pdf_path: str,
):
    # Outline(구 bookmark)을 저장할 PDF
    pdf_reader: PdfReader = PdfReader(pdf_path)
    pdf_writer: PdfWriter = PdfWriter()

    # Page를 추출할 PDF
    for page in pdf_reader.pages:
        pdf_writer.add_page(page)

    # Text 파일을 읽어서 PDF Outline으로 추가한다.
    default_page = 1
    with open(text_path, "r", encoding="utf-8") as f:
        txt = f.readlines()
        for line in txt:
            strip_line = line.strip()
            print(strip_line)
            pdf_writer.add_outline_item(title=strip_line, page_number=default_page)

    pdf_writer.write(f"{pdf_path}.update_outline.pdf")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="""
    파일에서 텍스트를 읽어서 PDF Outline으로 저장한다.
    """)
    parser.add_argument('-f', '--text-file',
                        metavar='<path>',
                        required=False,
                        default=r"C:\Users\user\Documents\text_from_pdf.txt",
                        type=str,
                        help='Outline(old Bookmark)을 추출할 Text 파일')
    parser.add_argument('-p', '--pdf',
                        metavar='<path>',
                        required=False,
                        default=r"C:\Users\user\Documents\page.pdf",
                        type=str,
                        help='Outline을 저장할 PDF')

    args = parser.parse_args()
    main(text_path=args.text_file, pdf_path=args.pdf)
