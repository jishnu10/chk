import os

class Config(object):

      BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
      API_ID = int(os.environ.get("API_ID", 12345))
      API_HASH = os.environ.get("API_HASH")
      OWNER_ID = int(os.environ.get("OWNER_ID"))
      LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))
      AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())
      DB_URL = os.environ.get("DB_URL", "")
      DB_NAME = os.environ.get("DB_NAME", "")

