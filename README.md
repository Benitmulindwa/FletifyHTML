# FletifyHTML
"FletifyHTML" is a versatile Python tool designed to seamlessly convert HTML content into Flet code. This project empowers developers to streamline the creation of Flet-based user interfaces by automating the transformation process from standard HTML elements to their Flet equivalents. Simplify your UI development workflow with "Fletify" and effortlessly bridge the gap between HTML and Flet.

 FletifyHTML

FletifyHTML is a Python package for converting HTML content into Flet controls. It leverages BeautifulSoup for HTML parsing and Flet for creating rich text-based UI components.

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
## Features
Convert HTML content to Flet controls
Support for various HTML tags and attributes
## Contributing
If you'd like to contribute to FletifyHTML, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
