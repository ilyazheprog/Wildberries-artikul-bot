from asyncio import run

from aiogram import Bot, Dispatcher

from bot.utils.registry import registry
from modules.envs.settings import settings

async def start(bot: Bot, dp: Dispatcher):
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


def main():
    dp = Dispatcher()

    registry(dp)

    run(start(settings.bot.bot, dp))


if __name__ == "__main__":
    main()
