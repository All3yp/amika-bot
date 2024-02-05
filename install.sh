#!/bin/sh

sudo apt-get update
sudo apt-get install firefox
git clone https://github.com/All3yp/amika-bot
cd amika-bot
python3 -m venv amika-env
pip3 install -r requirements.txt
source amika-env/bin/activate