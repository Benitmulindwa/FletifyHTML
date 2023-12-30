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
![test1](test1.png)

## Features

For now, **Fletify** support the following HTML tags:

`img`, `ul`, `ol`, `li`, `a`, `b`, `strong`, `i`, `em`, `u`, `mark`, `span`, `div`, `p`, `code`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `table`, `tr`, `th`, `td`
Fletify doesn't support CSS style however, it supports inline style using the `style` attribute.
#### eg:
```css 
<img style="width: 200; height: 200; background-color:yellow; border-radius: 5; border: 3 solid #336699; margin:40" src="https://picsum.photos/200/200?10" alt="Example Image">
```
these are the supported style properties
`color`, `background-color`, `font-family`, `font-size`, `text-align`, `text-decoration`, `display`, `justify-content`, `margin`, `padding`, `border-radius`, `border`, `width`, `height`

## Contributing
If you'd like to contribute to FletifyHTML, please open an issue or submit a pull request.

🚨 Give FletifyHTML a try and tell us what you think about it.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
