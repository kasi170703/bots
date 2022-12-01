from aiogram import types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp
import logging
import random

@dp.message_handler(commands=['start', 'help'])
async def star_handler(message: types.Message):
    await bot.send_message(message.from_user.id, f"Hello{message.from_user.first_name}!")


@dp.message_handler(commands=['meme'])
async def meme(message: types.Message):
    photo_list = ['media/images.jpg', 'media/Без названия (1).jpg']
    photo = open(random.choice(photo_list), 'rb')
    await bot.send_photo(message.from_user.id, photo=photo)

@dp.message_handler(commands=['quiz'])
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


@dp.callback_query_handler(text='button_call1')
async def quiz_2(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call1 = InlineKeyboardButton("NEXT", callback_data="button_call1")
    question = "Есть ли у А.Касиета МОЗГ?"
    answers = [
        "нет",
        "возможно",
        "скорее всего",
        "да наверное нет"
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=True,
        type='quiz',
        correct_option_id=0,
    )

@dp.message_handler()
async def echo(message: types.Message):
    if message.text.isdigit():
        await bot.send_message(message.from_user.id, int(message.text) ** 2)
    else:
        await bot.send_message(message.from_user.id, message.text)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
