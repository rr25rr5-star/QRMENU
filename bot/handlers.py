from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import CommandStart
from bot.config import BOT_TOKEN, ADMIN_ID
from bot.keyboards import main_menu

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(CommandStart())
async def start(m: types.Message):
    await m.answer("Assalomu alaykum!", reply_markup=main_menu())