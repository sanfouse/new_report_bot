from aiogram.fsm.state import StatesGroup, State

class Report(StatesGroup):
    route_number = State()
    date = State()
    time = State()
    car_numbers = State()
    route = State()
    report = State()
    email = State()
    choice_platform = State()
    finish = State()
