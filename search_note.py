import note
from datetime import date

# Функция по поиску заметки по заголовку
def search_for_heading():
    search_str = str(input("Введите заголовок заметки, которую вы ищете: "))
    for key, value in note.dict_note.items():
        if search_str in value.heading:
            print(key, value)

# Функция по поиску заметки по тексту
def search_for_text():
    search_str = str(input("Введите текст заметки, которую вы ищете: "))
    for key, value in note.dict_note.items():
        if search_str in value.text:
            print(key, value)
