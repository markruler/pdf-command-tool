from pypdf import PdfReader, PdfWriter


def recursive_copy(parent_node, outlines, reader, writer):
    for i in range(len(outlines)):
        outline_node = outlines[i]
        if not isinstance(outline_node, list):
            print(outline_node)
            writer.add_outline_item(
                title=outline_node["/Title"],
                page_number=reader.get_destination_page_number(outline_node) + 1,
                # parent=parent_node,
            )
        else:
            recursive_copy(outlines[i - 1], outline_node, reader, writer)


def copy(reader, writer):
    outlines: list = reader.outline
    recursive_copy(None, outlines, reader, writer)


reader = PdfReader("old.pdf")
writer = PdfWriter()

copy(reader, writer)

for page in reader.pages:
    writer.add_page(page)

writer.write("new.pdf")


