# Environment setup
1. Install Git. This is necessary because one of the dependencies is installed from a GitHub repo.
2. Virtual env
   1. `sudo apt install python3-virtualenv -y`
   2. Create virtual env: `virtualenv -p python3 venv`
   3. Source virtual env: `source venv/bin/activate`
3. Install python dependencies: `pip install -r requirements.txt`
4. Install Qt: `sudo apt-get install qt5-default -y`

# Packing app
- `sudo apt install python3-dev -y`
- `sudo apt install binutils -y`
- `pyinstaller --add-data 'res/*.png:res/' --onefile app.py`

Info about static files: [runtime information](https://pyinstaller.readthedocs.io/en/stable/runtime-information.html).
