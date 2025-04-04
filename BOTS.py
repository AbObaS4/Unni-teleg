import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

API_TOKEN = '7530243183:AAHinl-7GaTCMzlB6Fni20hc9qIelQ0EWF0'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
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
