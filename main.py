import config
import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.message import ContentType

# log
logging.basicConfig(level=logging.INFO)

# init
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

# echo bot

@dp.message_handler()
async def echo(message; types.Message):
    await message.answer (message.text)

# run long-polling

if __name__ == "main":
    executor.start_polling(dp, skip_updates=False) # чтобы обрабатывалось каждое сообщение с сервера телеграм
