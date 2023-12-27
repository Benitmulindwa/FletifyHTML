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

    class Style:
        COLOR = "color"
        BACKGROUND_COLOR = "background-color"
        FONT_FAMILY = "font-family"
        FONT_SIZE = "font-size"
        TEXT_ALIGN = "text-align"
        TEXT_DECORATION = "text-decoration"

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
        # Map <div> to ft.Container
        container = ft.Column([ft.Container()])
        for child in element.children:
            if child.name:
                # Recursively parse child elements
                child_flet = parse_html_to_flet(child)
                container.controls.append(child_flet)
        return container

    elif element.name == "span":
        # Map <span> to ft.Text
        text = ft.Text(value=element.text)
        return text
    elif element.name == "p":
        # Map <p> to ft.Text within ft.Container
        paragraph = ft.Container(content=ft.Text(value=element.text))
        return paragraph
    elif element.name == "a":
        # Map <a> to ft.Text with a URL
        link = ft.Text(spans=[ft.TextSpan(element.text, url=element.get("href"))])
        return link
    elif element.name == "img":
        # Map <img> to ft.Image with a source URL
        image = ft.Image(src=element.get("src"))
        return image
    elif element.name == "ul" or element.name == "ol":
        # Map <ul> and <ol> to ft.Column or ft.Row with ft.Text elements
        list_container = ft.Column() if element.name == "ul" else ft.Row()
        for li in element.find_all("li"):
            list_item = ft.Text(value=li.text)
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
