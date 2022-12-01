from config import dp, bot
from aiogram import types, Dispatcher
import random
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# @dp.message_handler(commands=['start', 'help'])
async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id, f"Hello{message.from_user.first_name}!")


# @dp.message_handler(commands=['meme'])
async def meme(message: types.Message):
    photo_list = ['media/images.jpg', 'media/Без названия (1).jpg']
    photo = open(random.choice(photo_list), 'rb')
    await bot.send_photo(message.from_user.id, photo=photo)


# @dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call1 = InlineKeyboardButton("NEXT", callback_data="button_call1")
    markup.add(button_call1)
    question = " Сколько дней ружно, чтобы Земля  сщвершила оборот вокруг Солнца ?"
    answers = [
        "300",
        "250",
        "30",
        "365"
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=True,
        type='quiz',
        correct_option_id=3,
        reply_markup=markup
    )

async def pin_message(message: types.Message):
    if message.reply_to_message:
        await bot.pin_chat_message(message.from_user.id, message.reply_to_message.message_id)
    else:
        await message.answer("Это должно быыть ответом на сообщении")

def register_client_handlers(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start', 'help'])
    dp.register_message_handler(meme, commands=['meme'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(pin_message, commands=['pin'], commands_prefix='!')
