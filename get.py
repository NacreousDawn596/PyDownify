from bs4 import *
from youtubesearchpython import VideosSearch
import requests
import get
import youtube_dl
import endpoints

def name(link):
    html = requests.get(link.split('?')[0]).text
    html = BeautifulSoup(html, 'html.parser')
    return html.title.string.split(" | ")[0]

def url(link):
    idk = VideosSearch(get.name(link), limit = 1).result()['result'][0]
    return idk["link"], idk["title"]

def tracks(link):
    return [i for i in endpoints.get(link) if "/track/" in i]

def audio(link, name=""):
    print(f"downloading {name}...")
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
