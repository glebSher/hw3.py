from os.path import exists
from csv_creator import creating
from file_writing import writing_csv
from file_writing import writing_txt

path = 'Phonebook.csv'
valid = exists(path)
if not valid:
    creating()

writing_csv()
writing_txt()
