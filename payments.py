from aiogram import Bot, types
from aiogram.types import LabeledPrice, PreCheckoutQuery
from config import PAYMENT_TOKEN


async def order1(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="iPhone 14 Pro",
                           description="iPhone 14 Pro max 256GB Deep Purple Smartfoni",
                           provider_token=PAYMENT_TOKEN,
                           currency='UZS',
                           photo_url="https://images.uzum.uz/ck9sgvbk9fq1var6o9h0/original.jpg",
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Narxi", amount=160_000_00),
                               LabeledPrice(label="QQS", amount=19_200_00),
                               LabeledPrice(label="Skidka", amount=-30_200_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='some-invoice-payload-for-our-internal-use',
                           request_timeout=15
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
