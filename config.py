# Copyright (c) 2025 devgagan : https://github.com/devgaganin.  
# Licensed under the GNU General Public License v3.0.  
# See LICENSE file in the repository root for full license text.

import os
from dotenv import load_dotenv

load_dotenv()

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = os.getenv("API_ID", "22590943")
API_HASH = os.getenv("API_HASH", "366ffec897af93a3f198f88454ebef1c")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7578483298:AAGyZjv2KR4_eKzt8S0j_IplP8UQc6b2rt4")
MONGO_DB = os.getenv("MONGO_DB", "mongodb+srv://DiggiDigi:ViperROX@cluster0.sa5j7yc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
OWNER_ID = list(map(int, os.getenv("OWNER_ID", "6668515216").split())) # list seperated via space
DB_NAME = os.getenv("DB_NAME", "telegram_downloader")
STRING = os.getenv("STRING", "BQFYtd8AA9lsOFfa4cYtCDwukVMOjjTIKnmB8lqdLBSEoN5VtO-q-pD_gL-V4z3FnUcE-E4PEAyYbfp-j4rUEpPXQXubNVsEhDB7w3QCG0cJDUmyxRqAReWTWTuXsYc_N3yJhIzYycIz_bwLqEpbo7hV63UT0Lb8Io20s-OIAeVhdiRrcQr6tcO8Gcxz10VyRRWRCwsxHo_I8ilMa1DYk45reqBTuZCQPwZVuxdgtN2dG05H8SetEclOAWRE4LMLq8O9PSVamQzlU8PINQhL_NorliTE2RiwP1Vpd9hwg0Pjy2nWgDA7VfSX6wMfX8JhTef-nKozo9amCI2W6_NlGqwUsOmcWwAAAAG9PyEaAA") # optional
LOG_GROUP = int(os.getenv("LOG_GROUP", "-1002329281910")) # optional with -100
FORCE_SUB = int(os.getenv("FORCE_SUB", "-1002470963728")) # optional with -100
MASTER_KEY = os.getenv("MASTER_KEY", "gK8HzLfT9QpViJcYeB5wRa3DmN7P2xUq") # for session encryption
IV_KEY = os.getenv("IV_KEY", "s7Yx5CpVmE3F") # for decryption
YT_COOKIES = os.getenv("YT_COOKIES", YTUB_COOKIES)
INSTA_COOKIES = os.getenv("INSTA_COOKIES", INST_COOKIES)
FREEMIUM_LIMIT = int(os.getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(os.getenv("PREMIUM_LIMIT", "2000"))
JOIN_LINK = os.getenv("JOIN_LINK", "https://t.me/DiggiDigi") # this link for start command message
ADMIN_CONTACT = os.getenv("ADMIN_CONTACT", "https://t.me/aViperROX")

