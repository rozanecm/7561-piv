#!/bin/bash
pyinstaller --add-data 'res/*.png:res/' --onefile app.py
