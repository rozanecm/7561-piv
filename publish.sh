#!/bin/bash
source venv/bin/activate
pyinstaller --add-data 'res/*.png:res/' --onefile app.py
