import view
import model
import logging

logging.basicConfig(filename='log.txt',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO,
                    encoding='utf-8')


def main():
    select = view.show_menu()
    if select == 1:
        logging.info('Выбран режим показа всех сотрудников')
        personal = model.get_all()
        view.show_all(personal)
    elif select == 2:
        logging.info('Выбран режим добавления данных')
        data = view.add_employee()
        model.add_data(data)
    elif select == 3:
        logging.info('Выбран режим изменения данных')
        change, new_data = view.change_employee()
        model.change_data(change, new_data)
    elif select == 4:
        logging.info('Выбран режим удаления данных')
        delete = view.delete_employee()
        model.delete_data(delete)
    elif select == 5:
        logging.info("Выбран экспорт в txt")
        model.export_list_txt()
    elif select == 6:
        logging.info("Выбран импорт из txt")
        model.import_list_txt()
    elif select == 7:
        logging.info("Выбран импорт из csv")
        model.import_list_csv()

logging.info('Программа выполнена!')
