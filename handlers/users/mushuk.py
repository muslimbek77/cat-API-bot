from aiogram.types.message import Message
import requests
from loader import dp


 
# Echo bot
@dp.message_handler(state=None, commands='mushuk')
async def bot_echo(message: Message):
    await message.answer_photo((requests.get('https://api.thecatapi.com/v1/images/search').json()[0]['url'])
,caption="<a href='https://t.me/muizzabot'>Mushuklar</a> 🐈 ")

