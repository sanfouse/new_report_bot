from enum import Enum


class ActionChoicePlatform(str, Enum):
    telegram = 'Телеграм'
    email = 'Почта'


class ActionResult(str, Enum):
    start = 'Начать'
    cancel = 'Отмена'
