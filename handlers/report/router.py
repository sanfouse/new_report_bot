from aiogram import F, Router, types
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext

import text
from keyboards.actions import ActionStart
from keyboards.report.actions import ActionChoicePlatform
from keyboards.report.callbacks import (СhoicePlatformCallback,
                                        СhoiceSuccesCallback)
from keyboards.report.inline import choice_answer_platform_keyboard
from states.default import Report

from .services import get_email_result_text, show_result_text
from .filters import FormatFilter
from mailer import sender

router = Router()


@router.message(StateFilter(Report.route_number))
async def route_number(message: types.Message, state: FSMContext):
    await state.update_data(route_number=message.text, username=message.from_user.username)
    await message.answer(text.DATE_TEXT)
    await state.set_state(Report.date)


@router.message(StateFilter(Report.date), FormatFilter())
async def date(message: types.Message, state: FSMContext):
    await state.update_data(date=message.text, email="")
    await message.answer(text.TIME_TEXT)
    await state.set_state(Report.time)


@router.message(StateFilter(Report.time), FormatFilter())
async def time(message: types.Message, state: FSMContext):
    await state.update_data(time=message.text)
    await message.answer(text.CAR_NUMBERS_TEXT)
    await state.set_state(Report.car_numbers)


@router.message(StateFilter(Report.car_numbers))
async def car_numbers(message: types.Message, state: FSMContext):
    await state.update_data(car_numbers=message.text)
    await message.answer(text.ROUTE_TEXT)
    await state.set_state(Report.route)


@router.message(StateFilter(Report.route))
async def route(message: types.Message, state: FSMContext):
    await state.update_data(route=message.text)
    await message.answer(text.REPORT_TEXT)
    await state.set_state(Report.report)


@router.message(StateFilter(Report.report))
async def report(message: types.Message, state: FSMContext):
    builder = await choice_answer_platform_keyboard()
    await state.update_data(
            report=message.text,
            photo=message.photo[-1] if message.photo else None
        )
    if message.photo:
        await message.bot.download(
                file=message.photo[-1].file_id,
                destination=f"media/{message.photo[-1].file_id}.png"
            )
    await message.answer(text.CHOICE_PLATFORM_TEXT, reply_markup=builder.as_markup())
    await state.set_state(Report.choice_platform)


@router.callback_query(
        StateFilter(Report.choice_platform),
        СhoicePlatformCallback.filter(F.action == ActionChoicePlatform.email)
    )
async def choice_platform_email(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer(
        text.EMAIL_TEXT
    )
    await state.set_state(Report.email)


@router.callback_query(
        StateFilter(Report.choice_platform),
        СhoicePlatformCallback.filter(F.action == ActionChoicePlatform.telegram)
    )
async def choice_platform_telegram(call: types.CallbackQuery, state: FSMContext):
    await show_result_text(call.message, state)


@router.message(StateFilter(Report.email), FormatFilter())
async def email(message: types.Message, state: FSMContext):
    await state.update_data(email=message.text)
    await show_result_text(message, state)


@router.callback_query(
            StateFilter(Report), 
            СhoiceSuccesCallback.filter(F.action == ActionStart.start)
        )
async def finish_report(call: types.CallbackQuery, state: FSMContext):
    state_data = await state.get_data()
    body = await get_email_result_text(state_data)
    sender.send_email(
            body=body, 
            photo_data=f"media/{state_data['photo'].file_id}.png" 
            if state_data["photo"] else None
        )
    await call.message.answer(text.SUCCES_TEXT)
    await state.clear()