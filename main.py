'''
Content types:
text, audio, document, photo, sticker, video, video_note, voice, location, contact,
new chat_members, left_chat_member, new_chat_title, new_chat_photo, delete_chat_photo,
group_chat_created, supergroup_chat_created,
channel_chat_created, migrate_to_chat_id, migrate_from_chat_id, pinned_message.
'''

import telebot
from config import *

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])  # первое знакомство
def send_welcome(message: telebot.types.Message):
    text = 'доброго времени суток, чтобы узнать список команд и как пользоваться ботам, используйте /help'
    # bot.send_message(message.chat.id, text)
    bot.send_message(message.chat.id,
                     f"доброго времени суток, чтобы узнать список команд и как пользоваться ботом, используйте /help \n приятного пользования, {message.chat.username}")


@bot.message_handler(commands=['help'])  # помощь в навигации по боту
def send_welcome(message: telebot.types.Message):
    texthelp = 'доступные команды: \n /start /values /help \n пример использования: USD RUB 123'
    bot.send_message(message.chat.id, texthelp)


@bot.message_handler(commands=['values'])  # узнать список доступных валют
def values(message: telebot.types.Message):
    text = 'доступные валюты:'
    for i in exchanges.keys():
        text = '\n'.join(((text, i)))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['photo', ])  # просто рофло реакция на фото от пользователя
def say_lmao(message: telebot.types.Message):
    bot.reply_to(message, 'воу воу! отличная пикча, добавлю ее в сохры прямо как в 2к17')


@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message: telebot.types.Message):
    bot.reply_to(message,
                 'это конечно замечательно, но со мной лучше общатья командами, чтобы их узнать, напиши мне /help')


base_key = 'USD'
sym_key = 'RUB'
amount = 1

r1 = requests.get(f"https://v6.exchangerate-api.com/v6/5f3d2ba1970175b2f4c0741e/pair/{base_key}/{sym_key}/{amount}")
resp = json.loads(r1.content)
print(resp['conversion_rate'])


@bot.message_handler(content_types=['text'])
def converter(message: telebot.types.Message):
    base_key, sym_key, amount = message.text.split()
    r = requests.get(f"https://v6.exchangerate-api.com/v6/5f3d2ba1970175b2f4c0741e/pair/{base_key}/{sym_key}/{amount}")
    resp = json.loads(r.content)
    new_price = resp['conversion_rate'] * (float(amount))
    bot.reply_to(message, f'Цена {amount} {base_key} в {sym_key}: {new_price}')


bot.polling(none_stop=True)
