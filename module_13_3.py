from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher(storage=MemoryStorage())


@dp.message(CommandStart())
async def start(msg):
    await msg.answer("Привет! Я бот помогающий твоему здоровью")


@dp.message()
async def all_messages(msg):
    await msg.answer("Введите команду /start, чтобы начать общение")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
