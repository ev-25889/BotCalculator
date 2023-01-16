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

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

class UserState(StatesGroup):
    name = State()
    address = State()
# Функция, обрабатывающая команду /start


@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Введите дату рождения в формате 01.01.2000')

@dp.message_handler(commands=["reg"])
async def user_register(message: types.Message):
    await message.answer("Введите своё имя")
    await UserState.name.set()

# dp = Dispatcher(bot, storage=storage)

# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message: types.Message, state: FSMContext):
    if  re.fullmatch(r'\d\d.\d\d.\d{4}', message.text):
        image_name = create_picture(message.text, message.chat.id)
        bot.send_photo(message.chat.id, photo=open(image_name, 'rb'))
        time.sleep(2)
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=False, one_time_keyboard=True)
        dia = types.KeyboardButton(text='Подсознание')
        mes = types.KeyboardButton(text='Что развить в себе')
        ano = types.KeyboardButton(text='Навыки предыдущего воплощения')
        dia1 = types.KeyboardButton(text='Непройденный опыт, который следует пройти')
        mes1 = types.KeyboardButton(text='Личность')
        ano1 = types.KeyboardButton(text='Препятствия, блоки, сценарии')
        keyboard.add(dia, mes, ano, dia1, mes1, ano1)
        bot.send_message(message.chat.id, 'Выберите, описание какой энергии хотите получить', reply_markup=keyboard)

        with state.proxy() as data:
            data['date'] = message.text
            data['chatid'] = message.chat.id

    if message.text == 'Подсознание' or message.text == 'Что развить в себе' or \
        message.text == 'Навыки предыдущего воплощения' \
        or message.text == 'Непройденный опыт, который следует пройти' or \
        message.text == 'Личность' \
        or message.text == 'Препятствия, блоки, сценарии':
        with state.proxy() as data:
            choice = data['choice']
            date = data['date']
            chatid = data['chatid']

        number = 1
        number = get_numbers(date)[0] if choice == 'Подсознание' else number
        number = get_numbers(date)[0] if choice == 'Что развить в себе' else number
        number = get_numbers(date)[0] if choice == 'Навыки предыдущего воплощения' else number
        number = get_numbers(date)[0] if choice == 'Непройденный опыт, который следует пройти' else number
        number = get_numbers(date)[0] if choice == 'Личность' else number
        number = get_numbers(date)[0] if choice == 'Препятствия, блоки, сценарии' else number

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
    else:
        bot.send_message(message.chat.id, 'Сначала введите корректную дату', parse_mode='MarkdownV2')






@bot.message_handler(content_types=["text"])
def send_text(messagecallback: types.CallbackQuery, state: FSMContext):
    with state.proxy() as data:
        choice = data['choice']
        date = data['date']
        chatid = data['chatid']

    number = 1
    number = get_numbers(date)[0] if choice == 'Подсознание' else number
    number = get_numbers(date)[0] if choice == 'Что развить в себе' else number
    number = get_numbers(date)[0] if choice == 'Навыки предыдущего воплощения' else number
    number = get_numbers(date)[0] if choice == 'Непройденный опыт, который следует пройти' else number
    number = get_numbers(date)[0] if choice == 'Личность' else number
    number = get_numbers(date)[0] if choice == 'Препятствия, блоки, сценарии' else number

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



# Запускаем бота
bot.polling(none_stop=True, interval=0)

