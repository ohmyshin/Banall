import os
from os import getenv

class Config:
    TELEGRAM_TOKEN = getenv("TELEGRAM_TOKEN", "6107417498:AAGPXIzVgqOqKCO9N-fAwIWODE4KtNyR4-8")
    TELEGRAM_APP_HASH= getenv("TELEGRAM_APP_HASH", "83b9a5efe0e619a7a0d0043844a860d9")
    TELEGRAM_APP_ID=int(getenv("TELEGRAM_APP_ID", "28320974"))
        
    if not TELEGRAM_APP_HASH:
        raise ValueError("TELEGRAM_APP_HASH not set")

    if not TELEGRAM_APP_ID:
        raise ValueError("TELEGRAM_APP_ID not set")
    if not TELEGRAM_TOKEN:
        raise ValueError("PYRO_SESSION / TELEGRAM_TOKEN not set")
