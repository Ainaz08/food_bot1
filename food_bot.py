# import telebot
# from telebot import types

# # Ваш токен
# TOKEN = '7545140888:AAEItO0WOZaX4BKBaLOPuf2O1QaoRvvaWts'
# bot = telebot.TeleBot(TOKEN)

# # Обработчик команды /start
# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     menu_button = types.KeyboardButton("Меню")
#     location_button = types.KeyboardButton("Локация")
#     about_button = types.KeyboardButton("О нас")
#     markup.add(menu_button, location_button, about_button)
#     bot.send_message(message.chat.id, "Добро пожаловать в FoodBot! Выберите опцию:", reply_markup=markup)

# # Обработчик для кнопки "Меню"
# @bot.message_handler(regexp="Меню")
# def show_menu(message):
#     markup = types.InlineKeyboardMarkup()
    
#     plov_button = types.InlineKeyboardButton("Плов Узбекский - 500с", url="https://www.google.com/imgres?q=%D1%83%D0%B7%D0%B1%D0%B5%D0%BA%D1%81%D0%BA%D0%B8%D0%B9%20%D0%BF%D0%BB%D0%BE%D0%B2&imgurl=https%3A%2F%2Fimages.unian.net%2Fphotos%2F2022_10%2Fthumb_files%2F1200_0_1666194211-5378.jpg&imgrefurl=https%3A%2F%2Fwww.unian.net%2Frecipes%2Fsecond-courses%2Fside-dishes%2Fnastoyashchiy-uzbekskiy-nazvan-glavnyy-sekret-rassypchatogo-plova-12017058.html")
#     shashlik_button = types.InlineKeyboardButton("Шашлык куринный - 450с", url="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.m2-shop.ru%2Frecipes%2Fshashlickuriniebedra&psig=AOvVaw0MdJPyMDQwNlutcJeqBsdH&ust=1725086778383000&source=images&cd=vfe&opi=89978449&ved=0CBMQjRxqFwoTCIilgJaPnIgDFQAAAAAdAAAAABAE")
#     samosa_button = types.InlineKeyboardButton("Самса - 65с", url="https://www.google.com/url?sa=i&url=https%3A%2F%2Fgrillweb.uz%2Freczepty%2Fpiczcza-i-pirogi%2Fuzbekskaya-samsa-na-grile%2F&psig=AOvVaw3hXK4Xe85K7TpWCAwP-Z70&ust=1725086858069000&source=images&cd=vfe&opi=89978449&ved=0CBMQjRxqFwoTCMjdgcCPnIgDFQAAAAAdAAAAABAE")
#     wings_button = types.InlineKeyboardButton("Крылышки 12шт - 500с", url="https://www.google.com/imgres?q=%D0%BA%D1%80%D1%8B%D0%BB%D1%8B%D1%88%D0%BA%D0%B8&imgurl=https%3A%2F%2Fhalal-spb.ru%2Fsites%2Fdefault%2Ffiles%2Fstyles%2Flarge%2Fpublic%2Fkrylyshki-kak-v-kfs-recept.jpg%3Fitok%3DYzgzaRNX&imgrefurl=https%3A%2F%2Fhalal-spb.ru%2Frecipe%2Fkurinye-krylyshki-kfc&docid=vFKknR4gMfg2FM&tbnid=mIzxXXRcWn1G8M&vet=12ahUKEwjIjoyWkJyIAxUeJxAIHYAbFeAQM3oFCIcBEAA..i&w=700&h=467&hcb=2&ved=2ahUKEwjIjoyWkJyIAxUeJxAIHYAbFeAQM3oFCIcBEAA")
#     shawarma_button = types.InlineKeyboardButton("Шаурма - 270с", url="https://www.google.com/imgres?q=%D1%88%D0%B0%D1%83%D1%80%D0%BC%D0%B0%20%D1%86%D0%B5%D0%BD%D0%B0%20%D0%BA%D0%B0%D1%84%D0%B5&imgurl=https%3A%2F%2Flookaside.fbsbx.com%2Flookaside%2Fcrawler%2Fmedia%2F%3Fmedia_id%3D100067684224848&imgrefurl=https%3A%2F%2Fwww.facebook.com%2Fdostavka.shaurma.plov.lagman%2F&docid=AzdyFIR6oGRUPM&tbnid=FKf7gHNLW4rG5M&vet=12ahUKEwjemLeLkZyIAxXSJhAIHahsAAIQM3oECCsQAA..i&w=1191&h=601&hcb=2&ved=2ahUKEwjemLeLkZyIAxXSJhAIHahsAAIQM3oECCsQAA")
#     burger_button = types.InlineKeyboardButton("Бургер - 300с", url="https://www.google.com/imgres?q=%20%D0%B1%D1%83%D1%80%D0%B3%D0%B5%D1%80%20%D1%86%D0%B5%D0%BD%D0%B0%20%D0%BA%D0%B0%D1%84%D0%B5&imgurl=https%3A%2F%2Fsxodim.com%2Fuploads%2Fimages%2F2022%2F11%2F11%2Foptimized%2Fbeff18152003115708dc2a06510b2f73_800xauto-q-85.jpg&imgrefurl=https%3A%2F%2Fsxodim.com%2Fbishkek%2Farticle%2Fgde-v-bishkeke-poest-vkusnye-burgery&docid=1wGBKUQ1gjORLM&tbnid=C3VfFrJz-yscOM&vet=12ahUKEwjD87u1kZyIAxVKFBAIHZFlKRsQM3oECB0QAA..i&w=800&h=533&hcb=2&ved=2ahUKEwjD87u1kZyIAxVKFBAIHZFlKRsQM3oECB0QAA")
    
#     back_button = types.InlineKeyboardButton("Назад", callback_data="back")

#     markup.add(plov_button, shashlik_button, samosa_button, wings_button, shawarma_button, burger_button, back_button)
#     bot.send_message(message.chat.id, "Меню:", reply_markup=markup)

