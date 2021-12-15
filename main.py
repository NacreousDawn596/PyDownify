import sys
import os
from moviepy.editor import *
import time
from pytube import YouTube
import json
from youtubesearchpython import VideosSearch
playlist = sys.argv[1]
infos = os.popen(f'curl -s {playlist}').read()
uh, mm = infos.split("Spotify.Entity = ")[1].split('M","ZW"]};')[0], 'M","ZW"]}'
result = json.loads(f'{uh}{mm}')
playlist_name = result['name']
def getUrl(name):
	videosSearch = VideosSearch(name, limit = 1)
	print(videosSearch.result()['result'][0]['title'], "...")
	return {'url': videosSearch.result()['result'][0]['link'], 'name': videosSearch.result()['result'][0]['title']}
def download(name):
	allstuff = getUrl(name)
	url, title = allstuff['url'], allstuff['name'].replace('|', '')
	YouTube(url).streams.filter(progressive=True, file_extension='mp4').first().download()
	if os.popen("uname -o") == "Android":
		os.system(f"mkdir sdcard/{playlist_name}/")
		mp4_file, mp3_file = rf'{title}.mp4', rf'/sdcard/PyDownify/{playlist_name}/{title}.mp3'
	else:
		os.system(f"mkdir {playlist_name}")
		mp4_file, mp3_file = rf'{title}.mp4', rf'{playlist_name}/{title}.mp3'
	audioclip = VideoFileClip(mp4_file).audio
	audioclip.write_audiofile(mp3_file)
	audioclip.close()
	videoclip.close()
	os.remove(f"{title}.mp4")
for track in result['tracks']['items']:
	print(f"downloading ", end='')
	try:
		download(track['track']['name'])
		print(track['track']['name'], ': {"statut": "downloaded succesfully"}')
	except:
		try:
			os.system(f'rm {title}.mp4')
		except:
			os.system(f'rm {title}.mp3')
		print(track['track']['name'], ': {"statut": "the download encountred some errors, please retry later"}')
