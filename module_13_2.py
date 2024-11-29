from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(text=['привет', 'Привет'])
async def hi(message):
    print('привет')


@dp.message_handler(commands=['старт'])
async def start_message(message):
    print('Привет! Я бот помогающий твоему здоровью.')


@dp.message_handler()
async def all_message(message):
    print('Введите команду /старт, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
