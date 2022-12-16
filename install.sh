# install virtualenv
pip3 install virtualenv
# create a virtual environment folder
python3 -m venv env
# activate env and install dependencies
source env/bin/activate
pip install python-telegram-bot -U --pre

