import note
import json

# Словарь для записи в .json-файл. 
new_dict = {}

# Функция, добавляющая новую заметку в словарь
def add_note(new_note):
    new_id()
    note.dict_note[new_id()] = new_note
    write_to_new_dict()
    whrite_to_json_file()

# Функция, присваивающая уникальный id новой заметке
def new_id():
    id = len(note.dict_note) + 1
    while (note.dict_note.get(id) != None):
        id += 1
    return int(id)

# Функция, выводящая полный перечень заметок    
def print_dict():
    for key, value in note.dict_note.items():
        print(key, value)

# Функция, записывающая заметки в словарь для записи в .json-файл. 
def write_to_new_dict():
    for id, values in note.dict_note.items():
        str_head = values.heading
        str_text = values.text
        str_date = str(values.new_date)
 
        data = {"Heading": str_head, "Text": str_text, "Date": str_date}

        new_dict[int(id)] = data

# Функция, осуществляющая запись в .json-файл
def whrite_to_json_file():
    # Преобразование словаря в JSON-строку
    json_string = json.dumps(new_dict)
    
    # Запись JSON-строки в .json-файл
    with open("data.json", "w", encoding = 'utf-8') as json_file:
        json_file.write(json_string)