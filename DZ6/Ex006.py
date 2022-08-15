from array import *
import random

print('Давай сыграем в крестики нолики.')
Enter = str(input('Сыграть? Y/N ?:'))
player_1 = str
player_2 = str
temp = bool

def New_Game(Enter,player_1):
    if Enter == 'n' or Enter == 'N':
        print('Очень жаль.')
        print('Пока.')
        exit
    elif Enter == 'y' or Enter == 'Y':
        player_1 = str(input('Как тебя зовут?:'))
        print()
        print(f'Приветствую тебя, {player_1}!')
    print()
    return player_1
player_1 = New_Game(Enter,player_1)

def Player_Or_Bot(player_2): # Пока сложно бота добавить. Но я выбор сделал и зациклил если попробовать нажать Y.
    player_2 = str(input('Ты хочешь поиграть с ботом?(Либо введи имя второго игрока.)(Y,N):'))
    if player_2 == 'n' or Enter == 'N':
        print('Значит давай познакомимся со вторым игроком.')
        player_2 = str(input('Как зовут твоего друга?:'))
        print(f'Приветствую, {player_2}!')
    elif player_2 == 'y' or Enter == 'Y':
        print('Функция пока недоступна.')
        Player_Or_Bot(player_2)
    return player_2
player_2 = Player_Or_Bot(player_2)

def First_Player(player_1,player_2): # Жеребьёвка.
    spisok_rnd = []
    for e in range(5): # Создаём список из 5 рандомных чисел от 0 до 100.
        rnd = int(random.randint(0,100))
        spisok_rnd.append(rnd)
    rnd_player_1 = int(input(f'Определим кто будет ходить первым.{player_1} введите номер числа от 1 до 5:'))
    rnd_player_2 = int(input(f'{player_2} введите номер числа от 1 до 5:'))
    print(f'У {player_1} под номером {rnd_player_1} скрывалось число {spisok_rnd[rnd_player_1-1]}.')
    print(f'У {player_2} под номером {rnd_player_2} скрывалось число {spisok_rnd[rnd_player_2-1]}.')
    print()
    if spisok_rnd[rnd_player_1-1] > spisok_rnd[rnd_player_2-1]:
        print(f'У игрока {player_1} результат выше.')
        print(f'Первым ходится {player_1}.')
        temp = True
        return temp
    elif spisok_rnd[rnd_player_2-1] > spisok_rnd[rnd_player_1-1]:
        print(f'У игрока {player_2} результат выше.')
        print(f'Первым ходится {player_2}.')
        temp = False
        return temp
print()

temp = First_Player(player_1,player_2)
Enter = int(0)
print()
print('Если ходить уже нет смысла и большая часть поля заполнена, просто заполните поле до конца и игра закончится.')
print()
def Game(k,temp):
    character = str
    pole = [['_','_','_'],['_','_','_'],['_','_','_']]
    while k < 10:
        print(' №  1.   2.   3.')
        i = 1
        for e in pole:
            print(f'{i}.{e}')
            i += 1
        print()
        if k < 9:
            if temp == True:
                step = list(input(f'{player_1},(X) ведите номер строки и номер столбца через запятую (1,3):'))
                x = int(step[0])
                y = int(step[2])
                if pole[x-1][y-1] == 'X' or pole[x-1][y-1] == '0':
                    print('Поле занято. Выберите другое поле.')
                    Game(k,temp)
                pole[x-1][y-1] = 'X'
                character = 'X'
                if pole[0][0]==pole[0][1]==pole[0][2]==character or pole[0][0]==pole[1][1]==pole[2][2]==character or pole[0][0]==pole[1][0]==pole[2][0]==character or pole[0][0]==pole[1][0]==pole[2][0]==character or pole[0][2]==pole[1][2]==pole[2][2]==character or pole[0][0]==pole[1][1]==pole[2][2]==character or pole[0][2]==pole[1][1]==pole[2][0]==character or pole[2][0]==pole[2][1]==pole[2][2]==character:
                    i = 1
                    for e in pole:
                        print(f'{i}.{e}')
                        i += 1
                    print(f'{player_1}, вы победили.')
                    print(' №  1.   2.   3.')
                    k = 9
                    exit
            if temp == False:
                step = list(input(f'{player_2},(0) ведите номер строки и номер столбца через запятую (1,3):'))
                x = int(step[0])
                y = int(step[2])
                if pole[x-1][y-1] == 'X' or pole[x-1][y-1] == '0':
                    print('Поле занято. Выберите другое поле.')
                    Game(k,temp)
                pole[x-1][y-1] = '0'
                character = '0'
                if pole[0][0]==pole[0][1]==pole[0][2]==character or pole[0][0]==pole[1][1]==pole[2][2]==character or pole[0][0]==pole[1][0]==pole[2][0]==character or pole[0][0]==pole[1][0]==pole[2][0]==character or pole[0][2]==pole[1][2]==pole[2][2]==character or pole[0][0]==pole[1][1]==pole[2][2]==character or pole[0][2]==pole[1][1]==pole[2][0]==character or pole[2][0]==pole[2][1]==pole[2][2]==character:
                    i = 1
                    for e in pole:
                        print(f'{i}.{e}')
                        i += 1
                    print(f'{player_2}, вы победили.')
                    k = 9
                    exit
            if (pole[0][0] == 'X' or pole[0][0] == '0') and (pole[0][1] == 'X' or pole[0][1] == '0') and (pole[0][2] == 'X' or pole[0][2] == '0') and (pole[1][0] == 'X' or pole[1][0] == '0') and (pole[1][1] == 'X' or pole[1][1] == '0') and (pole[1][2] == 'X' or pole[1][2] == '0') and (pole[2][0] == 'X' or pole[2][0] == '0') and (pole[2][1] == 'X' or pole[2][1] == '0') and (pole[2][2] == 'X' or pole[2][2] == '0'):
                print('Ничья.')
                print('Конец.')
                k = 9
                exit
            temp = not temp
        k+=1
Game(Enter,temp)
