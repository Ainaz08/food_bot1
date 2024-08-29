from aiogram import Bot, Dispatcher, types, executor
from config import token
from logging import basicConfig, INFO

bot = Bot(token='7060288127:AAFIqP6HL1siXQuJohVZu6sAEyO3ymAgY_A')
dp = Dispatcher(bot)
basicConfig(level=INFO)

# @dp.message_handler(commands='start')
# async def start(message:types.Message):
#     await message.answer("Здравствуйте, клиент!")

start_buttons = [
    types.KeyboardButton('О нас'),
    types.KeyboardButton('Товары'),
    types.KeyboardButton('Заказать'),
    types.KeyboardButton('Контакты'),
]

start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_buttons)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer(f'Здравствуйте,  {message.from_user.full_name}!', reply_markup=start_keyboard)

@dp.message_handler(text='О нас')
async def about_us(message:types.Message):
    await message.reply("tehno_shop — это  интернет магазин по продаже различных смартфонов")

@dp.message_handler(text='Контакты')
async def contact(message:types.Message):
    await message.answer(f'{message.from_user.full_name}, вот нащи контакты: ')
    await message.answer_contact("+996708424268", "Ainaz", "Mamatisa kyzy")
    await message.answer_contact("+996558620037", "Alisher", "Mamatisa uulu")

@dp.message_handler(text="Заказать")
async def order(message:types.Message):
    button = types.KeyboardButton("Отправить контакт", request_contact=True)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(button)
    await message.answer("Пожалуйста отправьте свой контакт", reply_markup=keyboard)

@dp.message_handler(content_types=types.ContentType.CONTACT)
async def get_contact(message:types.Message):
    # await message.answer(message)
    await bot.send_message(6490369099, f'Новый заказ:\nИмя: {message.contact.first_name}\nФамилия: {message.contact.last_name}\nUsername пользователя: {message.from_user.username}\nТелефон: {message.contact.phone_number}\n')
    await message.answer("Спасибо что зделали заказ\nМы свяжемся с вами в скором времени!")
    await start(message)


course = [
    types.KeyboardButton("Apple"),
    types.KeyboardButton("Samsung"),
    types.KeyboardButton("Xiaomi"),
    types.KeyboardButton("Google"),
    types.KeyboardButton("POCO"),  
    types.KeyboardButton("Oppo"),
    types.KeyboardButton("Назад")    
]

courses_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*course)

@dp.message_handler(text='Товары')
async def about(message: types.Message):
    await message.answer("Вот наши товары:", reply_markup=courses_keyboard)

@dp.message_handler(text="Назад")
async def back_start(message:types.Message):
    await start(message)

@dp.message_handler(text='Samsung')
async def back(message:types.Message):
    await message.reply("""https://www.google.com/imgres?q=%D1%82%D0%B5%D0%BB%D0%B5%D1%84%D0%BE%D0%BD%20%D1%81%D0%B0%D0%BC%D1%81%D1%83%D0%BD%D0%B3%20%D0%B015&imgurl=https%3A%2F%2Flogin.kg%2Fimage%2Fcache%2Fcatalog%2Fnew%2FPhones%2FSamsung%2FA15%2F1-1200x800.jpg&imgrefurl=https%3A%2F%2Flogin.kg%2Fphones%2Fsamsung-galaxy-a15-4-128gb-eu&docid=ZhLaBBKG6OlHeM&tbnid=NvFV-m9BxLrJ8M&vet=12ahUKEwjUu6_5qraHAxWAAxAIHWxCNkkQM3oECG8QAA..i&w=1200&h=800&hcb=2&ved=2ahUKEwjUu6_5qraHAxWAAxAIHWxCNkkQM3oECG8QAA""")

    await message.answer("цена:15000")

@dp.message_handler(text='Apple')
async def back(message:types.Message):
    await message.reply("""https://www.google.com/imgres?q=apple%2015%20pro%20max&imgurl=https%3A%2F%2Fcdsassets.apple.com%2Flive%2F7WUAS350%2Fimages%2Ftech-specs%2Fiphone-15-pro-max.png&imgrefurl=https%3A%2F%2Fsupport.apple.com%2Fen-us%2F111828&docid=SZYZEpwwXeaQUM&tbnid=0lXvrGRkalUyyM&vet=12ahUKEwil4tr3q8GHAxUAFxAIHfp-Jp4QM3oECBgQAA..i&w=1000&h=1000&hcb=2&ved=2ahUKEwil4tr3q8GHAxUAFxAIHfp-Jp4QM3oECBgQAA""")

    await message.reply("цена: 117000")

