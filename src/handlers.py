from aiogram import Router, F, Bot
from aiogram.filters import Command
from aiogram.types import Message
from io import BytesIO
from src.proceed_data import proceed
from src.database.commands import DataBase
from dotenv import load_dotenv

import os


load_dotenv()

rout = Router()
sql = DataBase(os.getenv('DB_URL'))


@rout.message(Command('start'))
async def start(message: Message):
    await message.answer('Hi, yes. I am bot')


@rout.message(F.document)
async def input_file(message: Message, bot: Bot):
    file = message.document
    if file:
        buffer = BytesIO()
        await bot.download(file.file_id, destination=buffer)
        buffer.seek(0)

        extracted_data = proceed(buffer.read())
        report = {}
        i = 0
        for title in extracted_data['title'].values():
            for url in extracted_data['url'].values():
                for xpath in extracted_data['xpath'].values():
                    await sql.add_data(title, url, xpath)
                    report[i] = [title, url, xpath]
                    i += 1
                    break
                break
        s = ''
        for x in report.values():
            s = ''.join(x[0]) + '\n' + ''.join(f'`{x[1]}`') + '\n' + ''.join(x[2])
            s += '\n'

        await message.answer(s, parse_mode='Markdown')
        await message.answer(str(report))

