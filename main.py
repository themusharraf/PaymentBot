import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram import types
from aiogram.filters.command import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import TOKEN
from payments import order1, pre_checkout_query, successful_payment

dp = Dispatcher()

inline_btn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="To'lov tizimi", callback_data="Tolov")]
])


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f"Assalomu Aleykum. Xurmatli {message.from_user.full_name}! botimizga xush kelibsiz 👋",
                         reply_markup=inline_btn)


dp.callback_query.register(order1, F.data == "Tolov")
dp.pre_checkout_query.register(pre_checkout_query)
dp.message.register(successful_payment, F.successful_payment)


async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
