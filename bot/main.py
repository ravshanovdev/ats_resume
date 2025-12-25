import asyncio
from aiogram import Bot, Dispatcher
from bot.bot_config import BOT_TOKEN
from bot.handlers.start_handlers import router


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)

    print('bot ishga tushdi...')
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())