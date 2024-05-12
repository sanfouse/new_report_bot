from enum import Enum

class ActionStart(str, Enum):
    start = 'Да'
    cancel = 'Отмена'
    

class ActionCancel(str, Enum):
    cancel = 'Отмена'


