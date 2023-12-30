# FletifyHTML

FletifyHTML is a Python package for converting HTML content into Flet code. It allows you to embed HTML code in your Flet app

## Installation

```bash
pip install fletify
```
## Usage
```python
from fletify import FletifyHTML

# Example HTML content
html_content = "<p>This is a <b>paragraph</b> with <a href='#'>a link</a></p>"

# Create a FletifyHTML instance
fletify = FletifyHTML(html_content)

# Get the Flet code
flet_code = fletify.get_flet()

# Display or use the Flet code as needed
def main(page: ft.Page):

    page.add(flet_code)
    page.update()

ft.app(target=main)
```
# OutPut:
(test1.png)

## Features

For now, **Fletify** support the following HTML tags:
*
        - "img"
        - "ul"
        - "ol"
        - "li"
        - "a"
        - "b"
        -  "strong"
        - "i"
        -  "em"
        - "u"
        - "mark"
        - "span"
        -  "div"
        - "p"
        - "code"
        - "h1"
        - "h2"
        - "h3"
        - "h4"
        - "h5"
        - "h6"
        - "table"
        - "tr"
        - "th"
        - "td"
*
## Contributing
If you'd like to contribute to FletifyHTML, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
