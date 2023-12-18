from bs4 import BeautifulSoup
import flet as ft


def convert_html_to_flet(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    flet_code = parse_html_to_flet(soup)
    return flet_code


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


def main(page: ft.Page):
    # Example usage:
    html_content = """
        <div>
            <h1>Title</h1>
            <p>This is a paragraph.</p>
            <ul>
                <li>Item 1</li>
                <li>Item 2</li>
            </ul>
            <a href="https://example.com">Visit Example</a>
            <img src="https://example.com/image.jpg" alt="Example Image">
        </div>
    """
    flet_code = convert_html_to_flet(html_content)
    page.add(flet_code)
    page.update()


ft.app(target=main)
