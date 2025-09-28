from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from bot.config import WEB_APP_URL

def main_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton("🍽 Menu", web_app=WebAppInfo(url=WEB_APP_URL)))
    return kb