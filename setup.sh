echo "downloading dependencies..."
sleep 1
sudo apt-get install python2 python3 python3-pip curl wget ffmpeg -y
clear
echo "downloading python2 pip"
python3 get-pip.py
clear
echo "downloading libs"
pip2 install requests argparse
pip3 install youtube-dl==2021.12.17 youtube-search-python==1.6.5 bs4==0.0.1
clear
echo "done!"
echo "now you can run it with => python3 main.py --help"
