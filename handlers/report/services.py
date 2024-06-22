import re

from aiogram import types
from aiogram.fsm.context import FSMContext

import text
from keyboards.report.inline import command_finish_keyboard
from utils.photo import Photo


class ResultHandler:
    @staticmethod
    async def get_result_text(data: dict, is_email: bool = False) -> str:
        template = text.EMAIL_RESULT_TEXT if is_email else text.RESULT_TEXT
        return template.format(
            data['route_number'],
            data['date'],
            data['time'],
            data['route'],
            data['car_numbers'],
            data['report'],
            data['email'],
            data["username"]
        )

    @classmethod
    async def show_result_text(
        cls, message: types.Message, state: FSMContext, is_email: bool = False
    ):
        state_data = await state.get_data()
        builder = await command_finish_keyboard()
        RESULT_TEXT = await cls.get_result_text(state_data, is_email)
        photo: Photo = state_data.get("photo")
        if photo:
            return await message.answer_photo(
                photo=photo.file_id,
                caption=RESULT_TEXT,
                reply_markup=builder.as_markup()
            )
        await message.answer(RESULT_TEXT, reply_markup=builder.as_markup())


class FormatChecker:
    @staticmethod
    def check_time_format(input_time):
        pattern = re.compile("(24:00|2[0-3]:[0-5][0-9]|[0-1][0-9]:[0-5][0-9])")
        return bool(re.match(pattern, input_time))

    @staticmethod
    def check_date_format(input_date):
        pattern = re.compile(r'^\d{1,2}\.\d{1,2}\.\d{4}$')
        return bool(re.match(pattern, input_date))

    @staticmethod
    def check_email_format(email):
        pattern = re.compile(
            r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        return bool(re.match(pattern, email))