# # Обработчик для кнопки "Локация"
# @bot.message_handler(regexp="Локация")
# def show_location(message):
#     bot.send_message(message.chat.id, "Мы находимся по адресу:\nМасалиева 100, Ош, Кыргызстан")


# # Обработчик для кнопки "О нас"
# @bot.message_handler(regexp="О нас")
# def about_us(message):
#     bot.send_message(message.chat.id, "Мы онлайн магазин еды. Вы можете заказать что есть в меню. Мы готовим вашу еду, и вы можете забрать её.")

# # Обработчик для кнопки "Назад"
# @bot.callback_query_handler(func=lambda call: call.data == "back")
# def back_to_menu(call):
#     start(call.message)

# # Запуск бота
# bot.polling(none_stop=True)





# import telebot
# from telebot import types

# # Ваш токен
# TOKEN = '7545140888:AAEItO0WOZaX4BKBaLOPuf2O1QaoRvvaWts'
# bot = telebot.TeleBot(TOKEN)

# # Обработчик команды /start
# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     menu_button = types.KeyboardButton("Меню")
#     location_button = types.KeyboardButton("Локация")
#     about_button = types.KeyboardButton("О нас")
#     markup.add(menu_button, location_button, about_button)
#     bot.send_message(message.chat.id, "Добро пожаловать в FoodBot! Выберите опцию:", reply_markup=markup)

# # Обработчик для кнопки "Меню"
# @bot.message_handler(regexp="Меню")
# def show_menu(message):
#     markup = types.InlineKeyboardMarkup()
    
#     plov_button = types.InlineKeyboardButton("Плов Узбекский - 500с", url="https://images.unian.net/photos/2022_10/thumb_files/1200_0_1666194211-5378.jpg")
#     shashlik_button = types.InlineKeyboardButton("Шашлык куринный - 450с", url="https://www.m2-shop.ru/recipes/shashlickuriniebedra")
#     samosa_button = types.InlineKeyboardButton("Самса - 65с", url="https://grillweb.uz/reczepty/piczcza-i-pirogi/uzbekskaya-samsa-na-grile")
#     wings_button = types.InlineKeyboardButton("Крылышки 12шт - 500с", url="https://halal-spb.ru/sites/default/files/styles/large/public/krylyshki-kak-v-kfs-recept.jpg")
#     shawarma_button = types.InlineKeyboardButton("Шаурма - 270с", url="https://lookaside.fbsbx.com/lookaside/crawler/media/?media_id=100067684224848")
#     burger_button = types.InlineKeyboardButton("Бургер - 300с", url="https://sxodim.com/uploads/images/2022/11/11/optimized/beff18152003115708dc2a06510b2f73_800xauto-q-85.jpg")
    
#     back_button = types.InlineKeyboardButton("Назад", callback_data="back")

#     markup.add(plov_button, shashlik_button, samosa_button, wings_button, shawarma_button, burger_button, back_button)
#     bot.send_message(message.chat.id, "Меню:", reply_markup=markup)

# # Обработчик для кнопки "Локация"
# @bot.message_handler(regexp="Локация")
# def show_location(message):
#     bot.send_message(message.chat.id, "Мы находимся по адресу:\nМасалиева 100, Ош, Кыргызстан")

# # Обработчик для кнопки "О нас"
# @bot.message_handler(regexp="О нас")
# def about_us(message):
#     bot.send_message(message.chat.id, "Мы онлайн магазин еды. Вы можете заказать что есть в меню. Мы готовим вашу еду, и вы можете забрать её.")

# # Обработчик для кнопки "Назад"
# @bot.callback_query_handler(func=lambda call: call.data == "back")
# def back_to_menu(call):
#     start(call.message)

# # Запуск бота
# bot.polling(none_stop=True)




# import telebot
# from telebot import types

# # Ваш токен
# TOKEN = '7545140888:AAEItO0WOZaX4BKBaLOPuf2O1QaoRvvaWts'
# bot = telebot.TeleBot(TOKEN)

# # Обработчик команды /start
# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     menu_button = types.KeyboardButton("Меню")
#     location_button = types.KeyboardButton("Локация")
#     about_button = types.KeyboardButton("О нас")
#     order_button = types.KeyboardButton("Заказать")
#     markup.add(menu_button, location_button, about_button, order_button)
#     bot.send_message(message.chat.id, "Добро пожаловать в FoodBot! Выберите опцию:", reply_markup=markup)

# # Обработчик для кнопки "Меню"
# @bot.message_handler(regexp="Меню")
# def show_menu(message):
#     menu_text = """
#     📋 Меню:
    
#     1. Плов Узбекский - 500с
#     2. Шашлык куринный - 450с
#     3. Самса - 65с
#     4. Крылышки (12 шт) - 500с
#     5. Шаурма - 270с
#     6. Бургер - 300с
#     """
#     bot.send_message(message.chat.id, menu_text)

# # Обработчик для кнопки "Локация"
# @bot.message_handler(regexp="Локация")
# def show_location(message):
#     bot.send_location(message.chat.id, latitude=40.5235, longitude=72.8003)
#     bot.send_message(message.chat.id, "Мы находимся по адресу:\nМасалиева 100, Ош, Кыргызстан")

# # Обработчик для кнопки "О нас"
# @bot.message_handler(regexp="О нас")
# def about_us(message):
#     about_text = """
#     🛒 О нас:
    
#     Мы онлайн магазин еды. Вы можете заказать блюда, указанные в меню. Мы готовим вашу еду, и вы можете забрать её по нашему адресу или оформить доставку.
#     """
#     bot.send_message(message.chat.id, about_text)

# # Обработчик для кнопки "Заказать"
# @bot.message_handler(regexp="Заказать")
# def order_food(message):
#     contact_markup = types.InlineKeyboardMarkup()
#     call_button = types.InlineKeyboardButton(text="Позвонить", url="tel:+996708424268")
#     contact_markup.add(call_button)
#     bot.send_message(message.chat.id, "Свяжитесь с нами для заказа:\nМаматиса кызы Айназ\n📞 0708 424 268", reply_markup=contact_markup)

