from pyrogram import Client
from pyrogram import filters
import logging
import os
from os import getenv

STARTED = 'Black Magic Begins...'
FINISH = 'done, {} users were removed from group'
ERROR = 'something Went Wrong Please Try Again.\n\n**{}** !'


class Config:
    TOKEN=getenv("BOT_TOKEN")
    OWNER=list(
        map(int, getenv("OWNER_ID", "").split()))
    APP_ID = int(getenv("API_ID", "8186557"))
    APP_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
    LOGGER=int(getenv("LOG_ID", "-1001658407031"))
 
    if not TOKEN:
        raise ValueError(' BOT TOKEN not set')
    
    if not APP_HASH:
        raise ValueError("API_HASH not set, set it first")

    if not APP_ID:
        raise ValueError("API_ID not set, set it first")
    if not LOGGER:
        raise ValueError("LOG_ID not set set i first")
       

    
OWN_UNAME=Config.OWNER

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

bot=Client(
           ":memory:",
           api_id=Config.APP_ID,
           api_hash=Config.APP_HASH,
           bot_token=Config.TOKEN
)
