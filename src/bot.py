# import tweepy
import requests
import json
from config import keys


def init_bot(keys):

    auth = tweepy.OAuthHandler(keys["consumer_key"], keys["consumer_secret"])
    auth.set_access_token(keys["access_token"], keys["access_token_secret"])

    return tweepy.API(auth)


def colorize_image(url):
    api_url = "https://api.deepai.org/api/colorizer"
    data = {"image": url}
    headers = {"Api-Key": keys["deepai_key"]}

    res = requests.post(api_url, data, headers)
    return res.json()
