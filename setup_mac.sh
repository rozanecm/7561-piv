#!/bin/bash
brew install qt5
brew install virtualenv
virtualenv -p python3 venv
source venv/bin/activate && pip install -r requirements.txt