# # Запуск бота
# bot.polling(none_stop=True)











# from telegram import Update, ParseMode
# from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, InlineKeyboardButton, InlineKeyboardMarkup
# from telegram import InputLocationMessageContent

# # Токен вашего бота
# TOKEN = '7545140888:AAEItO0WOZaX4BKBaLOPuf2O1QaoRvvaWts'

# def start(update: Update, context: CallbackContext):
#     keyboard = [
#         [InlineKeyboardButton("Меню", callback_data='menu')],
#         [InlineKeyboardButton("Локация", callback_data='location')],
#         [InlineKeyboardButton("О нас", callback_data='about')],
#         [InlineKeyboardButton("Заказать", callback_data='order')],
#         [InlineKeyboardButton("Доставка", callback_data='delivery')]
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)
#     update.message.reply_text('Добро пожаловать! Выберите опцию:', reply_markup=reply_markup)

# def button(update: Update, context: CallbackContext):
#     query = update.callback_query
#     data = query.data

#     if data == 'menu':
#         menu_keyboard = [
#             [InlineKeyboardButton("Плов Узбекский - 500с", callback_data='plov')],
#             [InlineKeyboardButton("Шашлык куриный - 450с", callback_data='shashlyk')],
#             [InlineKeyboardButton("Самса - 65с/шт", callback_data='samsa')],
#             [InlineKeyboardButton("Крылышки - 500с/12шт", callback_data='krylyshki')],
#             [InlineKeyboardButton("Шаурма - 270с", callback_data='shaurma')],
#             [InlineKeyboardButton("Бургер - 300с", callback_data='burger')],
#             [InlineKeyboardButton("Назад", callback_data='back')]
#         ]
#         reply_markup = InlineKeyboardMarkup(menu_keyboard)
#         query.edit_message_text(text="Выберите блюдо:", reply_markup=reply_markup)

#     elif data == 'plov':
#         query.edit_message_text(text="Плов Узбекский\nЦена: 500с\nФото: [Плов Узбекский](https://www.google.com/imgres?q=%D1%83%D0%B7%D0%B1%D0%B5%D0%BA%D1%81%D0%BA%D0%B8%D0%B9%20%D0%BF%D0%BB%D0%BE%D0%B2&imgurl=https%3A%2F%2Fimages.unian.net%2Fphotos%2F2022_10%2Fthumb_files%2F1200_0_1666194211-5378.jpg&imgrefurl=https%3A%2F%2Fwww.unian.net%2Frecipes%2Fsecond-courses%2Fside-dishes%2Fnastoyashchiy-uzbekskiy-nazvan-glavnyy-sekret-rassypchatogo-plova-12017058.html)")

#     # Аналогично добавьте обработчики для других меню и функций

#     elif data == 'location':
#         query.edit_message_text(text="📍 Локация: Масалиева 100, Ош, Кыргызстан")
#         context.bot.send_location(chat_id=update.effective_chat.id, latitude=40.5157, longitude=72.0638)

#     elif data == 'about':
#         query.edit_message_text(text="🛒 О нас:\n\nМы онлайн магазин еды. Вы можете заказать блюда, указанные в меню. Мы готовим вашу еду, и вы можете забрать её по нашему адресу или оформить доставку.")

#     elif data == 'order':
#         query.edit_message_text(text="📞 Номер: 0708424268\n👤 Имя: Маматиса кызы Айназ")

#     elif data == 'delivery':
#         query.edit_message_text(text="Вы можете отправить своё местоположение, чтобы наш доставщик мог вас найти.")

#     elif data == 'back':
#         start(update, context)

# def main():
#     updater = Updater(TOKEN, use_context=True)
#     dp = updater.dispatcher

#     dp.add_handler(CommandHandler("start", start))
#     dp.add_handler(CallbackQueryHandler(button))

#     updater.start_polling()
#     updater.idle()

# if name == 'main':
#     main()

# bot.polling(none_stop=True)






# from telegram import Update, ParseMode
# from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, InlineKeyboardButton, InlineKeyboardMarkup
# from telegram import InputLocationMessageContent

# # Токен вашего бота
# TOKEN = '7545140888:AAEItO0WOZaX4BKBaLOPuf2O1QaoRvvaWts'

# def start(update: Update, context: CallbackContext):
#     keyboard = [
#         [InlineKeyboardButton("Меню", callback_data='menu')],
#         [InlineKeyboardButton("Локация", callback_data='location')],
#         [InlineKeyboardButton("О нас", callback_data='about')],
#         [InlineKeyboardButton("Заказать", callback_data='order')],
#         [InlineKeyboardButton("Доставка", callback_data='delivery')]
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)
#     update.message.reply_text('Добро пожаловать! Выберите опцию:', reply_markup=reply_markup)

# def button(update: Update, context: CallbackContext):
#     query = update.callback_query
#     data = query.data

#     if data == 'menu':
#         menu_keyboard = [
#             [InlineKeyboardButton("Плов Узбекский - 500с", callback_data='plov')],
#             [InlineKeyboardButton("Шашлык куриный - 450с", callback_data='shashlyk')],
#             [InlineKeyboardButton("Самса - 65с/шт", callback_data='samsa')],
#             [InlineKeyboardButton("Крылышки - 500с/12шт", callback_data='krylyshki')],
#             [InlineKeyboardButton("Шаурма - 270с", callback_data='shaurma')],
#             [InlineKeyboardButton("Бургер - 300с", callback_data='burger')],
#             [InlineKeyboardButton("Назад", callback_data='back')]
#         ]
#         reply_markup = InlineKeyboardMarkup(menu_keyboard)
#         query.edit_message_text(text="Выберите блюдо:", reply_markup=reply_markup)

