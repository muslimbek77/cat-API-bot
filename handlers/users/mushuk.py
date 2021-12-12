from aiogram.types.message import Message
import requests
from loader import dp

def get_url():
    contents = requests.get('https://thatcopy.pw/catapi/rest/').json()
    image_url = contents['url']
    return image_url
 
# Echo bot
@dp.message_handler(state=None, commands='mushuk')
async def bot_echo(message: Message):

    url = get_url()    
    await message.answer_photo(url,caption="<a href='https://t.me/muizzabot'>Mushuklar</a> 🐈 ")

