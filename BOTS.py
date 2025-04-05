import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_func(message: types.Message):
    await message.answer('Вы ввели команду /start')

# Main entry point
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
