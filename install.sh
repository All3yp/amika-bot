#!/bin/sh

sudo apt-get update
sudo apt-get install firefox openvpn unzip

git clone https://github.com/All3yp/amika-bot
cd amika-bot
python3 -m venv amika-env
pip3 install -r requirements.txt
source amika-env/bin/activate

sh <(wget -qO - https://downloads.nordcdn.com/apps/linux/install.sh)
# in case of error: sudo usermod -aG nordvpn $USER && reboot
sudo nordvpn login
sudo nordvpn connect