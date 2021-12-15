echo "downloading dependencies..."

sleep 1

pkg install python curl

clear

echo "downloading python libs..."

pip install -r requirements.txt

clear

echo "done!"
