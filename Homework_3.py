from aiogram import Bot, Dispatcher, types,  executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.storage import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import token
import logging

bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO)

button = [
    types.KeyboardButton('о нас'),
    types.KeyboardButton('объекты'),
    types.KeyboardButton('контакты') 
]

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*button)

@dp.message_handler(commands ='start')
async def start(message:types.Message):
    await message.answer('здраствуй, выбери что тебя интересует:', reply_markup=keyboard)

@dp.message_handler(text='о нас')
async def about_us(message:types.Message):
    await message.answer('перейдите по ссылке,что узнать о нас: ')
    await message.answer('https://vg-stroy.com/about/')

@dp.message_handler(text='объекты')
async def objects(message:types.Message):
    await message.answer('здесь находиться информация о 3 обьектов, перейдите по ссылке:')
    await message.answer('https://vg-stroy.com/completedd_objects/zhk-tomiris/')
    await message.answer('https://vg-stroy.com/under_construction/zhk-vizion-sputnik/')
    await message.answer('https://vg-stroy.com/under_construction/zhk-vizion-lajf-park/')

@dp.message_handler(text='контакты')
async def contacts(message:types.Message):
    await message.answer('здесь находиться информация о контаках, зайдите по ссылке:')
    await message.answer('https://vg-stroy.com/contacts/')

executor.start_polling(dp)