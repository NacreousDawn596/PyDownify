echo "downloading dependencies..."
sleep 1
sudo apt-get install python3 python3-pip curl
clear
sudo dnf install python3 python3-pip curl
clear
sudo pacman -S python3 python3-pip curl
clear
echo "downloading python libs..."
pip install -r requirements.txt
clear
echo "done!"
