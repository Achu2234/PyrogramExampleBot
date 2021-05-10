# ( c ) Bruh_0x
# Made for beginners like me to learn some very basic things {Made with Love}
# Me sometimes suck at coding so PR's welcome

# Please don't copy paste cuz i made this for learning! Not for copy pasting! 
# I realize Copy Pasting can't make a programmer So Don't Copy Paste :)

# If you're deploying this on vps or in your pc or anything add your value in ""

import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    APP_ID = int(os.environ.get("APP_ID", ""))
    API_HASH = os.environ.get("API_HASH", "")