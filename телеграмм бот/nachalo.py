import sqlite3

import telebot
import sqlite3
import webbrowser
from telebot import types
tokin =('8349713612:AAFxSGwKUWS5_CP8hS-Qf_XoA8o55skSCGk')
bot = telebot.TeleBot (tokin)

@bot.message_handler(commands=['site', 'website'])
def site(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('перейти на сайт', url='https://www.avito.ru/domodedovo/krasota_i_zdorove/duhi_4437180629'))
    bot.reply_to(message,'хорошее решение', reply_markup=markup)

@bot.message_handler(commands= ['start'])
def ftornik (message):
    bot.send_message(message.chat.id,  f'Добрый день,'
                                       f'  покупатель {message.from_user.first_name}!  '
                                       f'Тебя приветствует семейный магазин ковров. '
                                       f'Предлагаем Вам ознакомиться с нашим ассортиментом на тех'
                                       f' платформах, которые Вам удобны \n 1)при вводе команды /site вас'
                                       f' перенесет на платформу АВИТО \n 2) если хотите остаться здесь введите команду (/shop)  ')

@bot.message_handler(commands= ['start '])
def start(message):
    conn = sqlite3.connect('shop.sql')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar (50), pass varchar (50)')
    conn.commit()
    cur.close()
    conn.close()

#@bot.message_handler()
#def info (message):
#    if message.text.lower()== 'привет':
#       bot.send_message(message.chat.id, f'Приветствую!{message.from_user.first_name}')
 #   elif message.text.lower()== 'id':
 #      bot.reply_to(message, f'ID:{message.from_user.id}')


bot.polling(none_stop= True)