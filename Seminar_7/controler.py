from Seminar_7 import view, model
import logging

# from Seminar_7.view import greeting, get_arithmetic_example

# logging.basicConfig(level=logging.INFO)
logging.basicConfig(filename='log.txt',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO, encoding='utf-8')


def calculator_converter():
    try:
        select = view.greeting()
        if select == 0:
            logging.info('Выбран режим калькулятор')
            example = view.get_arithmetic_example()
            result = model.calculator(example)
            view.view_result(result)
            logging.info(f'Выведен результат {result}')
        elif select == 1:
            logging.info('Выбран режим конвертер')
            weight = view.get_weight()
            logging.info(f'Введено значение {weight}')
            value = model.converter(weight)
            view.view_result(value)
    except Exception:
        logging.warning('Введено некорректное значение')


logging.basicConfig(level=logging.INFO)
