import requests
import json
from pygments import highlight
from pygments.formatters.terminal256 import Terminal256Formatter
from pygments.lexers.web import JsonLexer


response = requests.get("https://www.boredapi.com/api/activity")


def activity(response):
    obj = response.json()
    # pretty print Json
    json_formatted_str = json.dumps(obj, indent=4)
    colorful_json = highlight(
                              json_formatted_str,
                              lexer=JsonLexer(),
                              formatter=Terminal256Formatter()
                              )
    print(colorful_json)
 

if __name__ == "__main__.py":
    pass
else:
    activity(response)
    