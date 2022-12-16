# Creating a basic custom bot with Telegram and Python

After you have created a telegram bot using @botfather, retrieve its API key and paste it at the beginning of `bot.py`. That's all you need to do get started.

To install the project dependencies, run: 
```bash
chmod +x install.sh
./install.sh
```
or execute:
```bash
# install virtualenv
pip3 install virtualenv
# create a virtual environment folder
python3 -m venv env
# activate env and install dependencies
source env/bin/activate
pip install python-telegram-bot -U --pre
```

To start the bot, run:
```
chmod +x run.sh
./run.sh
```
or execute:
```bash
source env/bin/activate
python3 -i main.py
source deactivate
```

This should start a basic customizable bot able to:
- respond to user commands by running `CommandHandler`  functions.
- Utilize command arguments to execute code using `context.args` 
- process messages based on their type by running `MessageHandler`  functions.

For more information about this repo take look at the article here.
