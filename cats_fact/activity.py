import requests


def activity(response):
    return response.json()


response = requests.get("https://www.boredapi.com/api/activity")
print(activity(response))
