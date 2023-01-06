# СЧИТЫВАНИЕ ФАЙЛА csv ПОСТРОЧНО
import csv
# with open('file.csv', encoding="utf-8") as csvfile:
#     reader = csv.reader(csvfile, delimiter=';')
#     title = next(reader)
#     sp = list(reader)
#     for row in sp:
#         print(row)

# ЧТЕНИЕ В СЛОВАРЬ
# with open('file.csv', encoding="utf-8") as csvfile:
#     reader = csv.DictReader(csvfile, delimiter=';')
#     expensive = sorted(reader, key=lambda x: int(x['price']), reverse=True)
#
# for record in expensive:
#     print(record)

# ЗАПИСЬ В ФАЙЛ (w - перезапись, a - добавление)
# with open('file.csv', 'w', encoding="utf-8", newline='') as csvfile:
#     writer = csv.writer(csvfile, delimiter=';')
#     row0 = ['product', 'price', 'brend']
#     row1 = ['колбаса', 500, 'Микоян']
#     row2 = ['йогурт', 34, 'Данон']
#     writer.writerow(row0)
#     writer.writerow(row1)
#     writer.writerow(row2)

# ЗАПИСЬ ЧЕРЕЗ СЛОВАРЬ
data = [{
    'lastname': 'Иванов',
    'firstname': 'Иван',
    'class_number': '9',
    'class_letter': 'A'
}, {
    'lastname': 'Петров',
    'firstname': 'Петр',
    'class_number': '9',
    'class_letter': 'B'
}, {
    'lastname': 'Васильева',
    'firstname': 'Василиса',
    'class_number': '9',
    'class_letter': 'A'
}]
with open('dictwriter.csv', 'w', encoding="utf-8", newline='') as dict_f:
    writer = csv.DictWriter(
        dict_f, fieldnames=list(data[0].keys()),
        delimiter=';')
    writer.writeheader()
    for d in data:
        writer.writerow(d)
