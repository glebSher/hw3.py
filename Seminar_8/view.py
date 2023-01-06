def show_menu():
    print('Выберите команду: \n'
          '1 - показать всех сотрудников\n'
          '2 - добавить сотрудника\n'
          '3 - изменить данные сотрудника\n'
          '4 - удалить сотрудника')
    try:
        select = int(input())
        if not select in [1, 2, 3, 4, 5, 6, 7]:
            raise ValueError
        return select
    except Exception:
        print('Всё пропало!!!')
        exit()


def show_all(personal):
    print('Список всех сотрудников:')
    for i, employee in enumerate(personal):
        if i == 0:
            print(' ', *employee)
        else:
            print(i, *employee)


def add_employee():
    print('Введите данные нового сотрудника (фамилия, имя, телефон, должность через пробел): ')
    data = input().split()
    return data


def change_employee():
    print('Выберите строку для изменения данных: ')
    employee_select = int(input())
    print('Введите новые данные для записи (через пробел): ')
    new_data = input().split()
    return employee_select, new_data


def delete_employee():
    print('Выберите строку для удаления данных: ')
    employee_delete = int(input())
    return employee_delete
