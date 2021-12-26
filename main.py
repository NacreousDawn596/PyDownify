import sys
import os
try:
	from moviepy.editor import *
except:
	pass
import time
import requests
from pytube import YouTube
import json
from youtubesearchpython import VideosSearch
playlist = sys.argv[1]
infos = os.popen(f'curl -s {playlist}').read()
uh, mm = infos.split("Spotify.Entity = ")[1].split('M","ZW"]};')[0], 'M","ZW"]}'
result = json.loads(f'{uh}{mm}')
if os.popen('uname -o').read() == "Android":
	playlist_name = f"/sdcard/PyDownify/{result['name']}"
else:
	playlist_name = result['name']
os.system(f'mkdir "{playlist_name}"')
def getUrl(name):
	videosSearch = VideosSearch(name, limit = 1)
	print(videosSearch.result()['result'][0]['title'], "...")
	return {'url': videosSearch.result()['result'][0]['link'], 'name': videosSearch.result()['result'][0]['title']}
def download(name):
	try:
		if "200" in requests.get('https://google.com/search?q=NacreousDawn596'):
			pass
		else:
			print('uh, something is wrong on the device ._., I hope it gonna be just an internet issue')
	except:
		print('please, check your internet connection and retry ^^')
		sys.exit()
	allstuff = getUrl(name)
	url, title = allstuff['url'], allstuff['name'].replace('|', '').replace('.', '').replace(',', '').replace("it's", "its").replace('~', '')
	if f"{title}.mp3" in os.popen(f'ls "{playlist_name}"').read():
		return
	else:
		YouTube(url).streams.filter(progressive=True, file_extension='mp4').first().download()
		try:
			mp4_file, mp3_file = rf'{title}.mp4', rf'{playlist_name}/{title}.mp3'
			audioclip = VideoFileClip(mp4_file).audio
			audioclip.write_audiofile(mp3_file)
			audioclip.close()
		except:
			if title not in os.popen(f'ls {playlist_name}').read():
				os.system(f'ffmpeg -i {title}.mp4 -q:a 0 -map a {playlist_name}/{title}.mp3')
		os.remove(f"{title}.mp4")
def verification():
	for unconverted_title in os.popen('ls *.mp4').splitlines():
		if f"{unconverted_title.replace('.mp4', '')}.mp3" not in os.popen(f"ls {playlist_name}").read():
			os.system(f'ffmpeg -i "{title}" -q:a 0 -map a "{playlist_name}/{unconverted_title.replace(".mp4", "")}.mp3"')
		os.system(f'rm "{title}"')
for track in result['tracks']['items']:
	title = VideosSearch(track['track']['name'], limit = 1).result()['result'][0]['title']
	print(f"downloading ", end='')
	try:
		download(track['track']['name'])
		print(track['track']['name'], ': {"statut": "downloaded succesfully"}')
	except:
		try:
			os.system(f'rm *.mp4')
		except:
			os.system(f'rm "{playlist_name}/{title}.mp3"')
		os.system(f'echo "{title}" >> "{playlist_name}/.fail.txt"')
		print(track['track']['name'], ': {"statut": "the download encountred some errors, please retry later"}')
verification()
