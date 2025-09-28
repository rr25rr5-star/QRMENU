from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from bot.keyboards import main_menu

router = Router()

@router.message(CommandStart())
async def start(m: Message):
    await m.answer("Assalomu alaykum!", reply_markup=main_menu())