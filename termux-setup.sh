echo "downloading dependencies..."

sleep 1

pkg install python python-pip curl

clear

echo "downloading python libs..."

pip install -r requirements.txt

clear

echo "done!"
