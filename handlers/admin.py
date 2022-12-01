from aiogram import types, Dispatcher
from config import bot, dp, ADMINS
import random

async def game(message: types.Message):
    if message.text.startswith('game') and message.from_user.id in ADMINS:
        list_emoji = ['⚽', '🏀', '🎰', '🎳', '🎯', '🎲']
        emoji_random = random.choice(list_emoji)
        await bot.send_dice(message.from_user.id, emoji=emoji_random)
    else:
        await message.answer("Это функция для тебя не работает")


def register_admin_handlers(dp: Dispatcher):
    dp.register_message_handler(game)