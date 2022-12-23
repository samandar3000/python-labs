import requests

API_link = "https://api.telegram.org/bot5538790933:AAEuwxTODAUb4cB12g4KkCBPgwJjJlAJ27s"

updates = requests.get(API_link + "/getUpdates?offset=-1").json()

print(updates)

message = updates["result"][0]["message"]
chat_id = message["from"]["id"]
text = message["text"]

sent_message = requests.get(API_link + f"/sendMessage?chat_id={chat_id}&text=Здравствуй, ты написал {text}")

BOT_TOKEN = "5538790933:AAEuwxTODAUb4cB12g4KkCBPgwJjJlAJ27s"
admin_id = 1136634196

from main import bot, dp
from aiogram.types import Message
from config import admin_id

async def send_to_admin(dp):
    await bot.send_message(chat_id=admin_id, text="Бот запущен")

@dp.message_handler()
async def echo(message: Message):
    text = f"Здравствуй, ты написал: {message.text}"
    await message.answer(text=text)

import asyncio

from aiogram import Bot, Dispatcher, executor
from config import BOT_TOKEN



loop = asyncio.get_event_loop()
bot = Bot(BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, loop=loop)

if __name__ == "__main__":
    from handlers import dp, send_to_admin
    executor.start_polling(dp, on_startup=send_to_admin)
