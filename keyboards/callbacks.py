from aiogram.filters.callback_data import CallbackData
from keyboards.actions import ActionStart

class СhoiceCallback(CallbackData, prefix='choice'):
    action: ActionStart