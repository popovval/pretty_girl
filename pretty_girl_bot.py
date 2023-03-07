import os
import telebot
from messages import get_pretty_message

token = os.environ.get('TOKEN')

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, "Привет!\n Я могу дать тебе поощрение.\n Напиши 'Дай поощрение'")


@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text == 'Дай поощрение':
        bot.send_message(message.from_user.id, get_pretty_message())
    else:
        bot.send_message(message.from_user.id, 'Не понял')


bot.polling(none_stop=True)
