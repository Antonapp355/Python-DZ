import json
from cgitb import text
from xmlrpc.client import boolean
from progress.bar import Bar
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

def did(update: Update, context: CallbackContext):
    with open("book.json", "r", encoding = 'utf-8') as read_file:
        data = list(json.load(read_file))
    search = update.message.text
    temp = bool
    if "/did" in search:
        number_ID = int(update.message.text[4:])
        for e in data:
            for i in e:
                if "RID" in i:
                    continue
                elif ("ID" in i) and (search in i["ID"]):
                    update.message.reply_text(str(e))
                    temp = True
                    data.remove(e)
                    with open(f'book.json', 'w', encoding='utf-8') as book:
                        book.write(json.dumps(data , ensure_ascii=False))
                        update.message.reply_text(f'Удалено.')
                    break
                else:
                    temp = False
    if temp == False:
        update.message.reply_text('Такого ID не существует в книге. Попробуйте ещё раз.')
        


def dname(update: Update, context: CallbackContext):
    with open("book.json", "r", encoding = 'utf-8') as read_file:
        data = list(json.load(read_file))
    search = update.message.text
    temp = bool
    if "/dname" in search:
        name = str(update.message.text[7:])
        for e in data:
            for i in e:
                if "RФ.И.О." in i:
                    continue
                elif ("Ф.И.О." in i) and (search in i["Ф.И.О."]):
                    update.message.reply_text(str(e))
                    temp = True
                    data.remove(e)
                    with open(f'book.json', 'w', encoding='utf-8') as book:
                        book.write(json.dumps(data , ensure_ascii=False))
                        update.message.reply_text(f'Удалено.')
                    break
                else:
                    temp = False
    if temp == False:
        update.message.reply_text('Такого Ф.И.О. не существует в книге. Попробуйте ещё раз.')

def dtel(update: Update, context: CallbackContext):
    with open("book.json", "r", encoding = 'utf-8') as read_file:
        data = list(json.load(read_file))
    temp = bool
    tel = update.message.text
    if "/dtel" in tel:
        tel = str(update.message.text[6:])
        for e in data:
            for i in e:
                if "Rтел." in i:
                    continue
                elif ("тел." in i) and (i["тел."] == tel):
                    update.message.reply_text(str(e))
                    temp = True
                    data.remove(e)
                    with open(f'book.json', 'w', encoding='utf-8') as book:
                        book.write(json.dumps(data , ensure_ascii=False))
                        update.message.reply_text(f'Удалено.')
                    break
                else:
                    temp = False
    if temp == False:
        update.message.reply_text('Такого телефона не существует в книге. Попробуйте ещё раз.')