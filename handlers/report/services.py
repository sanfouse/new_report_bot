import text
from aiogram import types
from aiogram.fsm.context import FSMContext
from keyboards.report.inline import command_finish_keyboard
import re

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


class FormatChecker:
    @staticmethod
    def check_time_format(input_time):
        pattern = re.compile(r'^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$')
        return bool(re.match(pattern, input_time))

    @staticmethod
    def check_date_format(input_date):
        pattern = re.compile(r'^\d{2}\.\d{2}\.\d{4}$')
        return bool(re.match(pattern, input_date))

    @staticmethod
    def check_email_format(email):
        pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        return bool(re.match(pattern, email))