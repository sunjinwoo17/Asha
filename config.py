#(©)CodeXBotz

import os
import logging
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv()

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7364128304:AAEZCl3x2TKLlxwPyCFmXV_uMP7SROJE0xw")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "20902603"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "79e5caa103a9e9fb0183390b4800845d")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002294126424"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6283322330"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://ganeshganesh177:17032009@sasukeuchiha.k21bh.mongodb.net/?retryWrites=true&w=majority&appName=Sasukeuchiha")
DB_NAME = os.environ.get("DATABASE_NAME", "Sasukeuchiha")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))
JOIN_REQUEST_ENABLE = os.environ.get("JOIN_REQUEST_ENABLED", None)

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_PIC = os.environ.get("START_PIC","https://envs.sh/g3h.jpg")
START_MSG = os.environ.get(
    "START_MESSAGE",
    "✨ Welcome to Asha - Your Trusted File Sharing Assistant! ✨\n\n"
    "Hi {mention}! 👋\n\n"
    "I'm Asha, your personal file-sharing bot. With me, you can:\n"
    "📤 Upload files instantly.\n"
    "📥 Download and access shared files.\n"
    "🔗 Generate secure links for easy sharing.\n"
    "📂 Organize and manage your uploads effortlessly.\n\n"
    "Commands at a Glance:\n"
    "🆔 Your User ID: {id}\n"
    "👤 Username: {username}"
)

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6283322330").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

# Auto delete time in seconds.
AUTO_DELETE_TIME = int(os.getenv("AUTO_DELETE_TIME", "0"))
AUTO_DELETE_MSG = os.environ.get("AUTO_DELETE_MSG", "This file will be automatically deleted in {time} seconds. Please ensure you have saved any necessary content before this time.")
AUTO_DEL_SUCCESS_MSG = os.environ.get("AUTO_DEL_SUCCESS_MSG", "Your file has been successfully deleted. Thank you for using our service. ✅")

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>ᴡᴏʀᴋɪɴɢ ʜᴏᴜʀs</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
