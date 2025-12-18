import telebot 
from telebot import types
from extensions import APIException, CurrencyConverter
import config

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    instructions = """
📌 Отправьте сообщение в формате:
<валюта1> <валюта2> <количество>

Пример:
доллар рубль 100

💱 Доступные валюты: /values
"""
    bot.reply_to(message, instructions)


@bot.message_handler(commands=['values'])
def handle_values(message):
    currencies = """
💰 Доступные валюты:
- Евро (EUR)
- Доллар (USD)
- Рубль (RUB)
"""
    bot.reply_to(message, currencies)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    try:
        parts = message.text.split()
        if len(parts) != 3:
            raise APIException("Неверный формат. Нужно: валюта1 валюта2 количество")

        base, quote, amount = parts
        result = CurrencyConverter.get_price(base, quote, amount)
        bot.reply_to(message, f"💵 {amount} {base.upper()} = {result} {quote.upper()}")

    except APIException as e:
        bot.reply_to(message, f"❌ Ошибка: {e}")
    except Exception as e:
        bot.reply_to(message, f"⚠️ Неизвестная ошибка: {e}")


bot.polling()