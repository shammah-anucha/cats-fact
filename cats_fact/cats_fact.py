import sys
import requests
from colorama import Fore, Back, Style


def cat_facts() -> str:
    response = requests.get("https://catfact.ninja/fact")
    obj: dict = response.json()

    return obj["fact"]


if __name__ == "__main__":
    fact: str = cat_facts()
    print(Fore.CYAN)
    print(Back.WHITE, end="")
    sys.stdout.write(fact)
    print(Style.RESET_ALL)
