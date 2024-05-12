from aiogram import F, Router, types
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext

from keyboards.actions import ActionStart
from keyboards.callbacks import СhoiceCallback
from keyboards.commands.inline import command_start_keyboard
from keyboards.report.callbacks import СhoiceSuccesCallback
from states.default import Report
from text import ROUTE_NUMBER_TEXT, START_TEXT

from .services import cancel_and_clear_state

router = Router()


@router.message(CommandStart())
async def start_message(message: types.Message) -> None:
    builder = await command_start_keyboard()
    await message.answer(
        START_TEXT.format(message.from_user.full_name),
        reply_markup=builder.as_markup()
    )


@router.message(Command("cancel"))
async def command_cancel(message: types.Message, state: FSMContext):
    await cancel_and_clear_state(message, state)


@router.callback_query(СhoiceCallback.filter(F.action == ActionStart.cancel))
async def callback_cancel(call: types.CallbackQuery, state: FSMContext):
    await cancel_and_clear_state(call.message, state)


@router.callback_query(СhoiceSuccesCallback.filter(F.action == ActionStart.cancel))
async def callback_cancel(call: types.CallbackQuery, state: FSMContext):
    await cancel_and_clear_state(call.message, state)


@router.callback_query(СhoiceCallback.filter(F.action == ActionStart.start))
async def start_report(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer(ROUTE_NUMBER_TEXT)
    await state.set_state(Report.route_number)
