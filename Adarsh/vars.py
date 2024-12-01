import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', "18029060"))
    API_HASH = str(getenv('API_HASH', "c7e952440251e33bb5cce566b29f7254"))
    BOT_TOKEN = str(getenv('BOT_TOKEN', "7989012469:AAHAhqvM7kWTlorL_V8DgHqsWqsj-O74rZY"))
    name = str(getenv('name', 'THHFTOLBOT'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '0'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', "-1002376421685"))
    PORT = int(getenv('PORT', 80))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "1991522624").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = str(getenv('APP_NAME'))
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', "SANDIP_1507"))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', "mongodb+srv://jisshukh:jisshukh@cluster0.y9bck.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', "The_Happy_Hours"))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "0")).split())) 
