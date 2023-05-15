from aiogram import Dispatcher,Bot,executor
from aiogram.types import Message
import logging
import time
from api import airboshla

logging.basicConfig(level=logging.INFO)

bot=Bot(token=' token yoziladi')
dp=Dispatcher(bot)

@dp.message_handler(commands='start')
async def salomlash(message: Message):
    await message.answer("Dollar pulni kirit")

@dp.message_handler()
async def valyuta(message: Message):
        print(f"{message.from_user.full_name}({message.from_user.username}): {message.text} | TIME: {time.asctime()} ")
        pul=message.text
        if pul.isnumeric():
            conversiya=airboshla(pul)
            natija=conversiya['conversion_result']
            await message.answer(f"us {pul} dollar --> uz {natija} so'm")
        else:
            await message.reply("Sonni kiriting")
    

if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)