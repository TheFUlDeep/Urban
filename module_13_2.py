# executor нет в новой версии
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
# aiogram.contrib нет в новой версии и fsm_storage
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher(storage=MemoryStorage())


@dp.message(CommandStart())
async def start(msg):
    print('Привет! Я бот помогающий твоему здоровью')


@dp.message()
async def all_massages(msg):
    print('Введите команду /start, чтобы начать общение')


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
