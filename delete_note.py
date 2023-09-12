import note
import search_note
import add_note

# Функция удаления заметки на основании поиска по заголовку
def delete_for_heading():
    while True:
        try:
            search_note.search_for_heading()
            delete_str = int(input("Введите id заметки, которую вы хотите удалить: "))
            if delete_str in search_note.heading_list:
                note.dict_note.pop(int(delete_str))
                add_note.new_dict.pop(int(delete_str))
                add_note.whrite_to_json_file()
                search_note.heading_list.clear()
                print("Заметка удалена!")
                break
            else:
                print("Введенный id отсутствует в выведенном перечне")
                
        except ValueError:
            print('Ошибка. Введенный id отсутствует в выведенном перечне')
        

# Функция удаления заметки на основании поиска по тексту
def delete_for_text():
    while True:
        try:
            search_note.search_for_text()
            delete_str = int(input("Введите id заметки, которую вы хотите удалить: "))
            if delete_str in search_note.text_list:
                note.dict_note.pop(int(delete_str))
                add_note.new_dict.pop(int(delete_str))
                add_note.whrite_to_json_file()
                search_note.text_list.clear()
                print("Заметка удалена!")
                break
            else:
                print("Введенный id отсутствует в выведенном перечне")
        except ValueError:
            print('Ошибка. Введенный id отсутствует в выведенном перечне')

# Функция удаления заметки на основании id
def delete_for_id():
    add_note.print_dict()
    while True:
        try:
            delete_str = int(input("Введите id заметки, которую вы хотите удалить: "))
            if delete_str in note.dict_note.keys():
                note.dict_note.pop(int(delete_str))
                add_note.new_dict.pop(int(delete_str))
                add_note.whrite_to_json_file()
                print("Заметка удалена!")
                break
            else:
                print("Введенный id отсутствует в выведенном перечне")
        except ValueError:
            print('Ошибка. Введенный id отсутствует в выведенном перечне')