from re import T
import telebot
from gtts import gTTS

# txt = 'python developer'
txt = 'студенты'

audio = gTTS(text=txt, lang='ru')
audio.save('audio2.mp3')


token = '5116709006:AAExkfzjSV8EpNxUqloTgnpZF8Jj-w809DQ'
bot = telebot.TeleBot(token=token)
@bot.message_handler(commands=['start'])
def send_message(message):
    username = message.chat.first_name
    bot.send_message(message.chat.id, f'Привет {username}. Я телеграм бот')



@bot.message_handler(content_types='text')
def func(message):
    bot.send_message(message.chat.id, 'Hi')


print('Бот работает...')
bot.infinity_polling()
