import asyncio
from aiogram import Bot, Dispatcher
from bot.config import BOT_TOKEN
from bot.handlers import router   # yangi router

dp = Dispatcher()
dp.include_router(router)

async def main():
    await dp.start_polling(BOT)

if __name__ == '__main__':
    asyncio.run(main())