from bs4 import BeautifulSoup
from fletify.parser import parse_html_to_flet


def convert_html_to_flet(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    flet_code = parse_html_to_flet(soup)
    return flet_code
