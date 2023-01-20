# Создайте программу для игры с конфетами человек против человека.
#
# Условие задачи: На столе лежит заданное количество конфет. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
#  Все конфеты оппонента достаются сделавшему последний ход.
#
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'

from random import randint

candies = int(input('Введите кол-во конфет: '))
j = 28
x = int(input('Жеребьевка!\nВведите 0 или 1: '))
rnd = randint(0, 1)
if x == rnd:
    print(f'Загаданное число: {rnd}. Вы угадали, ходите первым!')
    while candies > 0:
        while True:
            res = input('Введите кол-во конфет от 1 до 28:\n')
            if res.isdigit():
                if 0 < int(res) < 29 and int(res) <= candies:
                    candies -= int(res)
                    break
                else:
                    print('Неправильное колличество!')
            else:
                print('Вы ввели не число!')
        if not candies:
            print('Вы победили!')
            break
        if not candies % (j + 1):
            res = randint(1, 28)
        else:
            res = candies % (j + 1)
        candies -= res
        print(f'Ваш аппонент взял:\n{res}')
        if not candies:
            print('Вы проиграли :(')
            break
        print(f'Остаток конфет равен:\n{candies}')
else:
    print(f'Загаданное число: {rnd}. Вы не угадали,первым ходит ваш оппонент.')
    while candies > 0:
        if not candies % (j + 1):
            res = randint(1, 28)
        else:
            res = candies % (j + 1)
        candies -= res
        print(f'Ваш аппонент взял:\n{res}')
        if not candies:
            print('Вы проиграли :(')
            break
        print(f'Остаток конфет равен:\n{candies}')
        while True:
            res = input('Введите кол-во конфет от 1 до 28:\n')
            if res.isdigit():
                if 0 < int(res) < 29 and int(res) <= candies:
                    candies -= int(res)
                    break
                else:
                    print('Неправильное колличество!')
            else:
                print('Вы ввели не число!')
        if not candies:
            print('Вы победили!')
