import os

import dotenv
from motor import motor_asyncio as motor

dotenv.load_dotenv()
TOKEN = os.getenv("TOKEN")
PREFIX = os.getenv("PREFIX", "#")
DB_TOKEN = os.getenv("DB_TOKEN")

dbclient = motor.AsyncIOMotorClient(DB_TOKEN)
db = dbclient.Bot
print(f"discord: PREFIX: {PREFIX}, TOKEN: {TOKEN}")
print(f"mongodb: USERNAME: {USERNAME}, PASSWORD: {PASSWORD}")
