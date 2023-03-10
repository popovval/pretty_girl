import os
import sys
import logging
import telebot
from messages import get_pretty_message

token = os.environ.get('TOKEN')

bot = telebot.TeleBot(token)
logging.basicConfig(filename='log.log', level=logging.INFO)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, "Привет!\n Я могу дать тебе поощрение.\n Напиши 'Дай поощрение'")


@bot.message_handler(content_types='text')
def message_reply(message):
    logging.info(f'USER: {message.from_user.username} MESSAGE: {message.text}')
    if message.text == 'Дай поощрение':
        bot.send_message(message.from_user.id, get_pretty_message())
    elif message.text == 'хуй':
        bot.send_message(message.from_user.id, 'ЗАЛУУПА!!')
    else:
        bot.send_message(message.from_user.id, 'Не понял')


bot.polling(none_stop=True)
