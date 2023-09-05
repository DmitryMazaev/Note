import note
from datetime import date

heading_list = []
text_list = []
# Функция по поиску заметки по заголовку
def search_for_heading():
    search_str = str(input("Введите заголовок заметки, которую вы ищете: "))
    i = 0
    for key, value in note.dict_note.items():
        if search_str in value.heading:
            print(key, value)
            heading_list.append(key)
            i =+1
    if i == 0:
        print("Искомого заголовка нет")

# Функция по поиску заметки по тексту
def search_for_text():
    search_str = str(input("Введите текст заметки, которую вы ищете: "))
    i = 0
    for key, value in note.dict_note.items():
        if search_str in value.text:
            print(key, value)
            text_list.append(key)
            i =+1
    if i == 0:
        print("Искомого текста нет")
