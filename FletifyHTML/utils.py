import os


class RenderHTML:
    def __init__(self, file, encoding="utf-8"):
        self.file = file
        if not os.path.exists(self.file):
            raise FileNotFoundError(f"No such HTML file: {self.file}")
        with open(self.file, encoding=encoding) as file:
            self.html_str = file.read()

    def __repr__():
        ...

    def display(self):
        return self.html_str

    __str__ = display
