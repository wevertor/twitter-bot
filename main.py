import tweepy
from config import keys

# auth stuff
auth = tweepy.OAuthHandler(keys["consumer_key"], keys["consumer_secret"])
auth.set_access_token(keys["access_token"], keys["access_token_secret"])


client = tweepy.API(auth)

for tweet in client.home_timeline():
    print(tweet.text)
