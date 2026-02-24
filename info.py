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

# Restored Original Graph URLs
PICS = (environ.get('PICS', 'https://graph.org/file/fa4a5a0a68db76100301e-914baa673dac438963.jpg https://graph.org/file/5daba2278b01a89c5a343-0955a8f7f5c161642f.jpg https://graph.org/file/4b11d3067189317433e01-81268cba7feee53044.jpg https://graph.org/file/83d8b6d48d5b44e3bb2b0-3abdf31d3f4a1b12d0.jpg')).split()
NOR_IMG = environ.get("NOR_IMG", "https://graph.org/file/e20b5fdaf217252964202.jpg")
MELCOW_PHOTO = environ.get("MELCOW_PHOTO", "https://graph.org/file/83d8b6d48d5b44e3bb2b0-3abdf31d3f4a1b12d0.jpg")
SPELL_IMG = environ.get("SPELL_IMG", "https://graph.org/file/13702ae26fb05df52667c.jpg")
SUBSCRIPTION = (environ.get('SUBSCRIPTION', 'https://graph.org/file/7e7dedc34ebdacb553bcd-f5444a94d5c3a14385.jpg'))
FSUB_PICS = (environ.get('FSUB_PICS', 'https://graph.org/file/33fca1f5101b22a351ff6-53bdd67d55cb33252f.jpg https://graph.org/file/33fca1f5101b22a351ff6-53bdd67d55cb33252f.jpg')).split()

# ============================
# Admin, Channels & Users Configuration
# ============================
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-100').split()]

LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-100'))
BIN_CHANNEL = int(environ.get('BIN_CHANNEL', '-100'))
PREMIUM_LOGS = int(environ.get('PREMIUM_LOGS', '-100')) # Restore for deployment
support_chat_id = environ.get('SUPPORT_CHAT_ID', '-100')
reqst_channel = environ.get('REQST_CHANNEL_ID', '-100')
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'https://t.me/')

auth_req_channels = environ.get("AUTH_REQ_CHANNELS", "-100")
auth_channels = environ.get("AUTH_CHANNELS", "-100")

# ============================
# MongoDB Configuration
# ============================
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'library_files') # Library Collection
MULTIPLE_DB = is_enabled(os.environ.get('MULTIPLE_DB', "False"), False)
DATABASE_URI2 = environ.get('DATABASE_URI2', "")

# ============================
# Library & International Logic
# ============================
LANGUAGES = {
    "ᴇɴɢʟɪsʜ": "eng", "ʜɪɴᴅɪ": "hin", "ᴀʀᴀʙɪᴄ": "ara", 
    "ʀᴜssɪᴀɴ": "rus", "ғʀᴇɴᴄʜ": "fre", "ᴊᴀᴘᴀɴᴇsᴇ": "jpn", 
    "sᴘᴀɴɪsʜ": "spa", "ɢᴇʀᴍᴀɴ": "ger", "ᴋᴏʀᴇᴀɴ": "kor"
}
QUALITIES = ["PDF", "EPUB", "MOBI", "CBZ", "ZIP"]
SEASON_COUNT = 150 
SEASONS = [f"Vol {i}" for i in range(1, SEASON_COUNT + 1)]

# ============================
# Server & Web Configuration (STRICT RECOVERY)
# ============================
PORT = int(environ.get("PORT", "8080"))
NO_PORT = bool(environ.get('NO_PORT', False))
APP_NAME = environ.get('APP_NAME', None)
BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
FQDN = str(getenv('FQDN', BIND_ADRESS))

if 'DYNO' in environ:
    URL = "https://{}.herokuapp.com/".format(APP_NAME) if APP_NAME else "https://{}/".format(FQDN)
else:
    URL = "https://{}/".format(FQDN) if NO_PORT else "https://{}:{}/".format(FQDN, PORT)

HAS_SSL = bool(getenv('HAS_SSL', True))
if HAS_SSL:
    URL = "https://{}/".format(FQDN)
else:
    URL = "http://{}/".format(FQDN)

# ============================
# Channel & Group Links (Restored)
# ============================
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/entertainment_hab')
OWNER_LNK = environ.get('OWNER_LNK', 'https://t.me/Mikasa_devbot')
UPDATE_CHNL_LNK = environ.get('UPDATE_CHNL_LNK', 'https://t.me/updates_op')
QR_CODE = environ.get('QR_CODE', 'https://i.ibb.co/21kg9wRK/1771333820919.png')
OWNER_UPI_ID = environ.get('OWNER_UPI_ID', 'angrajanuj@oksbi')

# ============================
# Miscellaneous Settings
# ============================
ULTRA_FAST_MODE = is_enabled(environ.get('ULTRA_FAST_MODE', "True"), True)
MAX_B_TN = environ.get("MAX_B_TN", "5")
DELETE_TIME = int(environ.get("DELETE_TIME", "300"))
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PM_SEARCH = bool(environ.get('PM_SEARCH', True))
EMOJI_MODE = bool(environ.get('EMOJI_MODE', False))
IMDB = False

# Ensure Auth lists are ready
AUTH_REQ_CHANNELS = [int(ch) for ch in auth_req_channels.split() if ch and id_pattern.match(ch)] 
AUTH_CHANNELS = [int(ch) for ch in auth_channels.split() if ch and id_pattern.match(ch)]
REQST_CHANNEL = int(environ.get('REQST_CHANNEL_ID', '-100'))
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None

if MULTIPLE_DB == False:
    DATABASE_URI2 = DATABASE_URI

# Log String logic for bot startup
LOG_STR = "Library Config Active.\n"
