from aiogram.types \
import ReplyKeyboardRemove, \
ReplyKeyboardMarkup,\
KeyboardButton, \
InlineKeyboardMarkup, InlineKeyboardButton
import telegram
import color
import telebot
from telebot import types
import pythoncom
import win32com.client
import datetime
import calendar
import pandas as pd
import logging
import  colorsys
token = "840565652:AAF3aW49Bq91tYrKKmgnycRtpB76cXG9_eo"
bot=telebot.TeleBot(token)

now = datetime.datetime.now()
V83_CONN_STRING = 'File="C:\\Users\\Admin\\Desktop\\InfoBas\\";Usr="Достон";Pwd="55555";'

pythoncom.CoInitialize()
V83 = win32com.client.Dispatch("V83.COMConnector").Connect(V83_CONN_STRING)
str  = ""
vizov=""
dictkk = {}
dictnk = {}
dictsk = {}
dictuk = {}
dictob = {}
dictpr={}
dictprpp={}
dictprpppf={}
dictprkk={}
dictprsos={}
kolpf=0
sampf = ""
kodpf=""
koldnpre = calendar.monthrange(now.year,now.month-1)[1]
namesa="ДАТАВРЕМЯ("+repr(now.year)+","+repr(now.month)+","+" 1, 0, 0, 0)"
konPeri= "ДАТАВРЕМЯ("+repr(now.year)+","+repr(now.month)+","+repr(now.day)+", 23, 59, 59)"
nachprm="ДАТАВРЕМЯ("+repr(now.year)+","+repr(now.month-1)+","+" 1, 0, 0, 0)"
konprm="ДАТАВРЕМЯ("+repr(now.year)+","+repr(now.month-1)+","+repr(koldnpre)+", 23, 59, 59)"
nachgod="ДАТАВРЕМЯ("+repr(now.year)+",1, 1, 0, 0, 0)"



def posledn(dict,call,kodpf,sampf):
    for key, value in dict.items():
        print(kodpf)
        print(dict)

        if kodpf == value:

            print(value)
            q = '''
                ВЫБРАТЬ
    		    	СпецификацииНоменклатурыИсходныеКомплектующие.Количество КАК kol,
    		    	СпецификацииНоменклатурыИсходныеКомплектующие.Номенклатура.Код КАК kod,
    		    	СпецификацииНоменклатурыИсходныеКомплектующие.Номенклатура.Наименование КАК imya,
    		    	СпецификацииНоменклатуры.Код КАК kodr
    		    ИЗ
    		    	Справочник.СпецификацииНоменклатуры.ИсходныеКомплектующие КАК СпецификацииНоменклатурыИсходныеКомплектующие
    				ЛЕВОЕ СОЕДИНЕНИЕ Справочник.СпецификацииНоменклатуры КАК СпецификацииНоменклатуры
    				ПО СпецификацииНоменклатурыИсходныеКомплектующие.Ссылка = СпецификацииНоменклатуры.Ссылка
    		    ГДЕ
    		        СпецификацииНоменклатуры.Код = "''' + value + '''"
                    '''
            query = V83.NewObject("Query", q)
            sel = query.Execute().Choose()
            keyboard = types.InlineKeyboardMarkup(row_width=2)
            dictprsos = {}
            plus1 = types.InlineKeyboardButton(text="+1", callback_data="plus1", )
            minus1 = types.InlineKeyboardButton(text="-1", callback_data="minus1")
            plus10 = types.InlineKeyboardButton(text="+10", callback_data="plus10")
            minus10 = types.InlineKeyboardButton(text="-10", callback_data="minus10")
            plus100 = types.InlineKeyboardButton(text="+100", callback_data="plus100")
            minus100 = types.InlineKeyboardButton(text="-100", callback_data="minus100")
            plus1000 = types.InlineKeyboardButton(text="+1000", callback_data="plus1000")
            minus1000 = types.InlineKeyboardButton(text="-1000", callback_data="minus1000")
            keyboard.row(plus1, plus10, minus10, minus1)
            keyboard.row(plus100, plus1000, minus1000, minus100)
            while sel.next():
                print(sel.kod)
                print(sel.imya)
                dictprsos[sel.imya] = sel.kod
                rol1 = types.InlineKeyboardButton(text=repr(sel.imya) + "--" + repr(sel.kol * 0), callback_data=sel.kod)
                keyboard.add(rol1)
            backbuttton = types.InlineKeyboardButton(text="назад", callback_data="second")
            pod_button = types.InlineKeyboardButton(text="Подтвердить", callback_data = "под")
            keyboard.add(backbuttton, pod_button)
            #bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
