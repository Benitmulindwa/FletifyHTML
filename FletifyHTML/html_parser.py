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

    TEXT_STYLE_DECORATION = ["underline", "line-through", "overline"]

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
        # if element.get(HTML.ATTRIBUTES[0]):
        #     style_props = parse_inline_styles(element.get(HTML.ATTRIBUTES[0]))[
        #         "decoration"
        #     ]
        #     style = ft.TextStyle(
        #         decoration=getattr(
        #             ft.TextDecoration,
        #             "LINE_THROUGH"
        #             if style_props == "line-through"
        #             else style_props.upper(),
        #         )
        #     )
        # else:
        #     style = None
        # Map <p> to ft.Text within ft.Container
        paragraph = ft.Container(
            content=ft.Text(
                value=element.text,
                style=ft.TextStyle(
                    bgcolor="red", decoration=ft.TextDecoration.UNDERLINE
                ),
            )
        )
        return paragraph
    elif element.name == "a":
        # Map <a> to ft.Text with a URL
        link = ft.Text(
            spans=[
                ft.TextSpan(
                    element.text,
                    url=element.get(HTML.ATTRIBUTES[1]),
                    style=ft.TextStyle(italic=True, color="blue"),
                )
            ]
        )
        return link
    elif element.name == "img":
        # Map <img> to ft.Image with a source URL
        image = ft.Image(src=element.get(HTML.ATTRIBUTES[2]))
        return image

    # HTML lists

    elif element.name == "ul" or element.name == "ol":
        # Map <ul> and <ol> to ft.Column or ft.Row with ft.Text elements
        list_container = ft.Column(spacing=0)

        for i, li in enumerate(element.find_all("li")):
            _leading = (
                ft.Text("•", size=20)
                if element.name == "ul"
                else ft.Text(f"{i+1}", size=16)
            )
            list_item = ft.ListTile(title=ft.Text(li.text), leading=_leading)

            list_container.controls.append(list_item)
        return list_container

    else:
        # Default to ft.Container for unrecognized elements
        container = ft.Container()
        for child in element.children:
            if child.name:
                child_flet = parse_html_to_flet(child)
                container.content = child_flet
        return container


# ____________________________________________________________________
html_to_flet_style_mapping = {
    "color": "color",
    "background-color": "background_color",
    "font-family": "font_family",
    "font-size": "font_size",
    "text-align": "text_align",
    "text-decoration": "decoration",
}


def parse_inline_styles(style_string):
    # Parse inline styles and convert to Flet properties
    style_properties = {}
    for style_declaration in style_string.split(";"):
        if ":" in style_declaration:
            property_name, property_value = style_declaration.split(":")
            property_name = property_name.strip()
            property_value = property_value.strip()

            # Convert property_name to Flet style name if needed
            property_name = html_to_flet_style_mapping[property_name]
            style_properties[property_name] = property_value

    return style_properties
