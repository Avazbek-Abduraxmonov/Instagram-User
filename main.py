from aiogram import Bot, Dispatcher, types
from asyncio import run
from aiogram.types import BotCommand
from aiogram.filters import Command
from function import *
from config import *

dp = Dispatcher()


async def get_start(bot: Bot):
    await bot.send_message(chat_id=admin_id, text='Bot ishga tushdi')
async def get_shutdown(bot: Bot):
    await bot.send_message(chat_id=admin_id, text="Bot ishdan to'xtadi")

async def start():
    dp.startup.register(get_start)
    
    dp.message.register(start_answer, Command('start'))
    dp.message.register(help_answer, Command('help'))
    dp.message.register(insta)
    
    bot = Bot(token=token)

    await bot.set_my_commands([
            BotCommand(command='/start', description='Botni ishga tushurish'),
            BotCommand(command='/help', description='Yordam berish')    
    ])

    dp.shutdown.register(get_shutdown)
    await dp.start_polling(bot, polling_timeout=1)


run(start())