from aiogram import F, Router, types
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
import httpx

from modules.dataclasses.buttons import Buttons
from bot.handlers.routers import client_router
from bot.keyboards import client_keyboard
from bot.states import ClientStates
from modules.envs import settings

router = Router()
client_router.include_router(router)

BACKEND_URL = settings.backend.url


@router.message(CommandStart())
async def start(message: types.Message, state: FSMContext):
    """Стартовое сообщение для клиента."""
    await state.set_state(ClientStates.main_menu)
    await message.reply("Добро пожаловать!\n", reply_markup=client_keyboard)


@router.message(F.text == Buttons.GET_DATA_FOR_PRODUCT)
async def get_data_for_product(message: types.Message, state: FSMContext):
    """Получить данные по товару."""
    await state.set_state(ClientStates.enter_artikul)
    await message.reply("Введите артикул товара:")


@router.message(ClientStates.enter_artikul)
async def enter_artikul(message: types.Message, state: FSMContext):
    """Ввод артикула товара."""
    try:
        artikul = int(message.text)
    except ValueError:
        await message.reply("Артикул должен быть числом.")
        return

    url = f"{BACKEND_URL}/api/v1/products/details/{artikul}"
    async with httpx.AsyncClient() as client:
        response = await client.get(
            url,
            headers={"Authorization": f"Bearer {settings.backend.auth_token}"},
        )
        if response.status_code != 200:
            await message.reply(
                f"Не удалось получить информацию по товару с артикулом {artikul}."
            )
            return
        data = response.json()
    await message.reply(
        f"Информация по товару с артикулом {artikul}:\n"
        f"Название: {data['name']}\n"
        f"Цена: {data['price_in_copecs']/100}\n"
        f"Рейтинг: {data['rate']}\n"
        f"Количество: {data['total_quantity']}\n"
    )
    await state.finish()
