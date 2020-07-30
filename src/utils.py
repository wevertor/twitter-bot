import requests


def download_image(url):
    res = requests.get(url, stream=True)
    if res.status_code == 200:
        with open("image.png", 'wb') as file:
            for chunk in res.iter_content(1024):
                file.write(chunk)
