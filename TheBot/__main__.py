# ( c ) Bruh_0x
# Made for beginners like me to learn some very basic things {Made with Love}
# Me sometimes suck at coding so PR's welcome

# Please don't copy paste cuz i made this for learning! Not for copy pasting! 
# I realize Copy Pasting can't make a programmer So Don't Copy Paste :)

import pyrogram
from pyrogram import Client
from config import Config


if __name__ == "__main__" :
    plugins = dict(root="TheBot/plugins")
    app = pyrogram.Client(
        "NexaBots",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        plugins=plugins
    )
    app.run()