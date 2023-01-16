import telebot
import time
import data
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import re
from telebot import types
from pillow import create_picture, get_numbers
from aiogram.dispatcher.filters.state import StatesGroup, State

# from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton

# Создаем экземпляр бота

bot = telebot.TeleBot('5978396970:AAEDoWW-BIFwYfyQ4bFJkuIKyeWjfH8OdlU')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Добро пожаловать в калькулятор профессий.')
    birthday = bot.send_message(message.chat.id, 'Введите дату рождения в формате 01.01.2000.')
    bot.register_next_step_handler(birthday, save_birthday)

def save_birthday(message):
    # bot.send_message(message.chat.id, 'Сначала введите корректную дату рождения в формате 01.01.2000.')
    user_info = {}
    if bool(re.fullmatch(r'\d\d.\d\d.\d{4}', message.text)):
        user_info['date'] = message.text
        print('True')
        image_name = create_picture(message.text, message.chat.id)
        bot.send_photo(message.chat.id, photo=open(image_name, 'rb'))
        time.sleep(2)
        bot.send_message(message.chat.id, 'Выберите, описание какой энергии хотите получить')
        bot.register_next_step_handler(message, choice, user_info)
    else:
        print('False')
        bot.send_message(message.chat.id, 'Сначала введите корректную дату рождения в формате 01.01.2000.')
        bot.register_next_step_handler(message, save_birthday)



def choice(message, user_info):
    date = user_info['date']
    print('date: ', date)
    if message.text == 'Подсознание':
        number = get_numbers(date)[1]
        send_description(chatid=message.chat.id, number=number)
    elif  message.text == 'Что развить в себе':
        number = get_numbers(date)[4]
        print(number)
        send_description(chatid=message.chat.id, number=number)

    elif message.text == 'Навыки предыдущего воплощения':
        number = get_numbers(date)[2]
        send_description(chatid=message.chat.id, number=number)
    elif message.text == 'Непройденный опыт, который следует пройти':
        number = get_numbers(date)[5]
        send_description(chatid=message.chat.id, number=number)
    elif message.text == 'Личность':
        number = get_numbers(date)[0]
        send_description(chatid=message.chat.id, number=number)
    elif message.text == 'Препятствия, блоки, сценарии':
        number = get_numbers(date)[3]
        send_description(chatid=message.chat.id, number=number)
        user_info['choice'] = message.text
        bot.send_message(message.chat.id, message.text)
        print(user_info)
    else:
        bot.send_message(message.chat.id, 'Выберите описание из пердложенных вариантов')
        print('False')
        bot.register_next_step_handler(message, choice, user_info)



def send_description(chatid, number):
    bot.send_message(chatid, '__КОД СУДЬБЫ__', parse_mode='MarkdownV2')
    bot.send_message(chatid, data.data[number])
    time.sleep(2)
    bot.send_message(chatid, '__Предназначение по коду судьбы__', parse_mode='MarkdownV2')
    bot.send_message(chatid, data.pred[number])
    time.sleep(2)
    bot.send_message(chatid, '__Рекомендации по коду судьбы__', parse_mode='MarkdownV2')
    bot.send_message(chatid, data.recom[number])
    time.sleep(2)
    bot.send_message(chatid, '__Негативная, неотработанная карма по коду судьбы:__', parse_mode='MarkdownV2')
    bot.send_message(chatid, data.nega[number])
    time.sleep(2)
    bot.send_message(chatid, '__Аффирмация для энергии:__', parse_mode='MarkdownV2')
    bot.send_message(chatid, data.afirm[number])
    time.sleep(2)

bot.polling(none_stop=True, interval=0)

