import json
from cgitb import text
from xmlrpc.client import boolean
from progress.bar import Bar
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
import bot_add
import modul_search
import modul_del
import modul_read

updater = Updater('5693527498:AAGfWjMpTQGj8DuQVoeWzxPCFq_vXVNQtwk')

# Done! Congratulations on your new bot. You will find it at t.me/My_New_355_bot. 
# You can now add a description, about section and profile picture for your bot, see /help for a list of commands. 
# By the way, when you've finished creating your cool bot, ping our Bot Support if you want a better username for it. 
# Just make sure the bot is fully operational before you do this.

# Use this token to access the HTTP API:
# 5693527498:AAGfWjMpTQGj8DuQVoeWzxPCFq_vXVNQtwk
# Keep your token secure and store it safely, it can be used by anyone to control your bot.

# For a description of the Bot API, see this page: https://core.telegram.org/bots/api

# Anton Popov, [14.09.2022 19:36]

# Bot Name: My_New_355_bot


# Команды
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'\nЯ бот телефонная книга.\nДля начала введи: /help, чтобы узнать команды.')
def help(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Привет {update.effective_user.first_name}.\nМои команды:\n/help - вывести все команды.\n/add - добавление в телефонную книгу.\n/del - удалить человека из телефонной книги.\n/read - редактировать телефонную книгу.\n/search - поиск по телефонной книге.\n/book - отобразить телефонную книгу.')
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))

# создание телефонной книги
def add_all(update: Update, context: CallbackContext):
    update.message.reply_text(f'Создать телефонную книгу /new. СТАРАЯ КНИГА УДАЛИТСЯ\nДобавить Ф.И.О. /name "Ф.И.О.".\nДобавить номер телефона /tel "Телефон"')
updater.dispatcher.add_handler(CommandHandler('add', add_all))
updater.dispatcher.add_handler(CommandHandler('new', bot_add.add_book))
updater.dispatcher.add_handler(CommandHandler('name', bot_add.add_name))
updater.dispatcher.add_handler(CommandHandler('tel', bot_add.add_tel))

# поиск по телефонной книге
def search(update: Update, context: CallbackContext):
    update.message.reply_text(f'/sid "iD" - найти по iD.\n/sname "Ф.И.О." - найти по имени.\n/stel "Телефон" - найти по номеру телефона.')
updater.dispatcher.add_handler(CommandHandler('search', search))
updater.dispatcher.add_handler(CommandHandler('sid', modul_search.sid))
updater.dispatcher.add_handler(CommandHandler('sname', modul_search.sname))
updater.dispatcher.add_handler(CommandHandler('stel', modul_search.stel))

# удаление из телефонной книги
def delet(update: Update, context: CallbackContext):
    update.message.reply_text(f'/did "iD" - удалить по iD.\n/dname "Ф.И.О." - удалить по имени.\n/dtel "Телефон" - удалить по номеру телефона.')
updater.dispatcher.add_handler(CommandHandler('del', delet))
updater.dispatcher.add_handler(CommandHandler('did', modul_del.did))
updater.dispatcher.add_handler(CommandHandler('dname', modul_del.dname))
updater.dispatcher.add_handler(CommandHandler('dtel', modul_del.dtel))

# редактирование книги
def read(update: Update, context: CallbackContext):
    update.message.reply_text(f'/rid "iD" - редактировать iD.\n/rname "Ф.И.О." - редактировать Ф.И.О.\n/rtel "Телефон" - редактировать номер телефона.')
updater.dispatcher.add_handler(CommandHandler('read', read))
updater.dispatcher.add_handler(CommandHandler('rid', modul_read.rid))
updater.dispatcher.add_handler(CommandHandler('rname', modul_read.rname))
updater.dispatcher.add_handler(CommandHandler('rtel', modul_read.rtel))

# показать книгу
def book(update: Update, context: CallbackContext):
    with open("book.json", "r", encoding = 'utf-8') as read_file:
        data = list(json.load(read_file))
    for e in data:
        update.message.reply_text(f'{e}.')
updater.dispatcher.add_handler(CommandHandler('book', book))

print('server start')
updater.start_polling()
updater.idle()
