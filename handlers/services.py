from aiogram import types
from aiogram.fsm.context import FSMContext
from functools import wraps


def reset_state_on_error(func):
    @wraps(func)
    async def wrapper(call: types.CallbackQuery = None, message: types.Message = None, **kwargs):
        try:
            return await func(call=call, message=message, **kwargs)
        except Exception as e:
            # Reset state on error
            state: FSMContext = kwargs.get("state")
            if state:
                await state.finish()
            # Handle or log the error as needed
            print(f"Error occurred: {e}")
            # Re-raise the error if needed
            raise
    return wrapper
