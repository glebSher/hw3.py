def greeting():
    print('Hello, Выберите действие: 0 - калькулятор, 1 - конвертер')
    select = int(input())
    return select


def get_arithmetic_example():
    example = input('Введите выражение ')
    return example


def view_result(result):
    print('Результат = ', result)


def get_weight():
    weight = input('Введите массу в кг')
    return weight
