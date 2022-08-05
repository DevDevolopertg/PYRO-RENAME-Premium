import os
from pyrogram import Client
import asyncio
import logging

PREMIUM_SESSION = os.environ.get("PREMIUM_SESSION", "pyrogram session")              

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

class User(Client):
    def __init__(self):
        super().__init__(
            PREMIUM_SESSION,
            api_hash=Config.API_HASH,
            api_id=Config.API_ID,
            workers=50
        )
        self.LOGGER = LOGGER

    
