from FletifyHTML.converter import convert_html_to_flet
import flet as ft


html_content = """
        <div>
            <h1>Title</h1>
            <p>This is a paragraph.</p>
            <ol>
                <li>Item 1</li>
                <li>Item 2</li>
            </ol>
            <a href="https://example.com">Visit Example</a>
            <img src="https://picsum.photos/200/200?10" alt="Example Image">
        </div>
    """
flet_code = convert_html_to_flet(html_content)


def main(page: ft.Page):
    # Example usage:

    page.add(flet_code)
    page.update()


ft.app(target=main)
