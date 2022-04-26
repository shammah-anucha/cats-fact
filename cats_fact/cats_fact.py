import requests


def cats_fact(response):
    return response.json()


response = requests.get("https://catfact.ninja/fact")
print(cats_fact(response))