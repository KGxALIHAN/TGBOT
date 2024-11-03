import os
from dotenv import dotenv_values
import asyncio
import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

config = dotenv_values(".env")  
bot_token = config.get('BOT_TOKEN') 
bot = Bot(token=bot_token)
dp = Dispatcher()

user_count = 0
unique_users = set()


@dp.message(Command("start"))
async def start_handler(message: types.Message):
    global user_count 
    user_id = message.from_user.id
    
    if user_id not in unique_users:
        unique_users.add(user_id)  
        user_count += 1  
    
    await message.answer(f'Привет {message.from_user.first_name}! У нас {user_count} уникальных пользователей.')


@dp.message(Command('myinfo'))
async def myinfo_handler(message: types.Message):
    name1 = message.from_user.first_name
    last_name = message.from_user.last_name
    id_user = message.from_user.id
    await message.answer(f'твое имя {name1} твоя фамилия {last_name} твое id {id_user}')

name_random = ['Alihan', 'Kazybek', 'Altynbek']
@dp.message(Command('random'))
async def random_name(message):
    random_choise = random.choice(name_random)
    await message.answer(random_choise)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
