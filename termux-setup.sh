echo "downloading dependencies..."

sleep 1

pkg install python curl ffmpeg

clear

echo "downloading python libs..."

pip install -r requirements.txt

mkdir /sdcard/PyDownify

clear

echo "done!"
