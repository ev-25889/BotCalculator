import telebot
import time
from telebot import types
from pillow import create_picture


# Создаем экземпляр бота

bot = telebot.TeleBot('5978396970:AAEDoWW-BIFwYfyQ4bFJkuIKyeWjfH8OdlU')

# Функция, обрабатывающая команду /start

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Введите дату рождения в формате 01.01.2000')
# Получение сообщений от юзера



@bot.message_handler(content_types=["text"])
def handle_text(message):

    image_name = create_picture(message.text, message.chat.id)
    #mess = 'число {}, месяц {}, год {}.'.format(hoy, mes, ano)
    # bot.send_message(message.chat.id, image_name)
    bot.send_photo(message.chat.id, photo=open(image_name, 'rb'))
    time.sleep(2)
    bot.send_message(message.chat.id, 'Выберете, описание какой энергии хотите получить')

# Запускаем бота
bot.polling(none_stop=True, interval=0)


"""
def send_photo_file(chat_id, img):
    files = {'photo': open(img, 'rb')}
    bot.send_message(chat.id, 'image.new_img.png')
    requests.post(f'{URL}{TOKEN}/sendPhoto?chat_id={chat_id}', files=files)
    """