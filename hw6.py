# 1.	Наибольший общий делитель.
# В модуле math есть функция math.gcd(a, b), возвращающая наибольший общий делитель
# (НОД) двух чисел. Вычислите и напечатайте наибольший общий делитель для списка
# натуральных чисел. Ввод чисел продолжается до ввода пустой строки.
# Входные данные: 36, 12, 144, 18

# from math import gcd
#
# numbers_sp = [36, 12, 144, 18]
# print(gcd(*numbers_sp))


# 2.	Орел и решка
# Дана строка текста, состоящая из букв русского алфавита "О" и "Р". Буква "О" – соответствует
# выпадению Орла, а буква "Р" – соответствует выпадению Решки. Напишите программу, которая
# подсчитывает наибольшее количество подряд выпавших Решек.
# Формат входных данных:
# На вход программе подается строка текста, состоящая из букв русского алфавита "О" и "Р".
# Формат выходных данных:
# Программа должна вывести наибольшее количество подряд выпавших Решек.
# Примечание. Если выпавших Решек нет, то необходимо вывести число 0.

# str = input('Введите текст: ').split(sep='О')
# result = list(filter(lambda x: 'Р' in x, str))
# print(len(max(result)))


# 3.	Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# sp = [1, 2, 3, 4, 5, 3, 2]
# print(sp)
# new_sp = []
# new_sp = list(filter(lambda x: sp.count(x) == 1, sp))
# print(new_sp)

