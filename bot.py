import pyrogram

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os

from config import Config
from pyrogram import Client 
logging.getLogger("pyrogram").setLevel(logging.WARNING)


if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    app = Client(
        "ShowJson",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        plugins=plugins,
        workers=100
        LOG_CHANNEL = config.LOG_CHANNEL
        AUTH_USERS = config.AUTH_USERS 
        DB_URL = config.DB_URL
      DB_NAME = config.DB_NAME
    )
    app.run()
