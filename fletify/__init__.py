from fletify.utils import RenderHTML
from fletify.converter import convert_html_to_flet


class FletifyHTML:
    def __init__(self, html):
        self.html = html
        if isinstance(self.html, str):
            self._flet = convert_html_to_flet(self.html)
        elif isinstance(self.html, RenderHTML):
            self._flet = convert_html_to_flet(self.html.display())

    def get_flet(self):
        return self._flet
