from aiogram.utils.keyboard import InlineKeyboardBuilder
from keyboards.actions import ActionStart
from keyboards.callbacks import СhoiceCallback


async def command_start_keyboard() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()

    for action in ActionStart:
        builder.button(
            text=action.value,
            callback_data=СhoiceCallback(action=action),
        )

    return builder
