echo "downloading dependencies..."
sleep 1
apt-get install python python-pip curl wget ffmpeg -y
clear
echo "downloading libs"
pip3 install yt-dlp youtube-search-python==1.6.5 bs4==0.0.1 requests
clear
echo "done!"
echo "now you can run it with => python3 main.py --help"
