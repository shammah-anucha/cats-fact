import requests
from colorama import Fore, Back, Style


def to_do() -> str:
    response = requests.get("https://www.boredapi.com/api/activity")
    obj: dict = response.json()

    return obj["activity"]


def activity(response):
    obj = response.json()
    # pretty print Json
    json_formatted_str = json.dumps(obj, indent=4)
    colorful_json = highlight(
        json_formatted_str, lexer=JsonLexer(), formatter=Terminal256Formatter()
    )
    print(colorful_json)


if __name__ == "__main__":
    activity = to_do()
    print(Back.BLACK, Fore.LIGHTYELLOW_EX, activity, Style.RESET_ALL, sep="")
