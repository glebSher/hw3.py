# 2.	Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому
# игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

import random

name1 = input('Введите имя первого игорока: ')
name2 = input('Введите имя второго игорока: ')

candy = int(input('Введите кличество конфет на столе: '))

play = random.randint(1, 3)
if play == 1:
    print('Первый ход делает ', name1)
else:
    print('Первый ход делает ', name2)

while candy > 0:
    if candy > 28:
        player1 = int(input('Ваш ход. Возьмите не более 28 конфет'))
        candy = candy - player1
        if candy > 28:
            player2 = int(input('Ваш ход. Возьмите не более 28 конфет'))
            candy = candy - player2
            if candy <= 28:
                if play == 1:
                    print('Победил игрок', name1)
                else:
                    print('Победил игрок', name2)
        else:
            if play == 1:
                print('Победил игрок', name2)
            else:
                print('Победил игрок', name1)