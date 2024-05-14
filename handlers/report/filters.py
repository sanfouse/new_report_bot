from aiogram import types
from aiogram.filters import Filter
from .services import FormatChecker
from enum import Enum


class FormatType(str, Enum):
    date = "date"
    time = "time"
    email = "email"


class FormatFilter(Filter):
    def __init__(self, format_type: FormatType) -> None:
        self.format_type = format_type

    async def __call__(self, message: types.Message):
        flag = False
        
        if message.content_type != 'text':
            return False
        text = message.text

        match self.format_type:
            case FormatType.date.value:
                flag = FormatChecker.check_date_format(text)
            case FormatType.time.value:
                flag = FormatChecker.check_time_format(text)
            case FormatType.email.value:
                flag = FormatChecker.check_email_format(text)

        if not flag:
            await message.answer("Некорректный формат. Пожалуйста, введите данные в корректном формате.")
        return flag
        