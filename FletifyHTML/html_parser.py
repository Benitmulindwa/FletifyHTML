import flet as ft


class HTML:
    # ----------------------------------------------------------------------------------------------
    """
    supported HTML tags and attributes
    """

    html_tags = [
        "br",
        "ul",
        "ol",
        "li",
        "img",
        "a",
        "b",
        "strong",
        "i",
        "em",
        "u",
        "mark",
        "span",
        "div",
        "p",
        "pre",
        "code",
        "h1",
        "h2",
        "h3",
        "h4",
        "h5",
        "h6",
        "table",
        "tr",
        "th",
        "td",
    ]

    ATTRIBUTES = ["style", "href", "src", "width", "height", "type"]

    style_attributes = [
        "color",
        "background-color",
        "font-family",
        "font-size",
        "font-weight",
        "font-style",
        "text-align",
        "text-decoration",
        "padding",
        "margin",
        "border",
        "border-radius",
        "width",
        "height",
        "display",
        "flex",
        "justify-content",
        "align-items",
        "box-shadow",
        "line-height",
        "letter-spacing",
        "word-spacing",
        "overflow",
        "position",
        "top",
        "right",
        "bottom",
        "left",
    ]

    STYLE_TEXT_DECORATION = ["underline", "line-through"]

    HEADINGS_TEXT_SIZE = {
        "h1": 32,
        "h2": 24,
        "h3": 18,
        "h4": 16,
        "h5": 13,
        "h6": 10,
    }


def parse_html_to_flet(element):
    if element.name == "div":
        # Map <div> to ft.Column
        container = ft.Column([])
        for child in element.children:
            if child.name:
                # Recursively parse child elements
                child_flet = parse_html_to_flet(child)
                container.controls.append(child_flet)
        return container
    # Heading tags
    elif element.name in HTML.HEADINGS_TEXT_SIZE.keys():
        heading_text = ft.Text(
            value=element.text, size=HTML.HEADINGS_TEXT_SIZE[element.name]
        )
        return heading_text
    elif element.name == "p":
        # Map <p> to ft.Text within ft.Container
        paragraph = ft.Container(content=ft.Text(value=element.text))
        return paragraph
    elif element.name == "a":
        # Map <a> to ft.Text with a URL
        link = ft.Text(
            spans=[
                ft.TextSpan(
                    element.text,
                    url=element.get("href"),
                    style=ft.TextStyle(italic=True, color="blue"),
                )
            ]
        )
        return link
    elif element.name == "img":
        # Map <img> to ft.Image with a source URL
        image = ft.Image(src=element.get("src"))
        return image

    elif element.name == "ul" or element.name == "ol":
        # Map <ul> and <ol> to ft.Column or ft.Row with ft.Text elements
        list_container = ft.Column() if element.name == "ul" else ft.Row()
        for li in element.find_all("li"):
            list_item = ft.ListTile(
                title=ft.Text(li.text), leading=ft.Text("•", size=20)
            )

            list_container.controls.append(list_item)
        return list_container
    # Add more mappings for other HTML elements
    else:
        # Default to ft.Container for unrecognized elements
        container = ft.Container()
        for child in element.children:
            if child.name:
                child_flet = parse_html_to_flet(child)
                container.content = child_flet
        return container


# ____________________________________________________________________


def parse_inline_styles(style_string):
    # Parse inline styles and convert to Flet properties
    style_properties = {}
    for style_declaration in style_string.split(";"):
        if ":" in style_declaration:
            property_name, property_value = style_declaration.split(":")
            property_name = property_name.strip()
            property_value = property_value.strip()

            # Convert property_name to Flet style name if needed
            # For simplicity, let's assume the property names are the same
            style_properties[property_name] = property_value

    return style_properties
