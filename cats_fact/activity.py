import requests
from colorama import Fore, Back, Style


def to_do() -> str:
    response = requests.get("https://www.boredapi.com/api/activity")
    obj: dict = response.json()

    return obj["activity"]


if __name__ == "__main__":
    activity = to_do()
    print(Back.BLACK, Fore.LIGHTYELLOW_EX, activity, Style.RESET_ALL, sep="")