#     elif data == 'plov':
#         query.edit_message_text(text="Плов Узбекский\nЦена: 500с\nФото: [Плов Узбекский](https://www.google.com/imgres?q=%D1%83%D0%B7%D0%B1%D0%B5%D0%BA%D1%81%D0%BA%D0%B8%D0%B9%20%D0%BF%D0%BB%D0%BE%D0%B2&imgurl=https%3A%2F%2Fimages.unian.net%2Fphotos%2F2022_10%2Fthumb_files%2F1200_0_1666194211-5378.jpg&imgrefurl=https%3A%2F%2Fwww.unian.net%2Frecipes%2Fsecond-courses%2Fside-dishes%2Fnastoyashchiy-uzbekskiy-nazvan-glavnyy-sekret-rassypchatogo-plova-12017058.html)")

#     # Аналогично добавьте обработчики для других меню и функций

#     elif data == 'location':
#         query.edit_message_text(text="📍 Локация: Масалиева 100, Ош, Кыргызстан")
#         context.bot.send_location(chat_id=update.effective_chat.id, latitude=40.5157, longitude=72.0638)

#     elif data == 'about':
#         query.edit_message_text(text="🛒 О нас:\n\nМы онлайн магазин еды. Вы можете заказать блюда, указанные в меню. Мы готовим вашу еду, и вы можете забрать её по нашему адресу или оформить доставку.")

#     elif data == 'order':
#         query.edit_message_text(text="📞 Номер: 0708424268\n👤 Имя: Маматиса кызы Айназ")

#     elif data == 'delivery':
#         query.edit_message_text(text="Вы можете отправить своё местоположение, чтобы наш доставщик мог вас найти.")

#     elif data == 'back':
#         start(update, context)

# def main():
#     updater = Updater(TOKEN, use_context=True)
#     dp = updater.dispatcher

#     dp.add_handler(CommandHandler("start", start))
#     dp.add_handler(CallbackQueryHandler(button))

#     updater.start_polling()
#     updater.idle()

# if  name == 'main':
#     main()

# import requests
# response = requests.get(f'https://api.telegram.org/bot{TOKEN}/getMe')
# print(response.json())
















# from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
# from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# # Токен вашего бота
# TOKEN = '7545140888:AAEItO0WOZaX4BKBaLOPuf2O1QaoRvvaWts'

# def start(update: Update, context: CallbackContext):
#     keyboard = [
#         [InlineKeyboardButton("Меню", callback_data='menu')],
#         [InlineKeyboardButton("Локация", callback_data='location')],
#         [InlineKeyboardButton("О нас", callback_data='about')],
#         [InlineKeyboardButton("Заказать", callback_data='order')],
#         [InlineKeyboardButton("Доставка", callback_data='delivery')]
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)
#     update.message.reply_text('Добро пожаловать! Выберите опцию:', reply_markup=reply_markup)

# def button(update: Update, context: CallbackContext):
#     query = update.callback_query
#     data = query.data

#     if data == 'menu':
#         menu_keyboard = [
#             [InlineKeyboardButton("Плов Узбекский - 500с", callback_data='plov')],
#             [InlineKeyboardButton("Шашлык куриный - 450с", callback_data='shashlyk')],
#             [InlineKeyboardButton("Самса - 65с/шт", callback_data='samsa')],
#             [InlineKeyboardButton("Крылышки - 500с/12шт", callback_data='krylyshki')],
#             [InlineKeyboardButton("Шаурма - 270с", callback_data='shaurma')],
#             [InlineKeyboardButton("Бургер - 300с", callback_data='burger')],
#             [InlineKeyboardButton("Назад", callback_data='back')]
#         ]
#         reply_markup = InlineKeyboardMarkup(menu_keyboard)
#         query.edit_message_text(text="Выберите блюдо:", reply_markup=reply_markup)
    
#     elif data == 'plov':
#         query.edit_message_text(text="Плов Узбекский\nЦена: 500с")
#         context.bot.send_photo(chat_id=update.effective_chat.id, photo='https://images.unian.net/photos/2022_10/thumb_files/1200_0_1666194211-5378.jpg')
    
#     elif data == 'shashlyk':
#         query.edit_message_text(text="Шашлык куриный\nЦена: 450с")
#         context.bot.send_photo(chat_id=update.effective_chat.id, photo='https://www.m2-shop.ru/recipes/shashlickuriniebedra')
    
#     elif data == 'samsa':
#         query.edit_message_text(text="Самса\nЦена: 65с/шт")
#         context.bot.send_photo(chat_id=update.effective_chat.id, photo='https://grillweb.uz/reczepty/piczcza-i-pirogi/uzbekskaya-samsa-na-grile/')
    
#     elif data == 'krylyshki':
#         query.edit_message_text(text="Крылышки\nЦена: 500с/12шт")
#         context.bot.send_photo(chat_id=update.effective_chat.id, photo='https://halal-spb.ru/sites/default/files/styles/large/public/krylyshki-kak-v-kfs-recept.jpg')
    
#     elif data == 'shaurma':
#         query.edit_message_text(text="Шаурма\nЦена: 270с")
#         context.bot.send_photo(chat_id=update.effective_chat.id, photo='https://lookaside.fbsbx.com/lookaside/crawler/media/?media_id=100067684224848')
    
#     elif data == 'burger':
#         query.edit_message_text(text="Бургер\nЦена: 300с")
#         context.bot.send_photo(chat_id=update.effective_chat.id, photo='https://sxodim.com/uploads/images/2022/11/11/optimized/beff18152003115708dc2a06510b2f73_800xauto-q-85.jpg')

#     elif data == 'location':
#         query.edit_message_text(text="📍 Локация: Масалиева 100, Ош, Кыргызстан")
#         context.bot.send_location(chat_id=update.effective_chat.id, latitude=40.5157, longitude=72.0638)

