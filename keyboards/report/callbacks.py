from aiogram.filters.callback_data import CallbackData

from keyboards.actions import ActionStart
from .actions import ActionChoicePlatform

class СhoicePlatformCallback(CallbackData, prefix='choice_platform'):
    action: ActionChoicePlatform


class СhoiceSuccesCallback(CallbackData, prefix='choice_is_succes'):
    action: ActionStart