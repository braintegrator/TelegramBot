import os
import random
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types.input_file import FSInputFile
from dotenv import load_dotenv

load_dotenv()
bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()

# Создаем клавиатуру
kb_builder = ReplyKeyboardBuilder()
kb_builder.add(
    KeyboardButton(text="Получить изображение"),
    KeyboardButton(text="Получить видео"),
    KeyboardButton(text="Получить цитату"),
)
kb_builder.adjust(1)
reply_kb = kb_builder.as_markup(resize_keyboard=True, is_persistent=True)


def get_random_file(folder):
    try:
        return random.choice(os.listdir(folder)) if os.path.exists(folder) else None
    except:
        return None


def get_random_quote():
    try:
        with open("quotes.txt", "r", encoding="utf-8") as f:
            quotes = f.read().splitlines()
        return random.choice(quotes) if quotes else None
    except FileNotFoundError:
        return None


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "Привет! Я PositiveInputsBot. Выбери, что ты хочешь получить:",
        reply_markup=reply_kb,
    )


@dp.message(F.text == "Получить изображение")
async def send_image(message: Message):
    if file := get_random_file("images"):
        await message.answer_photo(FSInputFile(f"images/{file}"))
    else:
        await message.answer("Изображения не найдены")


@dp.message(F.text == "Получить видео")
async def send_video(message: Message):
    if file := get_random_file("videos"):
        await message.answer_video(FSInputFile(f"videos/{file}"))
    else:
        await message.answer("Видео не найдены")


@dp.message(F.text == "Получить цитату")
async def send_quote(message: Message):
    if quote := get_random_quote():
        await message.answer(f"💡 {quote}")
    else:
        await message.answer("Цитаты не найдены")


@dp.message(Command("about"))
async def about(message: Message):
    await message.answer(
        "Бот создан [Begemot](https://t.me/photon_of_freedom)\n"
        "[hfwddm@gmail.com](mailto:hfwddm@gmail.com)\n"
        "При участии помощника-разработчика Qwen от Alibaba Cloud"
    )


if __name__ == "__main__":
    dp.run_polling(bot)
