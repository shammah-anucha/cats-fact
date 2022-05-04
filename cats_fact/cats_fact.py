import requests
# import json
# from pygments import highlight
# from pygments.formatters.terminal256 import Terminal256Formatter
# from pygments.lexers.web import JsonLexer

url = "https://catfact.ninja/fact"


# request mock: to mock an access to the url
# testing the return of the function which is the fact
def cat_facts(url):
    response = requests.get(url)
    obj = response.json()
    print(obj['fact'])

    # # pretty print Json
    # json_formatted_str = json.dumps(obj, indent=4)
    # colorful_json = highlight(
    #                           json_formatted_str,
    #                           lexer=JsonLexer(),
    #                           formatter=Terminal256Formatter()
    #                           )
    # status = response.status_code
    # header = response.headers["Content-Type"]

    # print(colorful_json)

    # return colorful_json, status, header


if __name__ == "__main__":
    cat_facts(url)
