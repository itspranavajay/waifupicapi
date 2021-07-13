from requests.exceptions import HTTPError
import requests

url = "https://api.waifu.pics"

def sfw(category):
    pic = f"{base}/sfw/{category}"
    response = requests.get(pic)
    response.raise_for_status()
    jsonResponse = response.json()
    img = (jsonResponse["url"])
    return img

def nsfw(category):
    pic = f"{base}/nsfw/{category}"
    response = requests.get(pic)
    response.raise_for_status()
    jsonResponse = response.json()
    img = (jsonResponse["url"])
    return img
