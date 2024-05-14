import asyncio
from aiogram import Bot, Dispatcher
from handlers import commands, report
from config import settings
from aiogram.enums.parse_mode import ParseMode
from aiogram.client.bot import DefaultBotProperties
from aiogram.fsm.storage.redis import RedisStorage

bot = Bot(
    token=settings.BOT_TOKEN, default=DefaultBotProperties(
        parse_mode=ParseMode.HTML, )
)
dp = Dispatcher(storage=RedisStorage.from_url(settings.REDIS_URL))


async def main():
    dp.include_routers(commands.commands_router)
    dp.include_routers(report.report_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
