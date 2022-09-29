import json
from cgitb import text
from xmlrpc.client import boolean
from progress.bar import Bar
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
import model_iD

def add_book(update: Update, context: CallbackContext):
    p = [[{"RID":0}, {"RФ.И.О": ""}, {"Rтел.": ""}]]
    with open(f'book.json', 'w', encoding='utf-8') as book:
        book.write(json.dumps(p , ensure_ascii=False))
    update.message.reply_text(f'Новая книга создана.')

def add_name(update: Update, context: CallbackContext): # Добавить имя
    name = [{"ID": model_iD.iD_name()},{"Ф.И.О.":update.message.text[6:]}]
    p = [[{"RID":0}, {"RФ.И.О": ""}, {"Rтел.": ""}]]
    with open("book.json", "r", encoding = 'utf-8') as read_file:
        data = list(json.load(read_file))
    if data == p:
        data.append(name)
        with open("book.json", "w", encoding = 'utf-8') as read_file:
            read_file.write(json.dumps(data , ensure_ascii=False))
            update.message.reply_text(f'{name[1]["Ф.И.О."]} добавлено.')
    else:
        if ("тел." in data[-1][-1]) or ("Rтел." in data[-1][-1]):
            data.append(name)
            with open("book.json", "w", encoding = 'utf-8') as read_file:
                read_file.write(json.dumps(data , ensure_ascii=False))
                update.message.reply_text(f'{name[1]["Ф.И.О."]} добавлено.')
        else:
            update.message.reply_text(f'Вы не добавили номер телефона для {data[-1][1]["Ф.И.О."]} \nДобавить номер телефона /tel "Телефон".')

def add_tel(update: Update, context: CallbackContext): # Добавить телефон
    tel = {'тел.':update.message.text[5:]}
    with open("book.json", "r", encoding = 'utf-8') as read_file:
        data = list(json.load(read_file))
        temp = list(data[-1])
        temp.append(tel)
        data.pop()
        data.append(temp)
    with open("book.json", "w", encoding = 'utf-8') as read_file:
        read_file.write(json.dumps(data , ensure_ascii=False))
        update.message.reply_text(f'К Ф.И.О.: {data[-1][1]["Ф.И.О."]} добавлен телефон: {str(update.message.text[5:])}.')
