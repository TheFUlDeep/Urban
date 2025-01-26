from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import F
import asyncio

kb_list = [
    [KeyboardButton(text="Рассчитать")],
    [KeyboardButton(text="Информация")]
]
kb = ReplyKeyboardMarkup(keyboard=kb_list, resize_keyboard=True)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


api = ''
bot = Bot(token=api)
dp = Dispatcher(storage=MemoryStorage())


@dp.message(CommandStart())
async def set_age(msg, state):
    await msg.answer("Привет! Я бот помогающий твоему здоровью", reply_markup=kb)


@dp.message(F.text == "Рассчитать")
async def set_age(msg, state):
    await msg.answer("Введите свой возраст")
    await state.set_state(UserState.age)


@dp.message(UserState.age)
async def set_growth(msg, state):
    await state.update_data(age=msg.text)
    await msg.answer("Введите свой рост")
    await state.set_state(UserState.growth)


@dp.message(UserState.growth)
async def set_weight(msg, state):
    await state.update_data(growth=msg.text)
    await msg.answer("Введите свой вес")
    await state.set_state(UserState.weight)


@dp.message(UserState.weight)
async def send_calories(msg, state):
    await state.update_data(weight=msg.text)
    data = await state.get_data()
    await msg.answer('Ваша норма калорий ' + str(10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 *
                                                 int(data['age']) + 5))
    await state.clear()


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
