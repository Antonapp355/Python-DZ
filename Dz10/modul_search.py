import json
from cgitb import text
from xmlrpc.client import boolean
from progress.bar import Bar
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

def sid(update: Update, context: CallbackContext):
    with open("book.json", "r", encoding = 'utf-8') as read_file:
        data = list(json.load(read_file))
    search = update.message.text
    temp = bool
    if "/sid" in search:
        number_ID = int(update.message.text[4:])
        for e in data:
            if e[0]["ID"] == number_ID:
                update.message.reply_text(str(e))
                temp = True
                data[0][0]["RID"] = e[0]["ID"]
                data[0][1]["RФ.И.О"] = e[1]["Ф.И.О."]
                data[0][2]["Rтел."] = e[2]["тел."]
                with open(f'book.json', 'w', encoding='utf-8') as book:
                    book.write(json.dumps(data , ensure_ascii=False))
                    update.message.reply_text(f'/rid "iD" - редактировать iD.')
                break
            else:
                temp = False
    if temp == False:
        update.message.reply_text('Такого ID не существует в книге. Попробуйте ещё раз.')


def sname(update: Update, context: CallbackContext):
    with open("book.json", "r", encoding = 'utf-8') as read_file:
        data = list(json.load(read_file))
    search = update.message.text
    temp = bool
    if "/sname" in search:
        name = str(update.message.text[7:])
        for e in data:
                for i in e:
                    if ("Ф.И.О." in i) and (i["Ф.И.О."] == name):
                        update.message.reply_text(str(e))
                        temp = True
                        data[0][0]["RID"] = e[0]["ID"]
                        data[0][1]["RФ.И.О"] = e[1]["Ф.И.О."]
                        data[0][2]["Rтел."] = e[2]["тел."]
                        with open(f'book.json', 'w', encoding='utf-8') as book:
                            book.write(json.dumps(data , ensure_ascii=False))
                            update.message.reply_text(f'/rid "iD" - редактировать iD.\n/rname "Ф.И.О." - редактировать Ф.И.О.\n/rtel "Телефон" - редактировать номер телефона.')
                        break
                    else:
                        temp = False
    if temp == False:
        update.message.reply_text('Такого Ф.И.О. не существует в книге. Попробуйте ещё раз.')

def stel(update: Update, context: CallbackContext):
    with open("book.json", "r", encoding = 'utf-8') as read_file:
        data = list(json.load(read_file))
    temp = bool
    tel = update.message.text
    if "/stel" in tel:
        tel = str(update.message.text[6:])
        for e in data:
            for i in e:
                if ("тел." in i) and (i["тел."] == tel):
                    update.message.reply_text(str(e))
                    temp = True
                    data[0][0]["RID"] = e[0]["ID"]
                    data[0][1]["RФ.И.О"] = e[1]["Ф.И.О."]
                    data[0][2]["Rтел."] = e[2]["тел."]
                    with open(f'book.json', 'w', encoding='utf-8') as book:
                        book.write(json.dumps(data , ensure_ascii=False))
                        update.message.reply_text(f'/rid "iD" - редактировать iD.\n/rname "Ф.И.О." - редактировать Ф.И.О.\n/rtel "Телефон" - редактировать номер телефона.')
                    break
                else:
                    temp = False
    if temp == False:
        update.message.reply_text('Такого телефона не существует в книге. Попробуйте ещё раз.')