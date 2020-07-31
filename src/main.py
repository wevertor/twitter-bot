import tweepy
import requests
import bot
import json
from config import keys

client = bot.init_bot(keys)
user = client.get_user("@trindamaster")

listener = bot.StatusListener(client, user)
stream = tweepy.Stream(auth=client.auth, listener=listener)

stream.filter(follow=[user.id_str])