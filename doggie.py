import requests
import re
# Подключаем модуль случайных чисел 
import random
# Подключаем модуль для Телеграма
import telebot
# Указываем токен
bot = telebot.TeleBot('1417556243:AAEw8AYeTybzy7Y4TJdvRcjZvw9BDwcG8CY');
# Импортируем типы из модуля, чтобы создавать кнопки
from telebot import types
# Заготовки для трёх предложений
motivation = ["never give up.","never stop.","you can fucking do anything.","youre worthy and valuable.","stay strong."]
love = ["i love you.","i adore you.","love you from the bottom of my heart.","youre loved.","luuuv."]
gay = ["i do it for the girls and the gays thats it.","shine girl.","take pride in yourself.","gay is the new black.", "❤️p🧡r💛i💚d💙e💜"]
emoji = ["🤍","💗","🗿","🌚","🌍"]
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url

def get_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url

# Метод, который получает сообщения и обрабатывает их
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # Если написали «Привет»
    if message.text == "Hello":
        # Пишем приветствие
        bot.send_message(message.from_user.id, "sry im only a child and cannot do anything yet bye and have a great day")
        # Готовим кнопки
        keyboard = types.InlineKeyboardMarkup()
        # По очереди готовим текст и обработчик для каждого знака зодиака
        key_oven = types.InlineKeyboardButton(text='sad', callback_data='sad')
        # И добавляем кнопку на экран
        keyboard.add(key_oven)
        key_telec = types.InlineKeyboardButton(text='gay', callback_data='gay')
        keyboard.add(key_telec)
        key_bliznecy = types.InlineKeyboardButton(text='shitty', callback_data='sad')
        keyboard.add(key_bliznecy)
        key_rak = types.InlineKeyboardButton(text='cringy', callback_data='gay')
        keyboard.add(key_rak)
        key_lev = types.InlineKeyboardButton(text='empowered', callback_data='empowered')
        keyboard.add(key_lev)
        key_deva = types.InlineKeyboardButton(text='loved', callback_data='loved')
        keyboard.add(key_deva)
        key_vesy = types.InlineKeyboardButton(text='energetic', callback_data='sad')
        keyboard.add(key_vesy)
        key_scorpion = types.InlineKeyboardButton(text='dead', callback_data='sad')
        keyboard.add(key_scorpion)
        key_strelec = types.InlineKeyboardButton(text='happy', callback_data='sad')
        keyboard.add(key_strelec)
        key_kozerog = types.InlineKeyboardButton(text='thankful', callback_data='loved')
        keyboard.add(key_kozerog)
        # Показываем все кнопки сразу и пишем сообщение о выборе
        bot.send_message(message.from_user.id, text='pls dont be sad actually i can surprise you love. choose how you feel', reply_markup=keyboard)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "tell me 'Hello'")
    elif message.text == "/luv":
      bot.send_message(message.from_user.id, "i love you sweetie cutie-pie")
      a = random.choice(love) + random.choice(emoji)
      bot.send_message(message.from_user.id, a)
    elif message.text == "/pic":
      bot.send_message(message.from_user.id, 'here you go swetie!')
      bot.send_photo(message.from_user.id, photo=get_image_url())
    elif message.text == "/start":
      bot.send_message(message.from_user.id, "i cannot do much yet but you can already ask for /help or look for /luv or try asking me for a doggie /pic but the most functional comes with the basic 'Hello' greeting just try it out")
    elif message.text == "Ксюша солнышко":
        bot.send_message(message.from_user.id, "Тимофей пидр")
    else:
        bot.send_message(message.from_user.id, "i dont quite get what you mean, try asking for /help")
# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    # Если нажали на одну из 12 кнопок — выводим гороскоп
    if call.data == "sad": 
        # Формируем гороскоп
        msg = random.choice(motivation) + ' ' + random.choice(love) 
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)
    elif call.data == "gay": 
        # Формируем гороскоп
        msg = random.choice(gay) + ' ' + random.choice(love) + random.choice(emoji)
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)
    elif call.data == "empowered": 
        # Формируем гороскоп
        msg = random.choice(motivation) + ' ' + random.choice(emoji)
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)
    elif call.data == "loved": 
        # Формируем гороскоп
        msg = random.choice(love) + random.choice(emoji) 
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)

# Запускаем постоянный опрос бота в Телеграме
bot.polling(none_stop=True, interval=0)

