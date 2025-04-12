import asyncio
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from src.core import router
from src.database.commands import DataBase

load_dotenv()

bot = Bot(token=os.getenv('ACCESS_TOKEN'))
dp = Dispatcher()
dp.include_router(router)


async def start():
    await DataBase(os.getenv('DB_URL')).create_db()
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(start())
