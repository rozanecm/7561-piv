#!/bin/sh
sudo apt install python3-virtualenv -y
virtualenv -p python3 venv
source venv/bin/activate && pip install -r requirements.txt
sudo apt-get install qt5-default -y