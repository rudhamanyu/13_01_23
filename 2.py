# Создайте программу для игры в 'Крестики-нолики'
# НЕОБЯЗАТЕЛЬНО Добавить игру против бота с интеллектом

dct = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}
data_x = ''
data_o = ''
data = ''
t = True  # переменная перехода хода
o = None  # клетка нолика
x = None  # клетка крестика
while True:
    key = 1  # переменная для нумерации клеток
    print()
    for i in range(3):
        my_str = ''
        for _ in range(1, 4):
            if x == key or dct[key] == 'X':
                my_str += 'X' + ' | '
                value = 'X'
            elif o == key or dct[key] == '0':
                my_str += '0' + ' | '
                value = '0'
            else:
                my_str += str(key) + ' | '
                value = key
            dct[key] = value
            key += 1
        print(my_str)
    print()
    if dct[1] == dct[5] == dct[9] or dct[3] == dct[5] == dct[7] \
            or dct[1] == dct[2] == dct[3] or dct[4] == dct[5] == dct[6] \
            or dct[7] == dct[8] == dct[9] or dct[1] == dct[4] == dct[7] \
            or dct[2] == dct[5] == dct[8] or dct[3] == dct[6] == dct[9]:
        print('Вы победили!\nИгра завершена.')
        break
    while True:
        if t % 2:
            x = int(input('Введите число от 1 до 9,чтобы поставить крестик: '))
            if dct[x] != 'X' and dct[x] != '0':
                t += 1
                break
            else:
                print('Эта клетка уже занята!')
        else:
            o = int(input('Введите число от 1 до 9,чтобы поставить нолик: '))
            if dct[o] != 'X' and dct[o] != '0':
                t += 1
                break
            else:
                print('Эта клетка уже занята!')
