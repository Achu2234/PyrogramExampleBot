# ( c ) Bruh_0x
# Made for beginners like me to learn some very basic things {Made with Love}
# Me sometimes suck at coding so PR's welcome

# Please don't copy paste cuz i made this for learning! Not for copy pasting! 
# I realize Copy Pasting can't make a programmer So Don't Copy Paste :)

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

# Bot will works both private & public because we don't filter chat private or group (Lol huh?)

@Client.on_message(filters.command(["start", "start@Pyro_Tg_Bot"]))
async def start(_, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name} 😉️!</b>

Heya I'm Alive :)

Made by **@Amalbiju154** for Noob/Beginners Like Him!

Join **@Animemusicarchive6**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔰️ My Updates Channel 🔰️", url="https://t.me/Animemusicarchive6"
                    ),
                    InlineKeyboardButton(
                        "⚜️ Support Group ⚜️", url="https://t.me/Yeageristbots"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Follow On Github", url="https://github.com/Achu2234"
                    )
                ]
            ]
        )
    )


# So now let's make private only command

@Client.on_message(filters.command(["repo", "repo@Pyro_Tg_Bot"]) & filters.private)
async def repo(_, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name} 😉️!</b>

Kk Click On The Below Button For The Repo :)

Made by **@Amalbiju154** for Noob/Beginners Like Him!

Join **@NexaBotsUpdates**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Repo", url=""
                    )
                ]
            ]
        )
    )
