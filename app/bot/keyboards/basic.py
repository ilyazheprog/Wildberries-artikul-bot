from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from modules.dataclasses.buttons import Buttons

client_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=Buttons.GET_DATA_FOR_PRODUCT),
        ],
    ],
    resize_keyboard=True,
)
