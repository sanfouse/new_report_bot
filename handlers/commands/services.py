from aiogram import types
from aiogram.fsm.context import FSMContext
import text


async def cancel_and_clear_state(message: types.Message, state: FSMContext) -> None:
    await message.answer(
        text.CANCEL_TEXT
    )
    await state.clear()
