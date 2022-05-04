from colorama import Fore, Back, Style
import requests


url = "https://catfact.ninja/fact"


def cat_facts(url):
    response = requests.get(url)
    obj = response.json()
    print(Fore.CYAN)
    print(Back.WHITE + obj['fact'])
    print(Style.RESET_ALL)
    return obj


if __name__ == "__main__":
    cat_facts(url)
