import json
from cgitb import text
from xmlrpc.client import boolean
from progress.bar import Bar
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters




def rid(update: Update, context: CallbackContext):
    with open("book.json", "r", encoding = 'utf-8') as read_file:
        data = list(json.load(read_file))
    read_ID = update.message.text[4:]
    read_data = str(data[0][1]["RID"])
    for e in data:
        for i in e:
            if "RID" in i:
                continue
            elif ("ID" in i) and (read_data in i["ID"]):
                i["ID"] = read_ID
                data[0] = [[{"RID":0}, {"RФ.И.О": ""}, {"Rтел.": ""}]]
                with open(f'book.json', 'w', encoding='utf-8') as book:
                    book.write(json.dumps(data , ensure_ascii=False))
                    update.message.reply_text(f'Отредактировано.\n {e}.')
        


def rname(update: Update, context: CallbackContext):
    with open("book.json", "r", encoding = 'utf-8') as read_file:
        data = list(json.load(read_file))
    read_name = update.message.text[7:]
    read_data = str(data[0][1]["RФ.И.О."])
    for e in data:
        for i in e:
            if "RФ.И.О." in i:
                continue
            elif ("Ф.И.О." in i) and (read_data in i["Ф.И.О."]):
                i["Ф.И.О."] = read_name
                data[0] = [[{"RID":0}, {"RФ.И.О": ""}, {"Rтел.": ""}]]
                with open(f'book.json', 'w', encoding='utf-8') as book:
                    book.write(json.dumps(data , ensure_ascii=False))
                    update.message.reply_text(f'Отредактировано.\n {e}.')

def rtel(update: Update, context: CallbackContext):
    with open("book.json", "r", encoding = 'utf-8') as read_file:
        data = list(json.load(read_file))
    read_tel = update.message.text[6:]
    read_data = str(data[0][2]["Rтел."])
    print(read_data)
    for e in data:
        for i in e:
            if "Rтел." in i:
                continue
            elif ("тел." in i) and (read_data in i["тел."]):
                i["тел."] = read_tel
                data[0] = [[{"RID":0}, {"RФ.И.О": ""}, {"Rтел.": ""}]]
                with open(f'book.json', 'w', encoding='utf-8') as book:
                    book.write(json.dumps(data , ensure_ascii=False))
                    update.message.reply_text(f'Отредактировано.\n {e}.')