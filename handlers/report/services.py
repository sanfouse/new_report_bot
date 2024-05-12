import text
from aiogram import types
from aiogram.fsm.context import FSMContext
from keyboards.report.inline import command_finish_keyboard

async def get_result_text(data: dict) -> str:
    return text.RESULT_TEXT.format(
        data['route_number'], data['date'], data['time'], data['route'], data['car_numbers'], data['report'], data['email'], data["username"]
    )

async def get_email_result_text(data: dict) -> str:
    return text.EMAIL_RESULT_TEXT.format(
        data['route_number'], data['date'], data['time'], data['route'], data['car_numbers'], data['report'], data['email'], data["username"]
    )

async def show_result_text(message: types.Message, state: FSMContext):
    state_data = await state.get_data()
    builder = await command_finish_keyboard()
    RESULT_TEXT = await get_result_text(state_data)
    if state_data["photo"]:
        photo: types.PhotoSize = state_data["photo"]
        return await message.answer_photo(
            photo=photo.file_id,
            caption=RESULT_TEXT,
            reply_markup=builder.as_markup()
        )
    await message.answer(RESULT_TEXT, reply_markup=builder.as_markup())