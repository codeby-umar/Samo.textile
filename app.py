import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import (
    Message,
    ReplyKeyboardMarkup,
    KeyboardButton
)
from aiogram.filters import Command

TOKEN = "8343079285:AAHTt9-jFMn_sKIbB7Je0ILzi8qqPWzZJw8"

bot = Bot(token=TOKEN)
dp = Dispatcher()


contact_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📲 Raqamni tasdiqlash", request_contact=True)]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)


menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="👤 About Me")],
        [KeyboardButton(text="💼 Portfolio"), KeyboardButton(text="🐙 GitHub")],
        [KeyboardButton(text="📞 Aloqa")]
    ],
    resize_keyboard=True
)


@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(
        "Salom 👋\nBotdan foydalanish uchun telefon raqamingizni tasdiqlang:",
        reply_markup=contact_kb
    )

@dp.message(F.contact)
async def contact_handler(message: Message):
    await message.answer(
        "✅ Rahmat! Siz muvaffaqiyatli tasdiqlandingiz.\n\nQuyidagi menudan foydalaning 👇",
        reply_markup=menu_kb
    )


@dp.message(F.text == "👤 About Me")
async def about_me(message: Message):
    await message.answer(
        "👤 Muhammad Umar\n\n"
        "💻 Junior Frontend Developer\n"
        "📍 O‘zbekiston\n\n"
        "🛠 Skills:\n"
        "- HTML, CSS, JavaScript, TypeScript\n"
        "- React, Tailwind CSS, Bootstrap\n"
        "- Python, Django (Backend asoslari)\n"
    )


@dp.message(F.text == "💼 Portfolio")
async def portfolio(message: Message):
    await message.answer(
        "💼 Portfolio loyihalarim:\n\n"
        "🔹 Zumar Office – Frontend Developer\n"
        "🔹 EGOMAN – Backend Developer\n\n"
        "Portfolio sayti:\n"
        "🌐 https://shahk-web.netlify.app/"
    )


@dp.message(F.text == "🐙 GitHub")
async def github(message: Message):
    await message.answer(
        "🐙 GitHub profilim:\n\n"
        "👉 https://github.com/codeby-umar/"
    )


@dp.message(F.text == "📞 Aloqa")
async def contact(message: Message):
    await message.answer(
        "📞 Aloqa uchun:\n\n"
        "📧 Email: codingbyumar\n"
        "📱 Telegram: @shahkwebs"
    )


@dp.message(Command("help"))
async def help_handler(message: Message):
    await message.answer(
        "/start - Botni ishga tushirish\n"
        "/help - Yordam"
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
