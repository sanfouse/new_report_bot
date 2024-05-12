from aiogram import types
from aiogram.filters import Filter
from .services import FormatChecker

class FormatFilter(Filter):
    async def __call__(self, message: types.Message):
        if message.content_type != 'text':
            return False
        
        text = message.text

        if FormatChecker.check_time_format(text):
            return True
        elif FormatChecker.check_date_format(text):
            return True
        elif FormatChecker.check_email_format(text):
            return True
        else:
            await message.answer("Некорректный формат. Пожалуйста, введите данные в корректном формате.")
            return False