#                                      text="установите количество и утвердите производство")
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Установите количество " + sampf + ":" + repr(kolpf), reply_markup=keyboard)



@bot.message_handler(commands=["start"])
def any_msg(message):
    keybardmain = types.InlineKeyboardMarkup(row_width=2)
    fist_button = types.InlineKeyboardButton(text="Продажа✅", callback_data = "first")
    second_button = types.InlineKeyboardButton(text="Производство🏭️", callback_data = "second")
    third_button = types.InlineKeyboardButton(text="Касса💵️", callback_data = "third")
    forth_button = types.InlineKeyboardButton(text="Банк💰️", callback_data = "forth")
    keybardmain.add(fist_button,second_button, third_button, forth_button)
    bot.send_message(message.chat.id, "Выберите тип отчета:", reply_markup=keybardmain)

@bot.callback_query_handler(func=lambda call:True)

def callback_inline(call):



    global str
    global vizov
    global dictprpppf
    global dictkk
    global dictnk
    global dictsk
    global dictuk
    global dictob
    global dictpr
    global dictprpp
    global dictprkk
    global dictprsos
    global inline_kb1
    global kolpf
    global sampf
    global kodpf


    if call.data == "mainmenu":
     keybardmain = types.InlineKeyboardMarkup(row_width=2)
     fist_button = types.InlineKeyboardButton(text="Продажа✅", callback_data = "first")
     second_button = types.InlineKeyboardButton(text="Производство🏭", callback_data = "second")
     third_button = types.InlineKeyboardButton(text="Касса💵", callback_data = "third")
     forth_button = types.InlineKeyboardButton(text="Банк💰", callback_data = "forth")
     keybardmain.add(fist_button,second_button, third_button, forth_button)
     bot.edit_message_text( chat_id=call.message.chat.id, message_id=call.message.message_id,text="menu", reply_markup=keybardmain)
    if call.data == "first":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        rol1 =types.InlineKeyboardButton(text="с начала месяца", callback_data="снм")
        rol2 =types.InlineKeyboardButton(text="с начала года", callback_data="снг")
        rol3 =types.InlineKeyboardButton(text="прошлый месяц", callback_data="пм")
        backbuttton = types.InlineKeyboardButton(text="назад", callback_data="mainmenu")
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Вы перешли в месячные отчеты")
        keyboard.add(rol1, rol2,rol3,  backbuttton)
        bot.edit_message_text( chat_id=call.message.chat.id, message_id=call.message.message_id,text="текущий остаток кассы: ", reply_markup=keyboard)
    elif call.data == "second":
        dictpr={}
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        q = '''
        ВЫБРАТЬ
			ПодразделенияОрганизаций.Наименование КАК imya,
			ПодразделенияОрганизаций.КПП КАК klyuch
		ИЗ
			Справочник.ПодразделенияОрганизаций КАК ПодразделенияОрганизаций
		ГДЕ
			ПодразделенияОрганизаций.КПП <> ""
            '''
        query = V83.NewObject("Query", q)
        sel = query.Execute().Choose()
        while sel.next():
            dictpr[sel.imya] = sel.klyuch
            rol1 = types.InlineKeyboardButton(text=repr(sel.imya), callback_data=sel.klyuch)
            keyboard.add(rol1)
        backbuttton = types.InlineKeyboardButton(text="назад", callback_data="mainmenu")
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="выберите вашу подразделению")
        keyboard.add(backbuttton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="выберите вашу подразделению", reply_markup=keyboard)

    elif call.data == "third":
        #print(konPeri)
        q = '''
        ВЫБРАТЬ
            ДеньгиОстаткиИОбороты.Период КАК data,
            ДеньгиОстаткиИОбороты.Статья.Наименование КАК statya,
            ДеньгиОстаткиИОбороты.Примечения КАК primechaniya,
            ДеньгиОстаткиИОбороты.СуммаПриход КАК sumpri,
            ДеньгиОстаткиИОбороты.СуммаРасход КАК sumras,
        	ДеньгиОстаткиИОбороты.Клиент КАК Clien
        ИЗ
        	РегистрНакопления.Деньги.ОстаткиИОбороты(''' + namesa + ''', ''' + konPeri + ''', Запись, , ХранилищеДенег.Код ="000000001") КАК ДеньгиОстаткиИОбороты
        УПОРЯДОЧИТЬ ПО
            statya,
            data	
        '''
        query = V83.NewObject("Query", q)
        sel = query.Execute().Choose()
        df = pd.DataFrame()
        while sel.next():
            print(repr(sel.data))
            print(repr(sel.statya))
            print(repr(sel.primechaniya))
            print(repr(sel.sumpri))
            print(repr(sel.sumras))
            print(repr(sel.Clien))
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        rol1 =types.InlineKeyboardButton(text="с начала месяца", callback_data="снм")
        rol2 =types.InlineKeyboardButton(text="с начала года", callback_data="снг")
        rol3 =types.InlineKeyboardButton(text="прошлый месяц", callback_data="пм")
        backbuttton = types.InlineKeyboardButton(text="назад", callback_data="mainmenu")
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Вы перешли в месячные отчеты")
        keyboard.add(rol1, rol2,rol3,  backbuttton)
        bot.edit_message_text( chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выберите период данных", reply_markup=keyboard)
    elif call.data == "снм":
        str  = str+"Продажа по регионам"
        q = '''
        ВЫБРАТЬ
            РасчетыОбороты.Клиент.Наименование КАК Clien,
			РасчетыОбороты.Клиент.КодАльфа2 КАК kodalfa2,
			РасчетыОбороты.СуммаПриход КАК sum
		ИЗ
		    РегистрНакопления.Расчеты.Обороты('''+namesa+''', '''+konPeri+''', , ) КАК РасчетыОбороты
        '''
        query = V83.NewObject("Query", q)
        sel = query.Execute().Choose()
        dictkk.clear()
        dictnk.clear()
        dictsk.clear()
        dictuk.clear()
        dictob.clear()
        sumprodreg = 0
        sumprodkorp = 0
        sumprodgor = 0
        sumprodstar = 0
        sumprodobsh = 0
        while sel.next():
            print(repr(sel.kodalfa2))
            print(repr(sel.sum))
            if repr(sel.kodalfa2)=="'УК'":
                sumprodreg=sumprodreg+sel.sum
                sumprodobsh=sumprodobsh+sel.sum
                dictuk[sel.Clien]=sel.sum
                dictob.update(dictuk)
                print(repr(dictuk.items())+"1")
            elif repr(sel.kodalfa2) == "'КК'":
                sumprodkorp = sumprodkorp + sel.sum
                sumprodobsh=sumprodobsh+sel.sum
                dictkk[sel.Clien] = sel.sum
                dictob.update(dictkk)
            elif repr(sel.kodalfa2) == "'НК'":
                sumprodgor = sumprodgor+sel.sum
                sumprodobsh=sumprodobsh+sel.sum
                dictnk[sel.Clien] = sel.sum
                dictob.update(dictnk)
            elif repr(sel.kodalfa2) == "'СК'":
                sumprodstar = sumprodstar + sel.sum
                sumprodobsh=sel.sum+sumprodobsh
                dictsk[sel.Clien] = sel.sum
                dictob.update(dictsk)
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        rov2 = types.InlineKeyboardButton(text="Регионы ("+repr("{:,}".format(sumprodreg))+")", callback_data="снмРегоины") # +repr(sumprodreg)+")"
        rov3 = types.InlineKeyboardButton(text="Корпоротивные ("+repr("{:,}".format(sumprodkorp))+")", callback_data="снмКорпоротивные")
        rov4 = types.InlineKeyboardButton(text="Город ("+repr("{:,}".format(sumprodgor))+")", callback_data="снмГород")
        rov5 = types.InlineKeyboardButton(text="Старые Клиенты ("+repr("{:,}".format(sumprodstar))+")", callback_data="снмСтраые")
        rov6 = types.InlineKeyboardButton(text="Общий ("+repr("{:,}".format(sumprodobsh))+")", callback_data="снмОбщий")
        sumprodreg = 0
        sumprodkorp = 0
        sumprodgor = 0
        sumprodstar = 0
        sumprodobsh = 0
        backbuttton = types.InlineKeyboardButton(text="назад" , callback_data="first")
        keyboard.add(rov2, rov3, rov4, rov5,rov6,backbuttton)
        bot.edit_message_text( chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выберите регион :", reply_markup=keyboard)
        print(dictuk.items())
    elif call.data == "снг":
        str = str + "Продажа по регионам"
        q = '''
            ВЫБРАТЬ
                РасчетыОбороты.Клиент.Наименование КАК Clien,
    			РасчетыОбороты.Клиент.КодАльфа2 КАК kodalfa2,
    			РасчетыОбороты.СуммаПриход КАК sum
    		ИЗ
    		    РегистрНакопления.Расчеты.Обороты(''' + nachgod + ''', ''' + konPeri + ''', , ) КАК РасчетыОбороты
            '''
        query = V83.NewObject("Query", q)
        sel = query.Execute().Choose()
        dictkk.clear()
        dictnk.clear()
        dictsk.clear()
        dictuk.clear()
        dictob.clear()
        sumprodreg = 0
        sumprodkorp = 0
        sumprodgor = 0
        sumprodstar = 0
        sumprodobsh = 0
        while sel.next():
            print(repr(sel.kodalfa2))
            print(repr(sel.sum))
            if repr(sel.kodalfa2) == "'УК'":
                sumprodreg = sumprodreg + sel.sum
                sumprodobsh = sumprodobsh + sel.sum
                dictuk[sel.Clien] = sel.sum
                dictob.update(dictuk)
            elif repr(sel.kodalfa2) == "'КК'":
                sumprodkorp = sumprodkorp + sel.sum
                sumprodobsh = sumprodobsh + sel.sum
                dictkk[sel.Clien] = sel.sum
                dictob.update(dictkk)
            elif repr(sel.kodalfa2) == "'НК'":
                sumprodgor = sumprodgor + sel.sum
                sumprodobsh = sumprodobsh + sel.sum
                dictnk[sel.Clien] = sel.sum
                dictob.update(dictnk)
            elif repr(sel.kodalfa2) == "'СК'":
                sumprodstar = sumprodstar + sel.sum
                sumprodobsh = sel.sum + sumprodobsh
                dictsk[sel.Clien] = sel.sum
                dictob.update(dictsk)
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        rov2 = types.InlineKeyboardButton(text="Регионы (" + repr("{:,}".format(sumprodreg)) + ")",
                                          callback_data="снгРегионы")  # +repr(sumprodreg)+")"
        rov3 = types.InlineKeyboardButton(text="Корпоротивные (" + repr("{:,}".format(sumprodkorp)) + ")", callback_data="снгКорпоротивные")
        rov4 = types.InlineKeyboardButton(text="Город (" + repr("{:,}".format(sumprodgor)) + ")", callback_data="снгГород")
        rov5 = types.InlineKeyboardButton(text="Старые Клиенты (" + repr("{:,}".format(sumprodstar)) + ")", callback_data="СнгСтарыеКлиенты")
        rov6 = types.InlineKeyboardButton(text="Общий (" + repr("{:,}".format(sumprodobsh)) + ")", callback_data="снгОбщий")
        sumprodreg = 0
        sumprodkorp = 0
        sumprodgor = 0
        sumprodstar = 0
        sumprodobsh = 0
        backbuttton = types.InlineKeyboardButton(text="назад", callback_data="first")
        keyboard.add(rov2, rov3, rov4, rov5, rov6, backbuttton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Выберите регион :", reply_markup=keyboard)
    elif call.data == "снгГород":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        for key,value in dictnk.items():
            print(key)
            vizov=key
            a = types.InlineKeyboardButton(text=repr(key)+" "+repr("{:,}".format(value))+"", callback_data=vizov)
            keyboard.add(a)
        backbuttton = types.InlineKeyboardButton(text="назад", callback_data="first")
        keyboard.add(backbuttton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="sadfdsafasdfsad", reply_markup=keyboard)
    elif call.data == "пм":
        str = str + "Продажа по регионам"
        q = '''
            ВЫБРАТЬ
                РасчетыОбороты.Клиент.Наименование КАК Clien,
    			РасчетыОбороты.Клиент.КодАльфа2 КАК kodalfa2,
    			РасчетыОбороты.СуммаПриход КАК sum
    		ИЗ
    		    РегистрНакопления.Расчеты.Обороты(''' + nachprm + ''', ''' + konprm + ''', , ) КАК РасчетыОбороты
            '''
        query = V83.NewObject("Query", q)
        sel = query.Execute().Choose()
        dictkk.clear()
        dictnk.clear()
        dictsk.clear()
        dictuk.clear()
        dictob.clear()
        sumprodreg = 0
        sumprodkorp = 0
        sumprodgor = 0
        sumprodstar = 0
        sumprodobsh = 0
        while sel.next():
            print(repr(sel.kodalfa2))
            print(repr(sel.sum))
            if repr(sel.kodalfa2) == "'УК'":
                sumprodreg = sumprodreg + sel.sum
                sumprodobsh = sumprodobsh + sel.sum
                dictuk[sel.Clien] = sel.sum
                dictob.update(dictuk)
            elif repr(sel.kodalfa2) == "'КК'":
                sumprodkorp = sumprodkorp + sel.sum
                sumprodobsh = sumprodobsh + sel.sum
                dictkk[sel.Clien] = sel.sum
                dictob.update(dictkk)
            elif repr(sel.kodalfa2) == "'НК'":
                sumprodgor = sumprodgor + sel.sum
                sumprodobsh = sumprodobsh + sel.sum
                dictnk[sel.Clien] = sel.sum
                dictob.update(dictnk)
            elif repr(sel.kodalfa2) == "'СК'":
                sumprodstar = sumprodstar + sel.sum
                sumprodobsh = sel.sum + sumprodobsh
                dictsk[sel.Clien] = sel.sum
                dictob.update(dictsk)
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        rov2 = types.InlineKeyboardButton(text="Регионы (" + repr("{:,}".format(sumprodreg)) + ")",
                                          callback_data="пмРегионы")  # +repr(sumprodreg)+")"
        rov3 = types.InlineKeyboardButton(text="Корпоротивные (" + repr("{:,}".format(sumprodkorp)) + ")", callback_data="пмКорпоротивные")
        rov4 = types.InlineKeyboardButton(text="Город (" + repr("{:,}".format(sumprodgor)) + ")", callback_data="мпГород")
        rov5 = types.InlineKeyboardButton(text="Старые Клиенты (" + repr("{:,}".format(sumprodstar)) + ")", callback_data="пмСтравыеКлиенты")
        rov6 = types.InlineKeyboardButton(text="Общий (" + repr("{:,}".format(sumprodobsh)) + ")", callback_data="пмОбщий")
        sumprodreg = 0
        sumprodkorp = 0
        sumprodgor = 0
        sumprodstar = 0
        sumprodobsh = 0
        backbuttton = types.InlineKeyboardButton(text="назад", callback_data="first")
        keyboard.add(rov2, rov3, rov4, rov5, rov6, backbuttton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Выберите регион :", reply_markup=keyboard)

    #пмРегионы
    elif call.data == "пмРегионы":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        for key,value in dictuk.items():
            print(key)
            vizov=key
            a = types.InlineKeyboardButton(text=repr(key)+" "+repr("{:,}".format(value))+"", callback_data=vizov)
            keyboard.add(a)
        backbuttton = types.InlineKeyboardButton(text="назад", callback_data="first")
        keyboard.add(backbuttton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="sadfdsafasdfsad", reply_markup=keyboard)
    elif call.data == "пмОбщий":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        for key,value in dictob.items():
            print(key)
            vizov=key
            a = types.InlineKeyboardButton(text=repr(key)+" -- "+repr("{:,}".format(value))+"", callback_data=vizov)
            keyboard.add(a)
        backbuttton = types.InlineKeyboardButton(text="назад", callback_data="first")
        keyboard.add(backbuttton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="sadfdsafasdfsad", reply_markup=keyboard)
    elif call.data == "пмСтравыеКлиенты":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        for key, value in dictsk.items():
            print(key)
            vizov = key
            a = types.InlineKeyboardButton(text=repr(key) + " " + repr("{:,}".format(value)) + "", callback_data=vizov)
            keyboard.add(a)
        backbuttton = types.InlineKeyboardButton(text="назад", callback_data="first")
        keyboard.add(backbuttton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="sadfdsafasdfsad", reply_markup=keyboard)
    elif call.data == "мпГород":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        for key,value in dictnk.items():
            print(key)
            vizov=key
            a = types.InlineKeyboardButton(text=repr(key)+" "+repr("{:,}".format(value))+"", callback_data=vizov)
            keyboard.add(a)
        backbuttton = types.InlineKeyboardButton(text="назад", callback_data="first")
        keyboard.add(backbuttton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="sadfdsafasdfsad", reply_markup=keyboard)
    elif call.data == "пмКорпоротивные":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        for key,value in dictkk.items():
            print(key)
            vizov=key
            a = types.InlineKeyboardButton(text=repr(key)+" "+repr("{:,}".format(value))+"", callback_data=vizov)
            keyboard.add(a)
        backbuttton = types.InlineKeyboardButton(text="назад", callback_data="first")
        keyboard.add(backbuttton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="sadfdsafasdfsad", reply_markup=keyboard)
    elif call.data == "снгКорпоротивные":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        for key,value in dictkk.items():
            print(key)
            vizov=key
            a = types.InlineKeyboardButton(text=repr(key)+" "+repr("{:,}".format(value))+"", callback_data=vizov)
            keyboard.add(a)
        backbuttton = types.InlineKeyboardButton(text="назад", callback_data="first")
        keyboard.add(backbuttton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="sadfdsafasdfsad", reply_markup=keyboard)
    #снмСтраые
    elif call.data == "снмСтраые":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        for key, value in dictsk.items():
            print(key)
            vizov = key
            a = types.InlineKeyboardButton(text=repr(key) + " " + repr("{:,}".format(value)) + "", callback_data=vizov)
            keyboard.add(a)
        backbuttton = types.InlineKeyboardButton(text="назад", callback_data="first")
        keyboard.add(backbuttton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="sadfdsafasdfsad", reply_markup=keyboard)
    elif call.data == "СнгСтарыеКлиенты":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        for key, value in dictsk.items():
            print(key)
            vizov = key
            a = types.InlineKeyboardButton(text=repr(key) + " " + repr("{:,}".format(value)) + "", callback_data=vizov)
            keyboard.add(a)
        backbuttton = types.InlineKeyboardButton(text="назад", callback_data="first")
        keyboard.add(backbuttton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="sadfdsafasdfsad", reply_markup=keyboard)
    elif call.data == "снгРегионы":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        for key,value in dictuk.items():
            print(key)
            vizov=key
            a = types.InlineKeyboardButton(text=repr(key)+" "+repr("{:,}".format(value))+"", callback_data=vizov)
            keyboard.add(a)
        backbuttton = types.InlineKeyboardButton(text="назад", callback_data="first")
        keyboard.add(backbuttton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="sadfdsafasdfsad", reply_markup=keyboard)

    elif call.data == "снмРегоины":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        for key,value in dictuk.items():
            print(key)
            vizov=key
            a = types.InlineKeyboardButton(text=repr(key)+" "+repr("{:,}".format(value))+"", callback_data=vizov)
            keyboard.add(a)
        backbuttton = types.InlineKeyboardButton(text="назад", callback_data="first")
        keyboard.add(backbuttton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="sadfdsafasdfsad", reply_markup=keyboard)
    elif call.data == "снмКорпоротивные":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        for key,value in dictkk.items():
            print(key)
            vizov=key
            a = types.InlineKeyboardButton(text=repr(key)+" "+repr("{:,}".format(value))+"", callback_data=vizov)
            keyboard.add(a)
        backbuttton = types.InlineKeyboardButton(text="назад", callback_data="first")
        keyboard.add(backbuttton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="sadfdsafasdfsad", reply_markup=keyboard)
    elif call.data == "снмГород":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        for key,value in dictnk.items():
            print(key)
            vizov=key
            a = types.InlineKeyboardButton(text=repr(key)+" "+repr("{:,}".format(value))+"", callback_data=vizov)
            keyboard.add(a)
        backbuttton = types.InlineKeyboardButton(text="назад", callback_data="first")
        keyboard.add(backbuttton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="sadfdsafasdfsad", reply_markup=keyboard)
    #снгОбщий
    elif call.data == "снгОбщий":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        for key,value in dictob.items():
            print(key)
            vizov=key
            a = types.InlineKeyboardButton(text=repr(key)+" -- "+repr("{:,}".format(value))+"", callback_data=vizov)
            keyboard.add(a)
        backbuttton = types.InlineKeyboardButton(text="назад", callback_data="first")
        keyboard.add(backbuttton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="sadfdsafasdfsad", reply_markup=keyboard)
    elif call.data == "снмОбщий":
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        for key,value in dictob.items():
            print(key)
            vizov=key
            a = types.InlineKeyboardButton(text=repr(key)+" "+repr("{:,}".format(value))+"", callback_data=vizov)
            keyboard.add(a)
        backbuttton = types.InlineKeyboardButton(text="назад", callback_data="first")
        keyboard.add(backbuttton)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="sadfdsafasdfsad", reply_markup=keyboard)
    elif call.data == vizov:
        keyboard = types.InlineKeyboardMarkup(row_width=1)

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="что еще хотите?", reply_markup=keyboard)
    for key, value in dictpr.items():
        if call.data == value:
            q = '''
            ВЫБРАТЬ
			    Номенклатура.Наименование КАК imya,
			    Номенклатура.Родитель.Код КАК kodr,
			    Номенклатура.Код КАК kod
		    ИЗ
			    Справочник.Номенклатура КАК Номенклатура
		    ГДЕ
			    Номенклатура.Родитель.Код = "'''+value+'''"
			    И Номенклатура.ЭтоГруппа = "ИСТИНА"
			    '''
            query = V83.NewObject("Query", q)
            sel = query.Execute().Choose()
            keyboard = types.InlineKeyboardMarkup(row_width=1)
            dictprpp = {}
            while sel.next():
                dictprpp[sel.imya] = sel.kod
                rol1 = types.InlineKeyboardButton(text=repr(sel.imya), callback_data=sel.kod)
                keyboard.add(rol1)
            backbuttton = types.InlineKeyboardButton(text="назад", callback_data="second")
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="выберите одно из пунктов")
            keyboard.add(backbuttton)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="выберите одно из пунктов", reply_markup=keyboard)
    for key, value in dictprpp.items():
        if call.data == value:
            q = '''
            ВЫБРАТЬ
                Номенклатура.Наименование КАК imya,
                Номенклатура.Родитель.Код КАК kodr,
            	Номенклатура.Код КАК kod
            ИЗ
                Справочник.Номенклатура КАК Номенклатура
            ГДЕ
                Номенклатура.Родитель.Код = "''' + value + '''"
                '''
            query = V83.NewObject("Query", q)
            sel = query.Execute().Choose()
            keyboard = types.InlineKeyboardMarkup(row_width=1)
            dictprpppf = {}
            while sel.next():
                dictprpppf[sel.imya] = sel.kod
                rol1 = types.InlineKeyboardButton(text=repr(sel.imya), callback_data=sel.kod)
                keyboard.add(rol1)
            backbuttton = types.InlineKeyboardButton(text="назад", callback_data="second")
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="выберите ПФ для производство")
            keyboard.add(backbuttton)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="выберите полуфабриката для производство", reply_markup=keyboard)
    for key, value in dictprpppf.items():
        if call.data == value:
            print(value)
            sampf=key
            q = '''
            ВЫБРАТЬ
                СпецификацииНоменклатуры.Код КАК kod,
                СпецификацииНоменклатуры.Наименование КАК imya
            ИЗ
                Справочник.СпецификацииНоменклатуры КАК СпецификацииНоменклатуры
            ГДЕ
                СпецификацииНоменклатуры.Владелец.Код = "''' + value + '''"
                '''
            query = V83.NewObject("Query", q)
            sel = query.Execute().Choose()
            keyboard = types.InlineKeyboardMarkup(row_width=1)
            dictprkk = {}
            while sel.next():
                dictprkk[sel.imya] = sel.kod
                rol1 = types.InlineKeyboardButton(text=repr(sel.imya), callback_data=sel.kod)
                keyboard.add(rol1)
            backbuttton = types.InlineKeyboardButton(text="назад", callback_data="second")
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="выберите калькуляцию")
            keyboard.add(backbuttton)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="выберите полуфабриката для производство", reply_markup=keyboard)
    for key, value in dictprkk.items():
        if call.data == value:
            print(value)
            kodpf=value
            q = '''
            ВЫБРАТЬ
		    	СпецификацииНоменклатурыИсходныеКомплектующие.Количество КАК kol,
		    	СпецификацииНоменклатурыИсходныеКомплектующие.Номенклатура.Код КАК kod,
		    	СпецификацииНоменклатурыИсходныеКомплектующие.Номенклатура.Наименование КАК imya,
		    	СпецификацииНоменклатуры.Код КАК kodr
		    ИЗ
		    	Справочник.СпецификацииНоменклатуры.ИсходныеКомплектующие КАК СпецификацииНоменклатурыИсходныеКомплектующие
				ЛЕВОЕ СОЕДИНЕНИЕ Справочник.СпецификацииНоменклатуры КАК СпецификацииНоменклатуры
				ПО СпецификацииНоменклатурыИсходныеКомплектующие.Ссылка = СпецификацииНоменклатуры.Ссылка
		    ГДЕ
		        СпецификацииНоменклатуры.Код = "''' + value + '''"
                '''
            query = V83.NewObject("Query", q)
            sel = query.Execute().Choose()
            keyboard = types.InlineKeyboardMarkup(row_width=1)
            dictprsos = {}
            plus1 = types.InlineKeyboardButton(text="*+1*", callback_data="plus1",)
            minus1 =types.InlineKeyboardButton(text="-1", callback_data="minus1")
            plus10 =types.InlineKeyboardButton(text="+10", callback_data="plus10")
            minus10 =types.InlineKeyboardButton(text="-10", callback_data="minus10")
            plus100 = types.InlineKeyboardButton(text="+100", callback_data="plus100")
            minus100 = types.InlineKeyboardButton(text="-100", callback_data="minus100")
            plus1000 = types.InlineKeyboardButton(text="+1000", callback_data="plus1000")
            minus1000 = types.InlineKeyboardButton(text="-1000", callback_data="minus1000")
            keyboard.row(plus1,plus10,minus10,minus1)
            keyboard.row(plus100, plus1000, minus1000, minus100)
            while sel.next():
                print(sel.kod)
                print(sel.imya)
                dictprsos[sel.imya] = sel.kod
                rol1 = types.InlineKeyboardButton(text=repr(sel.imya)+"--"+repr(sel.kol*0), callback_data=sel.kod)
                keyboard.add(rol1)
            pod_button = types.InlineKeyboardButton(text='''Подтвердить''', callback_data = "под")
            backbuttton = types.InlineKeyboardButton(text="назад", callback_data="second")
            keyboard.add(backbuttton,pod_button)
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="установите количество и утвердите производство")
            bot.edit_message_text( chat_id=call.message.chat.id, message_id=call.message.message_id,text="Установите количество " +sampf+":"+repr(kolpf), reply_markup=keyboard)
    if call.data == "plus1":
        print("no problem here")
        kolpf=kolpf+1
        posledn(dictprkk, call,kodpf,sampf)
    if call.data == "minus1":
        #print("no problem here")
        kolpf=kolpf-1
        posledn(dictprkk, call,kodpf,sampf)
    if call.data == "plus10":
        #print("no problem here")
        kolpf=kolpf+10
        posledn(dictprkk, call,kodpf,sampf)
    if call.data == "minus10":
        #print("no problem here")
        kolpf=kolpf-10
        posledn(dictprkk, call,kodpf,sampf)
    if call.data == "plus100":
        kolpf = kolpf+100
        posledn(dictprkk, call, kodpf, sampf)
    if call.data == "minus100":
        kolpf = kolpf-100
        posledn(dictprkk, call,kodpf,sampf)
    if call.data == "plus1000":
        kolpf = kolpf+1000
        posledn(dictprkk, call,kodpf,sampf)
    if call.data == "minus1000":
        kolpf = kolpf-1000
        posledn(dictprkk, call,kodpf,sampf)
    if call.data == "под":
        bot.send_message(chat_id=792481457,text="*ваш заказ принят и отпрален на обработку✅*", parse_mode='Markdown')



if __name__== "__main__":
        bot.polling(none_stop=True)
