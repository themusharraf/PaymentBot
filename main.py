import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram import types
from aiogram.filters.command import Command
from aiogram.types import PreCheckoutQuery

from config import Token, Payment_Token

dp = Dispatcher()

PRICE = types.LabeledPrice(label='Настоящая Машина Времени', amount=4200000)


@dp.message(Command("start"))
async def process_buy_command(message: types.Message, bot: Bot):
    await bot.send_invoice(message.chat.id,
                           title="iPhone 14 Pro",
                           description="iPhone 14 Pro max 256GB Deep Purple Smartfoni",
                           provider_token=Payment_Token,
                           currency='UZS',
                           photo_url="https://images.uzum.uz/ck9sgvbk9fq1var6o9h0/original.jpg",
                           photo_height=512,
                           photo_width=512,
                           photo_size=512,
                           is_flexible=False,
                           prices=[PRICE],
                           start_parameter='time-machine-example',
                           payload='some-invoice-payload-for-our-internal-use'
                           )


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment(message: types.Message, bot: Bot):
    msg = f"""
To'lov muvaffaqiyatli amalga oshirildi ✅
Maxsulot nomi : {message.successful_payment.invoice_payload}
Summa: {message.successful_payment.total_amount // 100} {message.successful_payment.currency} 💸
Menejerimiz so'rovingizni oldi va allaqachon sizga termoqda 💻
"""

    await message.answer(msg)


async def main() -> None:
    bot = Bot(token=Token)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
