from bs4 import *
from youtubesearchpython import VideosSearch
import os
import get
import youtube_dl

def name(link):
    html = os.popen(f"curl -s {link.split('?')[0]}").read()
    html = BeautifulSoup(html, 'html.parser')
    return html.title.string.split(" | ")[0]

def url(link):
    idk = VideosSearch(get.name(link), limit = 1).result()['result'][0]
    return idk["link"], idk["title"]

def tracks(link):
    return [idk for idk in [bruh for bruh in os.popen(f"python2 endpoints.py2 -u {link}").read().splitlines()[0:-1] if "/track/" in bruh]]

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
