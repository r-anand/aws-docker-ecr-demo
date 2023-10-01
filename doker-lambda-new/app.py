import requests


def handler(event, context):
    result = requests.get("https://randomuser.me/api/")
    return {
        "data": result.json()
    }
