
import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7990629906:AAGzrcD88T23vNCRBqAH_18sSigA1e63-uQ")
    API_ID = int(os.environ.get("API_ID", "20821267"))
    API_HASH = os.environ.get("API_HASH", "8723cdf433be176300044547ee6bab7a")
    AUTH_USERS = "6881758615"


