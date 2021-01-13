import requests

def get_page(url):
    response = requests.get(url)
    print(f"Got status code: {response.status_code}")
    print(f"Page html is {len(response.text)} characters long")


def demo():
    get_page("https://google.com")
