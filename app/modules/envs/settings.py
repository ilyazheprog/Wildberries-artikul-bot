from dataclasses import dataclass

from aiogram import Bot as AioBot
from environs import Env


@dataclass
class Bot:
    bot: AioBot


@dataclass
class Backend:
    url: str
    auth_token: str

@dataclass
class Wildberries:
    get_details_url: str
    minutes_to_update_subscriptions: int


@dataclass
class Database:
    engine: str
    user: str
    pswd: str
    mame: str
    host: str
    echo: bool
    link: str = None


@dataclass
class Config:
    backend: Backend
    bot: Bot
    database: Database
    wildberries: Wildberries


def get_settings():
    env_var = Env()
    env_var.read_env()

    return Config(
        backend=Backend(
            url=env_var.str("BACKEND_URL"),
            auth_token=env_var.str("BACKEND_AUTH_TOKEN"),
        ),
        bot=Bot(
            bot=AioBot(env_var.str("TOKEN")),
        ),
        database=Database(
            engine=env_var.str("DB_ENGINE"),
            user=env_var.str("DB_USER"),
            pswd=env_var.str("DB_PSWD"),
            mame=env_var.str("DB_DB"),
            host=env_var.str("DB_HOST"),
            echo=env_var.bool("DB_ECHO"),
        ),
        wildberries=Wildberries(
            get_details_url=env_var.str("WB_GET_DETAILS_URL"),
            minutes_to_update_subscriptions=env_var.int("WB_MINUTES_TO_UPDATE_SUBSCRIPTIONS"),
        ),
    )


settings = get_settings()
sdb = settings.database
settings.database.link = f"{sdb.engine}://{sdb.user}:{sdb.pswd}@{sdb.host}/{sdb.mame}"