#     elif data == 'about':
#         query.edit_message_text(text="🛒 О нас:\n\nМы онлайн магазин еды. Вы можете заказать блюда, указанные в меню. Мы готовим вашу еду, и вы можете забрать её по нашему адресу или оформить доставку.")
    
#     elif data == 'order':
#         query.edit_message_text(text="📞 Номер: 0708424268\n👤 Имя: Маматиса кызы Айназ")
    
#     elif data == 'delivery':
#         query.edit_message_text(text="Вы можете отправить своё местоположение, чтобы наш доставщик мог вас найти.")

#     elif data == 'back':
#         start(update, context)

# def main():
#     updater = Updater(TOKEN, use_context=True)
#     dp = updater.dispatcher
#     dp.add_handler(CommandHandler('start', start))
#     dp.add_handler(CallbackQueryHandler(button))

#     updater.start_polling()
#     updater.idle()

# if name == 'main':
#     main()



















# from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, LabeledPrice, ShippingOption
# from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
# from telegram import ParseMode
# from telegram.error import TelegramError
# import logging

# # Установите ваш токен бота здесь
# TOKEN = '7545140888:AAEItO0WOZaX4BKBaLOPuf2O1QaoRvvaWts'

# # Включите логирование
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# def start(update: Update, context: CallbackContext) -> None:
#     keyboard = [
#         [InlineKeyboardButton("Меню", callback_data='menu')],
#         [InlineKeyboardButton("Локация", callback_data='location')],
#         [InlineKeyboardButton("О нас", callback_data='about')],
#         [InlineKeyboardButton("Заказать", callback_data='order')],
#         [InlineKeyboardButton("Доставка", callback_data='delivery')]
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)
#     update.message.reply_text('Добро пожаловать! Выберите опцию:', reply_markup=reply_markup)

# def button(update: Update, context: CallbackContext) -> None:
#     query = update.callback_query
#     query.answer()

#     if query.data == 'menu':
#         menu_keyboard = [
#             [InlineKeyboardButton("Плов Узбекский", callback_data='plov')],
#             [InlineKeyboardButton("Шашлык куринный", callback_data='shashlik')],
#             [InlineKeyboardButton("Самса", callback_data='samsa')],
#             [InlineKeyboardButton("Крылышки", callback_data='wings')],
#             [InlineKeyboardButton("Шаурма", callback_data='shawarma')],
#             [InlineKeyboardButton("Бургер", callback_data='burger')],
#             [InlineKeyboardButton("Назад", callback_data='start')]
#         ]
#         reply_markup = InlineKeyboardMarkup(menu_keyboard)
#         query.edit_message_text(text="Выберите блюдо:", reply_markup=reply_markup)

#     elif query.data == 'location':
#         query.edit_message_text(text="📍Локация: Масалиева 100, Ош, Кыргызстан\n\n[Открыть на карте](https://maps.google.com/?q=Масалиева+100,+Ош,+Кыргызстан)", parse_mode=ParseMode.MARKDOWN)

#     elif query.data == 'about':
#         query.edit_message_text(text="🛒 О нас:\n\nМы онлайн магазин еды. Вы можете заказать блюда, указанные в меню. Мы готовим вашу еду, и вы можете забрать её по нашему адресу или оформить доставку.")

#     elif query.data == 'order':
#         query.edit_message_text(text="📞 Номер: 0708424268\nИмя: Маматиса кызы Айназ\n\nВы можете сразу [позвонить](tel:+0708424268).")

#     elif query.data == 'delivery':
#         query.edit_message_text(text="Вы можете отправить своё местоположение, чтобы наш доставщик мог привезти ваш заказ.")

#     elif query.data == 'plov':
#         query.edit_message_text(text="Плов Узбекский - 500с\n\n![Плов Узбекский](https://www.unian.net/photos/2022_10/thumb_files/1200_0_1666194211-5378.jpg)")

#     elif query.data == 'shashlik':
#         query.edit_message_text(text="Шашлык куринный - 450с\n\n![Шашлык куринный](https://www.m2-shop.ru/recipes/shashlickuriniebedra)")

#     elif query.data == 'samsa':
#         query.edit_message_text(text="Самса - 65с за штуку\n\n![Самса](https://grillweb.uz/reczepty/piczcza-i-pirogi/uzbekskaya-samsa-na-grile/)")

#     elif query.data == 'wings':
#         query.edit_message_text(text="Крылышки - 500с (12 шт)\n\n![Крылышки](https://halal-spb.ru/sites/default/files/styles/large/public/krylyshki-kak-v-kfs-recept.jpg)")

#     elif query.data == 'shawarma':
#         query.edit_message_text(text="Шаурма - 270с\n\n![Шаурма](https://lookaside.fbsbx.com/lookaside/crawler/media/?media_id=100067684224848)")

#     elif query.data == 'burger':
#         query.edit_message_text(text="Бургер - 300с\n\n![Бургер](https://sxodim.com/uploads/images/2022/11/11/optimized/beff18152003115708dc2a06510b2f73_800xauto-q-85.jpg)")

#     elif query.data == 'start':
#         start(update, context)

# def main() -> None:
#     updater = Updater(TOKEN)

#     dispatcher = updater.dispatcher

#     dispatcher.add_handler(CommandHandler("start", start))
#     dispatcher.add_handler(CallbackQueryHandler(button))
#     updater.start_polling()
#     updater.idle()

# if  name == 'main':
#     main()
















# from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
# from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
# import logging

# # Установите ваш токен бота здесь
# TOKEN = '7545140888:AAEItO0WOZaX4BKBaLOPuf2O1QaoRvvaWts'

# # Включите логирование
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# def start(update: Update, context: CallbackContext) -> None:
#     keyboard = [
#         [InlineKeyboardButton("Меню", callback_data='menu')],
#         [InlineKeyboardButton("Локация", callback_data='location')],
#         [InlineKeyboardButton("О нас", callback_data='about')],
#         [InlineKeyboardButton("Заказать", callback_data='order')],
#         [InlineKeyboardButton("Доставка", callback_data='delivery')]
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)
#     update.message.reply_text('Добро пожаловать! Выберите опцию:', reply_markup=reply_markup)

