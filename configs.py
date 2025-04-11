# (c) @AbirHasan2005

import os
import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)


class Config(object):
    API_ID = int(os.environ.get("API_ID", "27885190"))
    API_HASH = os.environ.get("API_HASH", "2fa09a645e1970af43ee3fc6f9ab4f2f")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7949387572:AAGyzlzuMKPKKfM0GjiTcOwarqnpBPxAmwQ")
    DOWNLOAD_DIR = os.environ.get("DOWNLOAD_DIR", "./downloads")
    LOGGER = 1002622690724
    OWNER_ID = int(os.environ.get("OWNER_ID", 7508054127))
    PRO_USERS = list(set(int(x) for x in os.environ.get("PRO_USERS", "0").split()))
    PRO_USERS.append(7508054127)
    MONGODB_URI = os.environ.get("MONGODB_URI", "")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002622690724"))
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
