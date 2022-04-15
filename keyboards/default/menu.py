from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="2E"),
            KeyboardButton(text="2D"),
        ],
        [
            KeyboardButton(text="4E"),
            KeyboardButton(text="4I"),
        ],
        [
            KeyboardButton(text="3C"),
            KeyboardButton(text="3G"),
            KeyboardButton(text="3I"),
        ],
    ],
    resize_keyboard=True
)