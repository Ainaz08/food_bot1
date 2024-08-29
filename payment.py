from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import LabeledPrice, PreCheckoutQuery,CallbackQuery, BotCommand
# from aiogram.dispatcher.storage import FSMContext
# from aiogram.utils.helper import Helper, HelperMode, ListItem
# from aiogram.utils.callback_data import CallbackData
# from aiogram.dispatcher.filters.state import State, StatesGroup
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup
from config import token, pay_token
import logging

bot = Bot(token=token)
db = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

buy_loptop_cd = CallbackData('buy','item_id')

@db.message_handlers(commands=['start'])
async def starts(massage):
    Keyboard = InlineKeyboardMarkup()
    Keyboard.add(InlineKeyboardButton(text='Купить ноутбук', callback_data=buy_loptop_cd.new(item_id = 'laptop')))
    await massage.reply("Привет выбери товар для покупки", reply_markup=Keyboard)

@db.callback_query_handler(buy_laptop_cb.filter(item_id = 'laptop'))
async def process_payment(callback: CallbackQuery):
    price = [LabeledPrice(label='HP Victus', amount=70000.00)]

    await bot.send_invoice()
        (chat_id=callback.from_user.id,
        title='Ноутбук',
        payload='laptop',
        description="Ноутбук HP VICTUS 15-fa0033dx Intel Core i5-12450H "
                    "(3.30-4.40GHz) 16GB DDR4,512GB SSD M.2 NVMe, "
                    "NVIDIA GTX 1650 4GB GDDR6,15.6\" FHD(1920x1080) 144Hz IPS,"
                    "WiFi a/b/g/n/ac, BT 5.0, HD WC, CR, Win11, MicaSilver "
                    "(68U87UA#ABA)",
        provider_token=pay_token,
        currency='RUB',
        prices=price,
        start_parameter='test_bot',
        photo_url='https://www.ultra.kg/upload/resize_cache/iblock/abb/'
                  '1000_1000_1d0e97e446f4386989a06dbd5311ca67/abb3c70230d3f06655fa949510ad6426.jpg',
        photo_height=512,
        photo_size=512
        photo_width=512,
        need_name=True,
        need_phone_number=True,
        need_email=True,
        need_shipping_address=False,
        is_flexible=False
    )
    await callback.answer()

@db.pre_checkout_query_handler(lambda query : True)
async def pre(pre: PreCheckoutQuery):
    await bot.answer_callback_query(pre.id, ok=True)

@db.massage_hangler(content_tupes=types.ContentType.SUCCESSFUL_PAYMENT)
async def suc(massage:types.Massage):
    await massage.reply("Спасибо за покупку")

executor.start_polling(db, skip_updates=True)
