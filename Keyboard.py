import telebot
from   telebot import types
import datetime
token = "840565652:AAF3aW49Bq91tYrKKmgnycRtpB76cXG9_eo"
bot  = telebot.TeleBot(token)

#klaviatura
@bot.message_handler(content_types=["text"])
def any_msg(message):
    keybardmain = types.InlineKeyboardMarkup(row_width=4)
    fist_button = types.InlineKeyboardButton(text="Поступление денег➡️", callback_data = "first")
    second_button = types.InlineKeyboardButton(text="Разные отчеты➡️", callback_data = "second")
    keybardmain.add(fist_button,second_button)
    bot.send_message(message.chat.id, "тестирование клавиш", reply_markup=keybardmain)

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    if call.data == "mainmenu":
     keybardmain = types.InlineKeyboardMarkup(row_width=2)
     fist_button = types.InlineKeyboardButton(text="Поступление денег", callback_data = "first")
     second_button = types.InlineKeyboardButton(text="Разные отчеты", callback_data = "second")
     keybardmain.add(fist_button,second_button)
     bot.edit_message_text( chat_id=call.message.chat.id, message_id=call.message.message_id,text="menu", reply_markup=keybardmain)
    if call.data == "first":
        keyboard = types.InlineKeyboardMarkup()
        rol1 =types.InlineKeyboardButton(text="yanvar", callback_data="1")
        rol2 =types.InlineKeyboardButton(text="fevral", callback_data="2")
        rol3 =types.InlineKeyboardButton(text="mart", callback_data="3")
        rol4 =types.InlineKeyboardButton(text="april", callback_data="4")
        rol5 =types.InlineKeyboardButton(text="may", callback_data="5")
        rol6 =types.InlineKeyboardButton(text="iyun", callback_data="6")
        rol7 =types.InlineKeyboardButton(text="iyul", callback_data="7")
        rol8 =types.InlineKeyboardButton(text="avgust", callback_data="8")
        backbuttton = types.InlineKeyboardButton(text="назад", callback_data="mainmenu")
        bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Вы перешли в месячные отчеты")
        keyboard.add(rol1, rol2,rol3,rol4,rol5,rol6,rol7,rol8, backbuttton)
        bot.edit_message_text( chat_id=call.message.chat.id, message_id=call.message.message_id,text="ответный текс", reply_markup=keyboard)

    elif call.data == "second":
        keyboard = types.InlineKeyboardMarkup()
        rol1 =types.InlineKeyboardButton(text="Налоговые отчеты", callback_data="1")
        rol2 =types.InlineKeyboardButton(text="Продажа", callback_data="2")
        rol3 =types.InlineKeyboardButton(text="покупка", callback_data="3")
        rol4 =types.InlineKeyboardButton(text="Затраты", callback_data="4")
        backbuttton = types.InlineKeyboardButton(text="назад", callback_data="mainmenu")
        keyboard.add(rol1, rol2,rol3,rol4, backbuttton)
        bot.edit_message_text( chat_id=call.message.chat.id, message_id=call.message.message_id,text="ответный текс", reply_markup=keyboard)
    elif call.data == "1" or call.data == "2" or call.data == "3":
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Придидущая кнопка")
        keyboard3 = types.InlineKeyboardMarkup()
        button  = types.InlineKeyboardButton(text="предеущая кнопка", callback_data="11")
        keyboard3.add(button)
        bot.edit_message_text( chat_id=call.message.chat.id, message_id=call.message.message_id,text="предеущая кнопка", reply_markup=keyboard3)


if __name__== "__main__":
        bot.polling(none_stop=True)
