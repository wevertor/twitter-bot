import tweepy
import requests
import bot
import json
from config import keys

client = bot.init_client(keys)
user = client.get_user("@trindamaster")

listener = bot.StatusListener(client, user)
stream = tweepy.Stream(auth=client.auth, listener=listener)

print("Listening to @{user.author.name}.")
stream.filter(follow=[user.id_str])