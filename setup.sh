echo "downloading dependencies..."
sleep 1
sudo apt-get install python3 python3-pip curl ffmpeg
clear
sudo dnf install python3 python3-pip curl ffmpeg
clear
sudo pacman -S python3 python3-pip curl ffmpeg
clear
echo "downloading python libs..."
pip3 install -r requirements.txt
clear
echo "done!"
