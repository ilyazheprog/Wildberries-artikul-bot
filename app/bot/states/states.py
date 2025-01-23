from aiogram.fsm.state import State, StatesGroup


class ClientStates(StatesGroup):
    """Состояния для клиентов."""

    main_menu = State()
    enter_artikul = State()