# def button(update: Update, context: CallbackContext) -> None:
#     query = update.callback_query
#     query.answer()

#     if query.data == 'menu':
#         menu_keyboard = [
#             [InlineKeyboardButton("Плов Узбекский", callback_data='plov')],
#             [InlineKeyboardButton("Шашлык куринный", callback_data='shashlik')],
#             [InlineKeyboardButton("Самса", callback_data='samsa')],
#             [InlineKeyboardButton("Крылышки", callback_data='wings')],
#             [InlineKeyboardButton("Шаурма", callback_data='shawarma')],
#             [InlineKeyboardButton("Бургер", callback_data='burger')],
#             [InlineKeyboardButton("Назад", callback_data='start')]
#         ]
#         reply_markup = InlineKeyboardMarkup(menu_keyboard)
#         query.edit_message_text(text="Выберите блюдо:", reply_markup=reply_markup)

#     elif query.data == 'location':
#         query.edit_message_text(text="📍Локация: Масалиева 100, Ош, Кыргызстан\n\n[Открыть на карте](https://maps.google.com/?q=Масалиева+100,+Ош,+Кыргызстан)", parse_mode=ParseMode.MARKDOWN)

#     elif query.data == 'about':
#         query.edit_message_text(text="🛒 О нас:\n\nМы онлайн магазин еды. Вы можете заказать блюда, указанные в меню. Мы готовим вашу еду, и вы можете забрать её по нашему адресу или оформить доставку.")

#     elif query.data == 'order':
#         query.edit_message_text(text="📞 Номер: 0708424268\nИмя: Маматиса кызы Айназ\n\nВы можете сразу [позвонить](tel:+0708424268).")

#     elif query.data == 'delivery':
#         query.edit_message_text(text="Вы можете отправить своё местоположение, чтобы наш доставщик мог привезти ваш заказ.")

#     elif query.data == 'plov':
#         query.edit_message_text(text="Плов Узбекский - 500с\n\n![Плов Узбекский](https://images.unian.net/photos/2022_10/thumb_files/1200_0_1666194211-5378.jpg)")

#     elif query.data == 'shashlik':
#         query.edit_message_text(text="Шашлык куринный - 450с\n\n![Шашлык куринный](https://www.m2-shop.ru/recipes/shashlickuriniebedra)")

#     elif query.data == 'samsa':
#         query.edit_message_text(text="Самса - 65с за штуку\n\n![Самса](https://grillweb.uz/reczepty/piczcza-i-pirogi/uzbekskaya-samsa-na-grile/)")

#     elif query.data == 'wings':
#         query.edit_message_text(text="Крылышки - 500с (12 шт)\n\n![Крылышки](https://halal-spb.ru/sites/default/files/styles/large/public/krylyshki-kak-v-kfs-recept.jpg)")

#     elif query.data == 'shawarma':
#         query.edit_message_text(text="Шаурма - 270с\n\n![Шаурма](https://lookaside.fbsbx.com/lookaside/crawler/media/?media_id=100067684224848)")

#     elif query.data == 'burger':
#         query.edit_message_text(text="Бургер - 300с\n\n![Бургер](https://sxodim.com/uploads/images/2022/11/11/optimized/beff18152003115708dc2a06510b2f73_800xauto-q-85.jpg)")

#     elif query.data == 'start':
#         start(update, context)

# def main() -> None:
#     updater = Updater(TOKEN)

#     dispatcher = updater.dispatcher

#     dispatcher.add_handler(CommandHandler("start", start))
#     dispatcher.add_handler(CallbackQueryHandler(button))

#     updater.start_polling()
#     updater.idle()

# if __name__ == '__main__':
#     main()




















# from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
# from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     menu_keyboard = [
#         [KeyboardButton("Меню"), KeyboardButton("Локация")],
#         [KeyboardButton("О нас"), KeyboardButton("Заказать")],
#         [KeyboardButton("Доставка"), KeyboardButton("Назад")]
#     ]
#     reply_markup = ReplyKeyboardMarkup(menu_keyboard, resize_keyboard=True)
#     await update.message.reply_text('Выберите опцию:', reply_markup=reply_markup)

# async def about_us(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     about_text = "🛒 О нас:\n\nМы онлайн магазин еды. Вы можете заказать блюда, указанные в меню. Мы готовим вашу еду, и вы можете забрать её по нашему адресу или оформить доставку."
#     await update.message.reply_text(about_text)

# async def location(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     location_text = "📍Локация: Масалиева 100, Ош, Кыргызстан."
#     await update.message.reply_location(latitude=40.523245, longitude=72.805633)
#     await update.message.reply_text(location_text)

# async def order(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     order_text = "📞 Номер: 0708424268\nИмя: Маматиса кызы Айназ"
#     await update.message.reply_text(order_text)

# async def delivery(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     delivery_text = "🛵 Вы можете отправить своё местоположение для доставки.\nВидео курьера будет показано здесь."
#     await update.message.reply_text(delivery_text)

# async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     menu_keyboard = [
#         [KeyboardButton("1. Плов Узбекский - 500с"), KeyboardButton("2. Шашлык куриный - 450с")],
#         [KeyboardButton("3. Самса - 65с"), KeyboardButton("4. Крылышки - 500с")],
#         [KeyboardButton("5. Шаурма - 270с"), KeyboardButton("6. Бургер - 300с")],
#         [KeyboardButton("Назад")]
#     ]
#     reply_markup = ReplyKeyboardMarkup(menu_keyboard, resize_keyboard=True)
#     await update.message.reply_text('Выберите блюдо:', reply_markup=reply_markup)

# def main():
#     application = ApplicationBuilder().token('7545140888:AAEItO0WOZaX4BKBaLOPuf2O1QaoRvvaWts').build()

