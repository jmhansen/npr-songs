import requests
from bs4 import BeautifulSoup


def get_markup(url):
    response = requests.get(url)

    if not response.ok:
        raise ValueError(f'Invalid URL raised {response.status_code} error.')

    markup = BeautifulSoup(response.text, 'html.parser')
    return markup
