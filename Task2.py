# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# Человек против человека!!!
import random as ran


def swits (num, person):
    if num <= 28:
        print(f'\n Последний игрок забирает {num} конфет\n')
        return person
    else:
        print(f'\n Сейчас {num} конфет\n')
        if person ==1:
            n = int(input ('Первый игрок, возьмите конфеты : '))
            if n > 28:
                print ('Необходимо взять меньше конфет\n')
                return swits (num, person)
            else:
                return swits (num - n, 2)
        if person ==2:
            n = int(input ('Второй игрок, возьмите конфеты : '))
            if n > 28:
                print ('Необходимо взять меньше конфет\n')
                return swits (num, person)
            else:
                return swits (num-n, 1)

#а) Бот против человека
def swits_bot (num, person):
    if num <= 28:
        print(f'\n Последний игрок забирает {num} конфет\n')
        return person
    else:
        print(f'\n Сейчас {num} конфет\n')
        if person == 1:
            n = int(input ('Ваш шаг, возьмите конфеты : '))
            if n > 28:
                print ('Необходимо взять меньше конфет\n')
                return swits_bot (num, person)
            else:
                return swits_bot (num - n, 2)
        if person ==2:
            n = ran.randint(1, 29)
            
            if num >= 85:
                print (f'Bot взял {n} конфет\n')
                return swits_bot (num-n, 1)
            elif num == 29:
                n = ran.randint(1, 29)
                print (f'Bot взял {n} конфет\n')
                return swits_bot (num-n, 1)
            elif 57 <= num  < 85:
                n = 1
                print (f'Bot взял {n} конфет\n')
                return swits_bot (num-n, 1)

            else: 
                n = num - 29
                print(f'Bot взял {n} конфет')
                return swits_bot (num-n, 1)

num = int(input("Введите количество конфет на столе: "))
print\
    (f'На столе лежит {num} конфет(а). Играют два игрока делая ход друг после друга.\n'
      'Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.\nВсе конфеты' 
      'достаются сделавшему последний ход\n'
    )
start = input('Если нажать 1 - будете играть против человека, если 2, против бота : ')
choise = ran.randint(1,2)
print(f'{choise} игрок начинает')


if start == '1':
    print(f' Выиграл игрок № {swits(num, choise)}\n')
elif start == '2':
    n = swits_bot(num, choise)
    if n == 1:
        print('ПОЗДРАВЛЯЮ!!! Вы выиграли\n')
    else: print('Выиграл Bot\n')

