# Environment setup
1. Install Git. This is necessary because one of the dependencies is installed from a GitHub repo.
   ```bash
   sudo apt install update -y && sudo apt install git -y
   ```
2. Install Qt
   ```bash
   sudo apt-get install qt5-default -y
   ```
3. Clone this repo, and `cd` to it.
4. Virtual env.
   1. Install needed dependency
      ```bash
      sudo apt install python3-virtualenv -y
      ```
   2. Create virtual env
      ```bash
      virtualenv -p python3 venv
      ```
   3. Source virtual env
      ```bash
      source venv/bin/activate
      ```
5. Install python dependencies: `pip install -r requirements.txt`

# Packing app
- `sudo apt install python3-dev -y`
- `sudo apt install binutils -y`
- `pyinstaller --add-data 'res/*.png:res/' --onefile app.py`

Info about static files: [runtime information](https://pyinstaller.readthedocs.io/en/stable/runtime-information.html).
