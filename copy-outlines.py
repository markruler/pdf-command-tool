from pprint import pprint

from pypdf import PdfReader, PdfWriter


def recursive_copy(parent_node, outlines, reader, writer):
    for i in range(len(outlines)):
        outline_node = outlines[i]
        if isinstance(outline_node, list):
            recursive_copy(outlines[i - 1], outline_node, reader, writer)
        else:
            # print(type(outline_node))
            # print(outline_node)

            # if outline_node["/Count"] != None:

            writer.add_outline_item(
                title=outline_node["/Title"],
                page_number=reader.get_destination_page_number(outline_node),
            )


def copy(reader, writer):
    outlines: list = reader.outline
    pprint(outlines)
    recursive_copy(None, outlines, reader, writer)


reader = PdfReader("old.pdf")
writer = PdfWriter()

copy(reader, writer)

for page in reader.pages:
    # writer.add_outline()
    writer.add_page(page)

writer.write("new.pdf")

# new_reader = PdfReader("new.pdf")
# pprint(new_reader.get_bookmarks())
