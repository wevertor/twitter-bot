import tweepy
import requests
import json
import utils
from config import keys


def init_bot(keys):

    auth = tweepy.OAuthHandler(keys["consumer_key"], keys["consumer_secret"])
    auth.set_access_token(keys["access_token"], keys["access_token_secret"])

    return tweepy.API(auth)


class StatusListener(tweepy.StreamListener):
	def __init__(self, client, user):
		super().__init__()
		self.client = client
		self.user = user

	def on_status(self, status):
		statusID = status.id_str

		print(f"Processing status {statusID}.")

		media = get_status_media(status)

		if media is not None and media[0]["type"] == "photo":
			urlArray = get_media_url(media)
			# download all images

			print("Downloading images...")
			for i, url in enumerate(urlArray):
				utils.download_image(f"image{i}.jpg", url)
			print("Completed!")

			print("Coloring images...")
			for i, url in enumerate(urlArray):
				colorize_image(f"image{i}.jpg")
			print("Completed!")

			print("Uploading images...")
			newMedias = []
			for i, url in enumerate(urlArray):

				newMedia = self.client.media_upload(f"image{i}.jpg")
				
				newMedias.append(newMedia.media_id)
			print(self.user)

			res = self.client.update_status(
				"@" + (self.user.screen_name),
				in_reply_to_status_id=self.user.id,
				media_ids=newMedias, auto_populate_reply_data=True)
			print("Completed!")
		return

	def on_error(self, status):
		print(status)


def get_status_media(status):
    if ("media" in status.entities):
        return status.entities["media"]
    # print("Status has no media.")
    # return None


def get_media_url(mediaArray):
    return [media["media_url_https"] for media in mediaArray]


def get_user_id(client, username):
    return client.get_user(username)._json["id_str"]


def colorize_image(filename):
    api_url = "https://api.deepai.org/api/colorizer"
    files = {"image": open(filename, 'rb')}
    headers = {"api-key": keys["deepai_key"]}

    res = requests.post(api_url, files=files, headers=headers)
    res_data = res.json()
    utils.download_image(filename, res_data["output_url"])