#     application.add_handler(CommandHandler("start", start))
#     application.add_handler(MessageHandler(filters.Text(["О нас"]), about_us))
#     application.add_handler(MessageHandler(filters.Text(["Локация"]), location))
#     application.add_handler(MessageHandler(filters.Text(["Заказать"]), order))
#     application.add_handler(MessageHandler(filters.Text(["Доставка"]), delivery))
#     application.add_handler(MessageHandler(filters.Text(["Меню"]), menu))

#     application.run_polling()

# if  name == 'main':
#     main()









# from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
# from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     menu_keyboard = [
#         [KeyboardButton("Меню"), KeyboardButton("Локация")],
#         [KeyboardButton("О нас"), KeyboardButton("Заказать")],
#         [KeyboardButton("Доставка"), KeyboardButton("Назад")]
#     ]
#     reply_markup = ReplyKeyboardMarkup(menu_keyboard, resize_keyboard=True)
#     await update.message.reply_text('Выберите опцию:', reply_markup=reply_markup)

# async def about_us(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     about_text = "🛒 О нас:\n\nМы онлайн магазин еды. Вы можете заказать блюда, указанные в меню. Мы готовим вашу еду, и вы можете забрать её по нашему адресу или оформить доставку."
#     await update.message.reply_text(about_text)

# async def location(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     location_text = "📍Локация: Масалиева 100, Ош, Кыргызстан."
#     await update.message.reply_location(latitude=40.523245, longitude=72.805633)
#     await update.message.reply_text(location_text)

# async def order(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     order_text = "📞 Номер: 0708424268\nИмя: Маматиса кызы Айназ"
#     await update.message.reply_text(order_text)

# async def delivery(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     delivery_text = "🛵 Вы можете отправить своё местоположение для доставки.\nВидео курьера будет показано здесь."
#     await update.message.reply_text(delivery_text)

# async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     menu_keyboard = [
#         [KeyboardButton("1. Плов Узбекский - 500с"), KeyboardButton("2. Шашлык куриный - 450с")],
#         [KeyboardButton("3. Самса - 65с"), KeyboardButton("4. Крылышки - 500с")],
#         [KeyboardButton("5. Шаурма - 270с"), KeyboardButton("6. Бургер - 300с")],
#         [KeyboardButton("Назад")]
#     ]
#     reply_markup = ReplyKeyboardMarkup(menu_keyboard, resize_keyboard=True)
#     await update.message.reply_text('Выберите блюдо:', reply_markup=reply_markup)

# def main():
#     application = ApplicationBuilder().token('7545140888:AAEItO0WOZaX4BKBaLOPuf2O1QaoRvvaWts').build()

#     application.add_handler(CommandHandler("start", start))
#     application.add_handler(MessageHandler(filters.Text(["О нас"]), about_us))
#     application.add_handler(MessageHandler(filters.Text(["Локация"]), location))
#     application.add_handler(MessageHandler(filters.Text(["Заказать"]), order))
#     application.add_handler(MessageHandler(filters.Text(["Доставка"]), delivery))
#     application.add_handler(MessageHandler(filters.Text(["Меню"]), menu))

#     application.run_polling()

# if __name__== '__main__':
#     main()





# from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
# from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters

# async def start(update: Update, context):
#     keyboard = [
#         [InlineKeyboardButton("Меню", callback_data='menu')],
#         [InlineKeyboardButton("Локация", callback_data='location')],
#         [InlineKeyboardButton("О нас", callback_data='about')],
#         [InlineKeyboardButton("Заказать", callback_data='order')],
#         [InlineKeyboardButton("Доставка", callback_data='delivery')]
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)
#     await update.message.reply_text('Выберите опцию:', reply_markup=reply_markup)

# async def button(update: Update, context):
#     query = update.callback_query
#     await query.answer()

#     if query.data == 'menu':
#         await show_menu(query)
#     elif query.data == 'location':
#         await show_location(query)
#     elif query.data == 'about':
#         await show_about(query)
#     elif query.data == 'order':
#         await show_order(query)
#     elif query.data == 'delivery':
#         await show_delivery(query)
#     else:
#         await query.edit_message_text(text="Неизвестная команда")

# async def show_menu(query):
#     keyboard = [
#         [InlineKeyboardButton("Плов Узбекский", callback_data='plov')],
#         [InlineKeyboardButton("Шашлык куриный", callback_data='shashlik')],
#         [InlineKeyboardButton("Самса", callback_data='samsa')],
#         [InlineKeyboardButton("Крылышки", callback_data='wings')],
#         [InlineKeyboardButton("Шаурма", callback_data='shawarma')],
#         [InlineKeyboardButton("Бургер", callback_data='burger')],
#         [InlineKeyboardButton("Назад", callback_data='start')]
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)
#     await query.edit_message_text(text="Выберите блюдо:", reply_markup=reply_markup)

# async def show_location(query):
#     await query.edit_message_text(text="📍Локация: Масалиева 100, Ош, Кыргызстан")

# async def show_about(query):
#     await query.edit_message_text(text="🛒 О нас:\n\nМы онлайн магазин еды. Вы можете заказать блюда, указанные в меню. Мы готовим вашу еду, и вы можете забрать её по нашему адресу или оформить доставку.")

# async def show_order(query):
#     await query.edit_message_text(text="Номер: 0708424268\nИмя: Маматиса кызы Айназ")

# async def show_delivery(query):
#     keyboard = [[KeyboardButton("Отправить местоположение", request_location=True)]]
#     reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
#     await query.edit_message_text(text="Отправьте ваше местоположение для доставки.", reply_markup=reply_markup)

