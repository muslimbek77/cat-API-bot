from aiogram import types
import wikipedia

from loader import dp


wikipedia.set_lang('uz')

@dp.message_handler()
async def sendWiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond+"\n\n<a href='https://t.me/muizzabot'>Mushuklar</a> 🐈 ")
    except:
        await message.answer("<a href='https://t.me/muizzabot'>Mushuklar</a> 🐈  ")

