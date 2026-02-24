import re
import os
from os import environ, getenv
from Script import script

# Utility functions
id_pattern = re.compile(r'^.\d+$')

def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# ============================
# Bot Information Configuration
# ============================
SESSION = environ.get('SESSION', 'royal_search')
API_ID = int(environ.get('API_ID', ''))
API_HASH = environ.get('API_HASH', '')
BOT_TOKEN = environ.get('BOT_TOKEN', "")

# ============================
# Bot Settings Configuration
# ============================
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))
INDEX_CAPTION = bool(environ.get('SAVE_CAPTION', True))

PICS = (environ.get('PICS', 'https://graph.org/file/fa4a5a0a68db76100301e-914baa673dac438963.jpg https://graph.org/file/5daba2278b01a89c5a343-0955a8f7f5c161642f.jpg https://graph.org/file/4b11d3067189317433e01-81268cba7feee53044.jpg https://graph.org/file/83d8b6d48d5b44e3bb2b0-3abdf31d3f4a1b12d0.jpg')).split()
NOR_IMG = environ.get("NOR_IMG", "https://graph.org/file/e20b5fdaf217252964202.jpg")
MELCOW_PHOTO = environ.get("MELCOW_PHOTO", "https://graph.org/file/83d8b6d48d5b44e3bb2b0-3abdf31d3f4a1b12d0.jpg")
SPELL_IMG = environ.get("SPELL_IMG", "https://graph.org/file/13702ae26fb05df52667c.jpg")
SUBSCRIPTION = (environ.get('SUBSCRIPTION', 'https://graph.org/file/7e7dedc34ebdacb553bcd-f5444a94d5c3a14385.jpg'))
FSUB_PICS = (environ.get('FSUB_PICS', 'https://graph.org/file/33fca1f5101b22a351ff6-53bdd67d55cb33252f.jpg')).split()

# ============================
# Admin & Channels
# ============================
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-100').split()]
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-100'))
BIN_CHANNEL = int(environ.get('BIN_CHANNEL', '-100'))
support_chat_id = environ.get('SUPPORT_CHAT_ID', '-100')
reqst_channel = environ.get('REQST_CHANNEL_ID', '-100')

# ============================
# MongoDB Configuration
# ============================
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'library_files')
MULTIPLE_DB = is_enabled(os.environ.get('MULTIPLE_DB', "False"), False)
DATABASE_URI2 = environ.get('DATABASE_URI2', "")

# ============================
# Library & International Logic
# ============================
# Updated for International Publishing Standards
LANGUAGES = {
    "ᴇɴɢʟɪsʜ": "eng", 
    "ʜɪɴᴅɪ": "hin", 
    "ᴀʀᴀʙɪᴄ": "ara", 
    "ʀᴜssɪᴀɴ": "rus", 
    "ғʀᴇɴᴄʜ": "fre", 
    "ᴊᴀᴘᴀɴᴇsᴇ": "jpn", 
    "sᴘᴀɴɪsʜ": "spa", 
    "ɢᴇʀᴍᴀɴ": "ger", 
    "ᴋᴏʀᴇᴀɴ": "kor"
}

# Swapped resolutions for book formats
QUALITIES = ["PDF", "EPUB", "MOBI", "CBZ", "ZIP"]

# Swapped Seasons for Volumes
SEASON_COUNT = 150 
SEASONS = [f"Vol {i}" for i in range(1, SEASON_COUNT + 1)]

# ============================
# Verification Settings
# ============================
IS_VERIFY = is_enabled(environ.get('IS_VERIFY', 'False'), False)
SHORTENER_API = environ.get("SHORTENER_API", "")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", "")
TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "1200"))
THREE_VERIFY_GAP = int(environ.get('THREE_VERIFY_GAP', "54000"))

# ============================
# Global Links
# ============================
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/')
OWNER_LNK = environ.get('OWNER_LNK', 'https://t.me/')
UPDATE_CHNL_LNK = environ.get('UPDATE_CHNL_LNK', 'https://t.me/')

# ============================
# Miscellaneous Settings
# ============================
ULTRA_FAST_MODE = is_enabled(environ.get('ULTRA_FAST_MODE', "True"), True)
MAX_B_TN = environ.get("MAX_B_TN", "5")
DELETE_TIME = int(environ.get("DELETE_TIME", "300"))
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
IMDB = False # Disabled for books to save bandwidth
PM_SEARCH = True
EMOJI_MODE = False

# Don't Change Anything Here
if MULTIPLE_DB == False:
    DATABASE_URI = DATABASE_URI
    DATABASE_URI2 = DATABASE_URI
else:
    DATABASE_URI = DATABASE_URI
    DATABASE_URI2 = DATABASE_URI2