@dp.message_handler(text='Xiaomi')
async def back(message:types.Message):
    await message.reply("""https://www.google.com/imgres?q=xiaomi%2014%20ultra&imgurl=https%3A%2F%2Fsoftech.kg%2Fimage%2Fcache%2F72776cda73625426690f9dd6f519701d.jpg&imgrefurl=https%3A%2F%2Fsoftech.kg%2Fsmartfon-xiaomi-14-ultra-12512&docid=owm8PbfAsZQYYM&tbnid=NM3gLz35SQChGM&vet=12ahUKEwiA942frcGHAxVSKhAIHXjuA6gQM3oECBkQAA..i&w=230&h=230&hcb=2&ved=2ahUKEwiA942frcGHAxVSKhAIHXjuA6gQM3oECBkQAA""")

    await message.reply("цена: 840000")

@dp.message_handler(text='Google')
async def back(message:types.Message):
    await message.reply("""https://www.google.com/imgres?q=google%20pixel%208%20pro&imgurl=https%3A%2F%2Flogin.kg%2Fimage%2Fcache%2Fcatalog%2Fnew%2FPhones%2FGoogle%2FPixel%25208%2520Pro%2F123-500x400.jpg&imgrefurl=https%3A%2F%2Flogin.kg%2Fphones%2Fgoogle-phones%2Fgoogle-pixel-8-pro-12-128gb-ca&docid=SUpjyGw0FwxQuM&tbnid=Ci38pyJen7tKbM&vet=12ahUKEwjTqqXwrsGHAxXSHXcKHbw0CbgQM3oECBwQAA..i&w=500&h=400&hcb=2&ved=2ahUKEwjTqqXwrsGHAxXSHXcKHbw0CbgQM3oECBwQAA""")

    await message.reply("цена: 140000")

@dp.message_handler(text='POCO')
async def back(message:types.Message):
    await message.reply("""https://www.google.com/imgres?q=poco%20x3%20pro&imgurl=https%3A%2F%2Flogin.kg%2Fimage%2Fcache%2Fcatalog%2Fnew%2FPhones%2FXiaomi%2FPoco%2520X3%2520Pro%2F3-500x400.jpg&imgrefurl=https%3A%2F%2Flogin.kg%2Fphones%2Fxiaomi-poco-x3-pro-8256gb-eu&docid=_PkhvMD3i2GX0M&tbnid=AE9ghRWcaSMddM&vet=12ahUKEwiL86Hpr8GHAxVmIxAIHU2LPakQM3oECBcQAA..i&w=500&h=400&hcb=2&ved=2ahUKEwiL86Hpr8GHAxVmIxAIHU2LPakQM3oECBcQAA""")

    await message.reply("цена: 220000")

@dp.message_handler(text='Oppo')
async def back(message:types.Message):
    await message.reply("""https://www.google.com/imgres?q=oppo%20f17%20pro&imgurl=https%3A%2F%2Fimage.oppo.com%2Fcontent%2Fdam%2Foppo%2Fin%2Fmkt%2Fsmartphone%2Ff-series%2Ff17-pro%2Fproduct%2Fcolor.png&imgrefurl=https%3A%2F%2Fwww.oppo.com%2Fin%2Fsmartphones%2Fseries-f%2Ff17-pro%2Fspecs%2F&docid=5AxfVNJ3CK5ggM&tbnid=MbkrmZ0QHX2bTM&vet=12ahUKEwjrmfDpsMGHAxXGFxAIHbRWATQQM3oECHEQAA..i&w=1568&h=954&hcb=2&ved=2ahUKEwjrmfDpsMGHAxXGFxAIHbRWATQQM3oECHEQAA""")

    await message.reply("цена: 300000")

executor.start_polling(dp, skip_updates=True) 




