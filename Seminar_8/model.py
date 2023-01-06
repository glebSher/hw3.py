import csv


def get_all():
    with open('task_file.csv', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        # sp = list(reader)
        return list(reader)


def add_data(employee):
    with open('task_file.csv', 'a', encoding="utf-8", newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(employee)


def change_data(number, new_data):
    try:
        with open('task_file.csv', 'r', encoding="utf-8", newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            data = list(reader)
            data[number] = new_data
        with open('task_file.csv', 'w', encoding="utf-8", newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            for i in data:
                writer.writerow(i)
    except IndexError:
        print('Вы вышли за пределы списка')
        exit()
    except Exception:
        print('Что-то пошло не так =(')
        exit()


def delete_data(number):
    with open('task_file.csv', 'r', encoding="utf-8", newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        data = list(reader)
        del data[number]
    with open('task_file.csv', 'w', encoding="utf-8", newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        for i in data:
            writer.writerow(i)


def export_list_txt():
    with open('task_file.csv', 'r', encoding="utf8", newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        list_employees = list(reader)
    with open('list-employees.txt', 'w', encoding="utf-8") as data:
        for i in list_employees:
            for j in i:
                data.write(j + ' ')
            data.write('\n')

def import_list_txt():
    with open('list-employees.txt', 'r', encoding='utf-8') as data:
        for row in data:
            print(row)

def import_list_csv():
    with open("task_file.csv", encoding='utf-8') as r_file:
        file_reader = csv.DictReader(r_file, delimiter=";")
        count = 0
        for row in file_reader:
            if count == 0:
                print(f'Информация по следующим столбцам:\n {", ".join(row)}')
            print(f' {row["Фамилия"]} {row["Имя"]}, {row["Телефон"]}, {row["Должность"]}')
            count += 1