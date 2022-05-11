import requests

# doesn't work with poetry. Why?
from colorama import Fore, Back, Style


def cat_facts() -> str:
    response = requests.get("https://catfact.ninja/fact")
    obj: dict = response.json()

    return obj["fact"]


if __name__ == "__main__":
    fact = cat_facts()
    print(Fore.CYAN, Back.WHITE, fact, Style.RESET_ALL, sep="")
