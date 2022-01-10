import logging
import os
from typing import Final, Union
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


def load_asset(file: str, split: bool = False) -> Union[str, list[str]]:
    path_list = [os.path.dirname(__file__), os.pardir, "assets", file]
    with open(os.path.abspath(os.path.join(*path_list))) as f:
        logger.debug(f"load asset {file}")
        if split:
            return f.readlines()
        return f.read()

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