# async def item_description(update: Update, context):
#     query = update.callback_query
#     await query.answer()
#     if query.data == 'plov':
#         await query.edit_message_text(text="Узбекский Плов\nЦена: 500с\n[Фото](https://images.unian.net/photos/2022_10/thumb_files/1200_0_1666194211-5378.jpg)")
#     elif query.data == 'shashlik':
#         await query.edit_message_text(text="Шашлык куриный\nЦена: 450с\n[Фото](https://www.m2-shop.ru/recipes/shashlickuriniebedra)")
#     elif query.data == 'samsa':
#         await query.edit_message_text(text="Самса\nЦена: 65с за штуку\n[Фото](https://grillweb.uz/reczepty/piczcza-i-pirogi/uzbekskaya-samsa-na-grile/)")
#     elif query.data == 'wings':
#         await query.edit_message_text(text="Крылышки\nЦена: 500с за 12шт\n[Фото](https://halal-spb.ru/sites/default/files/styles/large/public/krylyshki-kak-v-kfs-recept.jpg)")
#     elif query.data == 'shawarma':
#         await query.edit_message_text(text="Шаурма\nЦена: 270с\n[Фото](https://lookaside.fbsbx.com/lookaside/crawler/media/?media_id=100067684224848)")
#     elif query.data == 'burger':
#         await query.edit_message_text(text="Бургер\nЦена: 300с\n[Фото](https://sxodim.com/uploads/images/2022/11/11/optimized/beff18152003115708dc2a06510b2f73_800xauto-q-85.jpg)")

# if __name__ == '__main__':
#     application = ApplicationBuilder().token('7545140888:AAEItO0WOZaX4BKBaLOPuf2O1QaoRvvaWts').build()
#     application.add_handler(CommandHandler('start', start))
#     application.add_handler(CallbackQueryHandler(button))
#     application.add_handler(CallbackQueryHandler(item_description))

#     application.run_polling()










from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Главное меню
    keyboard = [
        [InlineKeyboardButton("Меню", callback_data='menu')],
        [InlineKeyboardButton("Локация", callback_data='location')],
        [InlineKeyboardButton("О нас", callback_data='about')],
        [InlineKeyboardButton("Заказать", callback_data='order')],
        [InlineKeyboardButton("Доставка", callback_data='delivery')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Выберите опцию:', reply_markup=reply_markup)

async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == 'menu':
        # Подменю Меню
        keyboard = [
            [InlineKeyboardButton("Плов Узбекский", callback_data='plov')],
            [InlineKeyboardButton("Шашлык куриный", callback_data='shashlyk')],
            [InlineKeyboardButton("Самса", callback_data='samsa')],
            [InlineKeyboardButton("Крылышки", callback_data='krylyshki')],
            [InlineKeyboardButton("Шаурма", callback_data='shaurma')],
            [InlineKeyboardButton("Бургер", callback_data='burger')],
            [InlineKeyboardButton("Назад", callback_data='start')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text="Меню:", reply_markup=reply_markup)

    elif query.data == 'location':
        # Локация
        await query.edit_message_text(
            text="📍Локация: Масалиева 100, Ош, Кыргызстан\n\n[Посмотреть на карте](https://www.google.com/maps?q=40.5135,72.8168)", parse_mode='Markdown'
        )
        
    elif query.data == 'about':
        # О нас
        await query.edit_message_text(text="🛒 О нас:\n\nМы онлайн магазин еды. Вы можете заказать блюда, указанные в меню. Мы готовим вашу еду, и вы можете забрать её по нашему адресу или оформить доставку.")

    elif query.data == 'order':
        # Заказать
        keyboard = [[InlineKeyboardButton("Позвонить", url="tel:+996708424268")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text="Контакты:\n\nНомер: 0708424268\nИмя: Маматиса кызы Айназ", reply_markup=reply_markup)
          
    elif query.data == 'delivery':
        # Доставка
        button = KeyboardButton('Отправить местоположение', request_location=True)
        reply_markup = ReplyKeyboardMarkup([[button]], resize_keyboard=True, one_time_keyboard=True)
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Отправьте свое местоположение для доставки:", reply_markup=reply_markup)

    elif query.data == 'plov':
        # Плов Узбекский
        await query.edit_message_text(text="Плов Узбекский - 500с\n\n[Посмотреть фото](https://images.unian.net/photos/2022_10/thumb_files/1200_0_1666194211-5378.jpg)")

    elif query.data == 'shashlyk':
        # Шашлык куриный
        await query.edit_message_text(text="Шашлык куриный - 450с\n\n[Посмотреть фото](https://www.m2-shop.ru/recipes/shashlickuriniebedra)")

    elif query.data == 'samsa':
        # Самса
        await query.edit_message_text(text="Самса - 65с за штук\n\n[Посмотреть фото](https://grillweb.uz/reczepty/piczcza-i-pirogi/uzbekskaya-samsa-na-grile)")

    elif query.data == 'krylyshki':
        # Крылышки
        await query.edit_message_text(text="12шт Крылышки - 500с\n\n[Посмотреть фото](https://halal-spb.ru/sites/default/files/styles/large/public/krylyshki-kak-v-kfs-recept.jpg)")

    elif query.data == 'shaurma':
        # Шаурма
        await query.edit_message_text(text="Шаурма - 270с\n\n[Посмотреть фото](https://lookaside.fbsbx.com/lookaside/crawler/media/?media_id=100067684224848)")
        
    elif query.data == 'burger':
        # Бургер
        await query.edit_message_text(text="Бургер - 300с\n\n[Посмотреть фото](https://sxodim.com/uploads/images/2022/11/11/optimized/beff18152003115708dc2a06510b2f73_800xauto-q-85.jpg)")

    elif query.data == 'start':
        await start(update, context)

async def location_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_location = update.message.location
    await update.message.reply_text(f"Ваше местоположение: {user_location.latitude}, {user_location.longitude}\n\nВаш заказ будет доставлен.")



def main():
    application = ApplicationBuilder().token("7545140888:AAEItO0WOZaX4BKBaLOPuf2O1QaoRvvaWts").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_click))
    application.add_handler(MessageHandler(filters.LOCATION, location_handler))

    application.run_polling()

if __name__ == '__main__':
    main()