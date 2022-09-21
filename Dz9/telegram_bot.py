import json
from cgitb import text
from xmlrpc.client import boolean
from isOdd import isOdd
from progress.bar import Bar
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
import random

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

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Для начала введи: /hello, чтобы познакомиться с ботом.')

def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Привет {update.effective_user.first_name}. \nЯ готов к работе. \nВведи команду /game если хочешь поиграть в конфеты.')

def game(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'{update.effective_user.first_name}, начнём игру в конфетки. \nНа столе лежит 2021 конфета. \nБрать можно не более 28 конфет за раз. \nКто заберёт последнюю конфету тот и выиграл.')
    name = {'Player_1': update.effective_user.first_name}
    result = {'Result_1': 0}
    name_list = []
    name_list.append(name)
    name_list.append(result)
    with open("players_name.json", "w", encoding = 'utf-8') as book:
        book.write(json.dumps(name_list , ensure_ascii=False))
    update.message.reply_text(f'Введите имя второго игрока.')

def name(update: Update, context: CallbackContext):
    name = {'Player_2': update.message.text}
    result = {'Result_2': 0}
    candies = {'Left': 2021}
    with open("players_name.json", "r", encoding = 'utf-8') as read_file:
        data = list(json.load(read_file))
    data.append(name)
    data.append(result)
    data.append(candies)
    with open("players_name.json", "w", encoding = 'utf-8') as book:
        book.write(json.dumps(data , ensure_ascii=False))
    update.message.reply_text(f'Команда "/first" определит кто первым ходит.')
    
def first_player(update: Update, context: CallbackContext) -> None:
    f = bool(random.choice([True, False]))
    enter = {'Enter': 1}
    with open("players_name.json", "r", encoding = 'utf-8') as read_file:
        data = list(json.load(read_file))
    first = {'First_player': f}
    data.append(first)
    data.append(enter)
    with open("players_name.json", "w", encoding = 'utf-8') as book:
        book.write(json.dumps(data , ensure_ascii=False))
    update.message.reply_text(f'Введите "/step" 0 и игра начнётся.')

def new_game(update: Update, context: CallbackContext) -> None:
    with open("players_name.json", "r", encoding = 'utf-8') as read_file:
        data = list(json.load(read_file))
    step = update.message.text[6:]
    step = int(step)
    if (data[5]["First_player"] == False) and (step < data[4]["Left"]):
        data[1]["Result_1"] += step
    elif (data[5]["First_player"] == True) and (step < data[4]["Left"]):
        data[3]["Result_2"] += step
    if data[6]["Enter"] == 1:
        if data[5]["First_player"] == True:
            update.message.reply_text(f'По результатам рандомайзера, первым ходит {data[0]["Player_1"]}.')
            data[6]["Enter"] = 0
            data[5]["First_player"] = not data[5]["First_player"]
        else:
            update.message.reply_text(f'По результатам рандомайзера, первым ходит {data[2]["Player_2"]}.')
            data[6]["Enter"] = 0
            data[5]["First_player"] = not data[5]["First_player"]
    else:
        if data[5]["First_player"] == True:
            update.message.reply_text(f'{data[0]["Player_1"]}, делай ход.')
        else:
            update.message.reply_text(f'{data[2]["Player_2"]}, делай ход.')
        if data[4]["Left"] >= 0 and data[4]["Left"] >= step:
            if step <= 28:
                data[4]["Left"] -= step
                data[5]["First_player"] = not data[5]["First_player"]
            else:
                update.message.reply_text(f'Вы взяли слишком много конфет. Введите "/step Количество конфет".')
        else:
            update.message.reply_text(f'Осталось {data[4]["Left"]} конфет, вы пытаетесь взять {step} конфет. Введите "/step Количество конфет".')
    update.message.reply_text(f'Осталось {data[4]["Left"]} конфет. Введите "/step Количество конфет".')
    if (data[5]["First_player"] == False) and (data[4]["Left"] == 0):
        update.message.reply_text(f'Выиграл {data[2]["Player_2"]}.')
        update.message.reply_text(f'/start.')
    elif (data[5]["First_player"] == True) and (data[4]["Left"] == 0):
        update.message.reply_text(f'Выиграл {data[0]["Player_1"]}.')
        update.message.reply_text(f'/start.')
    with open("players_name.json", "w", encoding = 'utf-8') as book:
        book.write(json.dumps(data , ensure_ascii=False))

updater = Updater('5693527498:AAGfWjMpTQGj8DuQVoeWzxPCFq_vXVNQtwk')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('game', game))
updater.dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), name))
updater.dispatcher.add_handler(CommandHandler('first', first_player))
updater.dispatcher.add_handler(CommandHandler('step', new_game))

print('server start')
updater.start_polling()
updater.idle()
