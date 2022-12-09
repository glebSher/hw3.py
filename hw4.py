# 1.	Вычислить число c заданной точностью d

# from math import pi
#
# d = int(input("Задайте точность числа Пи:\n"))
# print(f'число Пи с заданной точностью {d} равно {round(pi, d)}')


# 2.	Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

# num = int(input("Введите число: "))
# i = 2
# sp = []
# start = num
# while i <= num:
#     if num % i == 0:
#         sp.append(i)
#         num //= i
#         i = 2
#     else:
#         i += 1
# print(f"Простые множители числа {start} приведены в списке: {sp}")


# 3.	Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# sp = list(map(int, input("Введите числа через пробел:\n").split()))
# print(f"Исходный список: {sp}")
# new_sp = []
# [new_sp.append(i) for i in sp if i not in new_sp]
# print(f"Список из неповторяющихся элементов: {new_sp}")


# 4.	Задана натуральная степень k. Сформировать случайным образом
# список коэффициентов (значения от 0 до 100) многочлена и записать
# в файл многочлен степени k.

# import random
#
# def write_file(st):
#     with open('hw4_task4.txt', 'w') as data:
#         data.write(st)
#
# def rnd():
#     return random.randint(0, 101)
#
# def create_mn(k):
#     lst = [rnd() for i in range(k + 1)]
#     return lst
#
# def create_str(sp):
#     lst = sp[::-1]
#     wr = ''
#     if len(lst) < 1:
#         wr = 'x = 0'
#     else:
#         for i in range(len(lst)):
#             if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
#                 wr += f'{lst[i]}x^{len(lst) - i - 1}'
#                 if lst[i + 1] != 0:
#                     wr += ' + '
#             elif i == len(lst) - 2 and lst[i] != 0:
#                 wr += f'{lst[i]}x'
#                 if lst[i + 1] != 0:
#                     wr += ' + '
#             elif i == len(lst) - 1 and lst[i] != 0:
#                 wr += f'{lst[i]} = 0'
#             elif i == len(lst) - 1 and lst[i] == 0:
#                 wr += ' = 0'
#     return wr
#
# k = int(input("Введите натуральную степень k = "))
# koef = create_mn(k)
# write_file(create_str(koef))


# 5.	Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

with open('hw4_task5_1.txt', 'w', encoding='utf-8') as file:
    file.write('2*x^2 + 5*x^5')
with open('hw4_task5_2.txt', 'w', encoding='utf-8') as file:
    file.write('23*x^4 + 9*x^6')

with open('hw4_task5_1.txt','r') as file:
    poly_1 = file.readline()
    list_of_poly_1 = poly_1.split()


with open('hw4_task5_2.txt','r') as file:
    poly_2 = file.readline()
    list_of_poly_2 = poly_2.split()

print(f'{list_of_poly_1} + {list_of_poly_2}')
sum_poly = list_of_poly_1 + list_of_poly_2

with open('hw4_task5_sum.txt', 'w', encoding='utf-8') as file:
    file.write(f'{list_of_poly_1} + {list_of_poly_2}')