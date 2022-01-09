import logging
import os
from typing import Final
from urllib.parse import quote_plus

import dotenv
from motor import motor_asyncio as motor

dotenv.load_dotenv()
TOKEN: Final = os.getenv("TOKEN")
PREFIX: Final = os.getenv("PREFIX", "#")
USERNAME: Final = os.getenv("USERNAME")
PASSWORD: Final = os.getenv("PASSWORD")

print(f"discord: PREFIX: {PREFIX}, TOKEN: {TOKEN}")
print(f"mongodb: USERNAME: {USERNAME}, PASSWORD: {PASSWORD}")

host = "mongo"
database = "test"
client = motor.AsyncIOMotorClient(
    "mongodb://{0}:{1}@{2}:27017/{3}?authSource=admin".format(
        quote_plus(USERNAME),
        quote_plus(PASSWORD),
        quote_plus(host),
        quote_plus(database),
    )
)
DB = client[database]

__all__ = (TOKEN, PREFIX, DB)
