echo "downloading dependencies..."
sleep 1
sudo apt-get install python3 python3-pip curl wget ffmpeg -y
clear
echo "downloading libs"
pip3 install youtube-dl==2021.12.17 youtube-search-python==1.6.5 bs4==0.0.1 requests
clear
echo "done!"
echo "now you can run it with => python3 main.py --help"
