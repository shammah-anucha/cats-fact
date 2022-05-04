from colorama import Fore, Back, Style
import requests


def cat_facts():
    response = requests.get("https://catfact.ninja/fact")
    obj = response.json()

    return obj['fact']


if __name__ == "__main__":
    fact = cat_facts()
    print(Fore.CYAN)
    print(Back.WHITE)
    print(fact)
    print(Style.RESET_ALL)
