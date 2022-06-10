import os
import sys
import get
import threading

if sys.argv[1] == "-p": urls, download_folder = get.tracks(sys.argv[2]), get.name(sys.argv[2])
elif sys.argv[1] == "-t": urls, download_folder = [sys.argv[2]], get.name(sys.argv[2])
else:
    print("usage:\n\tpython3 main.py -p [playlist url]\n\n\tor\n\n\tpython3 main.py -t [track url]")
    sys.exit()
if "android" in os.popen("uname -a").read().split()[-1].lower():
    try:
        os.mkdir(f"/sdcard/Music/{download_folder}")
    except:
        pass
    os.chdir(f"/sdcard/Music/{download_folder}")
else:
    try:
        os.mkdir(f"./{download_folder}")
    except:
        pass
    os.chdir(f"./{download_folder}")

for url in urls:
    link, name = get.url(url)
    threading.Thread(target=get.audio, args=[link, name]).start()
