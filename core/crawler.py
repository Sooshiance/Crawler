import requests
from requests import Response


def fetch_data(link:str)->Response:

    data = requests.get(link)

    return data
