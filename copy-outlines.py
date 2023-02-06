from pprint import pprint
from typing import Any

from pypdf import PdfReader, PdfWriter
from pypdf.types import OutlineType


def flatten(outlines: Any) -> list[OutlineType]:
    return _flatten_outlines([], outlines)


def _flatten_outlines(
        ls: list,
        outlines: Any
) -> list[OutlineType]:
    for i in range(len(outlines)):
        outline_node = outlines[i]
        if isinstance(outline_node, list):
            _flatten_outlines(ls, outline_node)
        else:
            ls.append(outline_node)

    return ls


def main(outline: str,
         page: str,
         merge: str):
    # Outline(구 bookmark)을 추출할 PDF
    outline_reader = PdfReader(outline)
    original_outlines: list = outline_reader.outline
    pprint(original_outlines)
    flattened_outline_list: list = flatten(original_outlines)

    # Page를 추출할 PDF
    page_reader = PdfReader(page)

    # Page와 Outline을 합칠 최종 PDF
    merge_writer = PdfWriter()

    for outline in flattened_outline_list:
        merge_writer.add_outline_item(
            title=outline["/Title"],
            page_number=outline_reader.get_destination_page_number(outline),
        )

    for page in page_reader.pages:
        # writer.add_outline()
        merge_writer.add_page(page)

    merge_writer.write(merge)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="""
    PDF 파일의 Outline(Bookmark)을 추출하여 다른 PDF 파일의 Page와 합친다.
    """)
    parser.add_argument('-o', '--outline',
                        metavar='<path>',
                        required=False,
                        default=r"outline.pdf",
                        type=str,
                        help='Outline(old Bookmark)을 추출할 PDF')
    parser.add_argument('-p', '--page',
                        metavar='<path>',
                        required=False,
                        default=r"page.pdf",
                        type=str,
                        help='Page를 추출할 PDF')
    parser.add_argument('-m', '--merge',
                        metavar='<path>',
                        required=False,
                        default='merge.pdf',
                        type=str,
                        help='Merged PDF')

    args = parser.parse_args()
    main(outline=args.outline, page=args.page, merge=args.merge)
