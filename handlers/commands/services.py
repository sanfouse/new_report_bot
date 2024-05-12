from aiogram import types
from aiogram.fsm.context import FSMContext


async def cancel_and_clear_state(message: types.Message, state: FSMContext) -> None:
    await message.answer(
            "Отмена"
        )
    await state.clear()