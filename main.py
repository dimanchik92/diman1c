import telebot
from   telebot import types
import datetime
token = "840565652:AAF3aW49Bq91tYrKKmgnycRtpB76cXG9_eo"
bot  = telebot.TeleBot(token)
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def first(message):
    key  = telebot.types.ReplyKeyboardMarkup(True,False)
    key.row("Отчеты 1", "Отчеты 2")
    send = bot.send_message(message.from_user.id,)
    bot.register_next_step_handler(send, second)
def second (message):
    if message.text == "Отчеты 1":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("oylik3" , "Yillik4"," Bitta orqaga qaytish" )
        send = bot.send_message(message.from_user.id, "Ikkinchi darajali klaviatura", reply_markup=keyboard)
        bot.register_next_step_handler(send,third)
    elif message.text == "Отчеты 2":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("Sotuv miqdori5", "Soliq6","Bitta orqaga qaytish")
        send = bot.send_message(message.from_user.id, "Ikkinchi darajali klaviatura", reply_markup=keyboard)
        bot.register_next_step_handler(send,third)
def third(message):
    if message.text == "oylik3":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("Foyda7", "Summa8","Ikkita orqaga qaytish")
        send = bot.send_message(message.from_user.id, "Ikkinchi darajali klaviatura", reply_markup=keyboard)
        bot.register_next_step_handler(send,fourth)
    elif message.text == "Yillik4":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("Umumiy daromad9", "kvartal10","Ikkita orqaga qaytish")
        send = bot.send_message(message.from_user.id, "Uchinchi darajali klaviatura", reply_markup=keyboard)
        bot.register_next_step_handler(send,fourth)
    elif message.text == "Sotuv miqdori5":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("Agent11", "Klient12","Ikkita orqaga qaytish")
        send = bot.send_message(message.from_user.id, "Ikkinchi darajali klaviatura", reply_markup=keyboard)
        bot.register_next_step_handler(send,fourth)
    elif  message.text == "Soliq6":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("Oylik13", "Kvartal14","Ikkinchi darajali klaviatura")
        send = bot.send_message(message.from_user.id, "Uchinchi darajali klaviatura", reply_markup=keyboard)
        bot.register_next_step_handler(send,fourth)
    elif message.text == "Birinchi darajaga qaytish ":
        first(message)


def fourth(message):
    if message.text == "Ikkita orqaga qaytish":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("oylik3", "Yillik4"," Bitta orqaga qaytish")
        send = bot.send_message(message.from_user.id, "Ikkinchi darajali klaviatura", reply_markup=keyboard)
        bot.register_next_step_handler(send,third)
    else:

        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("Oxirgi darajali klaviatura, tamom", "Bitta orqaga qaytish")
        send = bot.send_message(message.from_user.id, "To'rtinchi darajali klaviatura, Tamom", reply_markup=keyboard)
        bot.register_next_step_handler(send, first)
def fin(message):
    if message.text == "Uchinchi darajali klaviaturaga qaytish":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("Foyda7", "Summa8","Ikkita orqaga qaytish")
        send = bot.send_message(message.from_user.id, "Uchinchi darajali klaviatura", reply_markup=keyboard)
        bot.register_next_step_handler(send,fourth)

if __name__== "__main__":
        bot.polling(none_stop=True)
#Chiroyli amalga oshmagan ichma ich knopkalar