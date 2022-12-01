from aiogram import types
from aiogram.utils import executor
from config import bot, dp
import logging
from handlers import extra, callback, client, admin

client.register_client_handlers(dp)
callback.register_callback_handlers(dp)
admin.register_admin_handlers(dp)
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
