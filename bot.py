# ©️ LISA-KOREA | @LISA_FAN_LK | NT_BOT_CHANNEL | LISA-KOREA/YouTube-Video-Download-Bot

# [⚠️ Do not change this repo link ⚠️] :- https://github.com/LISA-KOREA/YouTube-Video-Download-Bot



from pyrogram import Client, filters
from Youtube.config import Config

# Create a Pyrogram client
app = Client(
    "my_bot",
    api_id=Config.API_ID,25604709
    api_hash=Config.API_HASH,6a53ef81ff567058c2aa8ef1f9fa0ba5
    bot_token=Config.BOT_TOKEN,7656527709:AAFaxqRDDlE9g49rRD-cLib3tte0CcnCrJs
    plugins=dict(root="Youtube")
)



# Start the bot
print("🎊 I AM ALIVE 🎊")
app.run()
