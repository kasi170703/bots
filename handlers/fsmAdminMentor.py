from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


class FSMmentor(StatesGroup):
    id = State()
    name = State()
    direction = State()
    age = State()
    group = State()
    submit = State()


async def fsm_start(message: types.Message):
    if message.chat.type == "private":
        await FSMmentor.id.set()
        await message.answer("id mentora")
    else:
        await message.answer("Напиши в личку")


async def load_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["id"] = int(message.text)
    await FSMmentor.next()
    await message.answer("name mentora")


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["name"] = message.text
    await FSMmentor.next()
    await message.answer("Направление ментора")


async def load_direction(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["direction"] = (message.text)
    await FSMmentor.next()
    await message.answer("Возраст ментора")


async def load_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["age"] = int(message.text)
    await FSMmentor.next()
    await message.answer("Группа ментора")


async def load_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["group"] = (message.text)
    await FSMmentor.next()
    await message.answer("Все правильно?", reply_markup=ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=True
    ).add(
        KeyboardButton("Да"),
        KeyboardButton("Нет"),
    ))


async def submit(message: types.Message, state: FSMContext):
    if message.text.lower() == "да":
        await state.finish()
        await message.answer("Все свободен!")
    else:
        await message.answer("Отмена записи")
        await state.finish()


def register_handlers_fsm_mentor(dp: Dispatcher):
    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(load_name, state=FSMmentor.name)
    dp.register_message_handler(load_id, state=FSMmentor.id)
    dp.register_message_handler(load_direction, state=FSMmentor.direction)
    dp.register_message_handler(load_age, state=FSMmentor.age)
    dp.register_message_handler(load_group, state=FSMmentor.group)
    dp.register_message_handler(submit, state=FSMmentor.submit)

