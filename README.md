# Executable
An executable version of this software is available for download [here](https://drive.google.com/drive/folders/1YUM2VVjaF4yQYgm3gwEPKKY3SuDYmBK6?usp=sharing).

# Environment setup
The easiest way to install the software is by executing the scripts `setup.sh` or setup_mac.sh`, depending if you need the Linux or the Mac version. Nevertheless, detailed instructions are included below if you want to get a better grasp at each step of the setup.

## Linux

1. Install Git. This is necessary because one of the dependencies is installed from a GitHub repo.
   ```bash
   sudo apt install update -y && sudo apt install git -y
   ```
2. Install QT
   ```bash
   sudo apt install update -y && sudo apt-get install qt5-default -y
   ```
3. Clone this repo, and `cd` to it.
4. Virtual env.
   1. Install needed dependency
      ```bash
      sudo apt install update -y && sudo apt install python3-virtualenv -y
      ```
   2. Create virtual env
      ```bash
      virtualenv -p python3 venv
      ```
   3. Source virtual env
      ```bash
      source venv/bin/activate
      ```
5. Install python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   
## MacOS

1. Install Git.
   ```bash
   brew install git
   ```
2. Install QT
   ```bash
   brew install qt5
   ```
3. Clone this repo, and `cd` to it.

4. Virtual env.

   1. Install needed dependency
      ```bash
      brew install virtualenv
      ```
      
   2. Create virtual env
      ```bash
      virtualenv -p python3 venv
      ```
      
   3. Source virtual env
      ```bash
      source venv/bin/activate
      ```
      
6. Install python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

# Packing app
- `sudo apt install python3-dev -y`
- `sudo apt install binutils -y`
- `pyinstaller --add-data 'res/*.png:res/' --onefile app.py`

Info about static files: [runtime information](https://pyinstaller.readthedocs.io/en/stable/runtime-information.html).
