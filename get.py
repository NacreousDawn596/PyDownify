from bs4 import *
from youtubesearchpython import VideosSearch
import requests
import get
#import youtube_dl
import yt_dlp as youtube_dl
import endpoints

def name(link):
    html = requests.get(link.split('?')[0]).text
    html = BeautifulSoup(html, 'html.parser')
    return (html.title.string.split(" | ")[0] if html.title else link.split("/")[-1])

def url(link):
    idk = VideosSearch(get.name(link), limit = 1).result()['result'][0]
    return idk["link"], idk["title"]

def tracks(link):
    return [i for i in endpoints.get(link) if "/track/" in i]

def audio(link, name=""):
    print(f"downloading {name}...")
    ydl_opts = {
        'writethumbnail': True,
        'format': 'bestaudio/best',
        'writesubtitles': True,
        'subtitleslangs': 'en',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }, {'key': 'EmbedThumbnail',
            'already_have_thumbnail': False,
        }, {'key': 'FFmpegMetadata',
            'add_metadata': True
        #}, {'key': 'FFmpegSubtitle',
        #    'format': 'lrc',
        #   'already_have_subtitle': False
        }]
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
