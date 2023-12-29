import flet as ft
from fletify import FletifyHTML


html_content = """
        <div>
            <h1>Title</h1>
            <p style="background-color: red; color:black; font-size:30">This is a paragraph.</p>
            <p style="text-decoration: underline; background-color: blue">This is underlined text.</p>
            <p style="text-decoration: overline;">This has an overline.</p>
            <mark style="background-color:green;">milk vggvgvg</mark>
            <b>This is a bold text</b>
            <strong>This is a STRONG text</strong>
            <p>This is free text.<b>This is a bold text </b>this is la suite.<span style="color:pink;">this text is in span1</span><span style="color:green;">this text is in span2</span>autres choses</p>

            <code>
              function example() {
                console.log("This is a code block");
              }
            </code>

            <table border="1">
            <tr>
                <th>Header 1</th>
                <th>Header 2</th>
                <th>Header 3</th>
            </tr>
            <tr>
                <td>Row 1, Cell 1</td>
                <td>Row 1, Cell 2</td>
                <td>Row 1, Cell 3</td>
            </tr>
            <tr>
                <td>Row 2, Cell 1</td>
                <td>Row 2, Cell 2</td>
                <td>Row 2, Cell 3</td>
            </tr>
        </table>
            
            <ul>
                <li>Item 1</li>
                <li>Item 2</li>
            </ul>
            <a href="https://example.com">Visit Example</a>
            <img style="width: 200; height: 200; background-color:yellow; border-radius: 5; border: 3 solid #336699; margin:40" src="https://picsum.photos/200/200?10" alt="Example Image">
            <div style="display: flex; justify-content: space-between;">
                <div style="width: 100; height: 100; background-color: blue; margin: 0;"></div>
                <div style="width: 100; height: 100; background-color: lightblue; margin: 5;"></div>
                <div style="width: 100; height: 100; background-color: lightblue; margin: 5;"></div>
        </div>
        </div>
    """
flet_code = FletifyHTML(html_content)


def main(page: ft.Page):
    page.scroll = "always"

    page.add(flet_code.get_flet())
    page.update()


ft.app(target=main)
