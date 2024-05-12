from aiogram.utils.keyboard import InlineKeyboardBuilder

from keyboards.actions import ActionStart
from .actions import ActionChoicePlatform
from .callbacks import СhoicePlatformCallback, СhoiceSuccesCallback

async def choice_answer_platform_keyboard() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()

    for action in ActionChoicePlatform:
        builder.button(
            text=action.value,
            callback_data=СhoicePlatformCallback(action=action),
        )

    return builder


async def command_finish_keyboard() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()

    for action in ActionStart:
        builder.button(
            text=action.value,
            callback_data=СhoiceSuccesCallback(action=action),
        )

    return builder