from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp


# @dp.callback_query_handler(text='button_call1')
async def quiz_2(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call2 = InlineKeyboardButton("NEXT", callback_data="button_call2")
    markup.add(button_call2)
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
        reply_markup=markup
    )

async def quiz_3(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call3 = InlineKeyboardButton("NEXT", callback_data="button_call3")
    question = "Какой сегодня день?"
    answers = [
        "2",
        "3",
        "5",
        "6"
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=True,
        type='quiz',
        correct_option_id=0,
    )


def register_callback_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text='button_call1')
    dp.register_callback_query_handler(quiz_3, text='button_call2')