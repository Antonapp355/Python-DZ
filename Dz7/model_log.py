from datetime import date
import model_datetime
from encodings import utf_8
import menu_model
import webbrowser
import os

def get_log(m):
    with open('log.txt', 'a+', encoding = 'utf-8') as fh:
        fh.write(f'\n ==================================================================== \n Datetime: {model_datetime.date_time()}; \n Operation: {m} \n ')

def show_log():
    os.startfile('log.txt')