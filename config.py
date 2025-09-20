from typing import Optional
from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    _database = os.getenv("DATABASE") or "sqlite:///database.db"
    _async_database = os.getenv("A_DATABASE") or "sqlite+aiosqlite:///database.db"
    _bot_token = os.getenv("BOT_TOKEN")

    @classmethod
    def get_database(cls) -> str:
        return cls._database

    @classmethod
    def get_adatabase(cls) -> str:
        return cls._async_database

    @classmethod
    def get_bot_token(cls) -> Optional[str]:
        return cls._bot_token
