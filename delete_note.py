import note
import search_note
import add_note

# Функция удаления заметки на основании поиска по заголовку
def delete_for_heading():
    search_note.search_for_heading()
    delete_str = input("Введите id заметки, которую вы хотите удалить: ")
    note.dict_note.pop(int(delete_str))
    add_note.new_dict.pop(int(delete_str))
    add_note.whrite_to_json_file()

# Функция удаления заметки на основании поиска по тексту
def delete_for_text():
    search_note.search_for_text()
    delete_str = input("Введите id заметки, которую вы хотите удалить: ")
    note.dict_note.pop(int(delete_str))
    add_note.new_dict.pop(int(delete_str))
    add_note.whrite_to_json_file()

# Функция удаления заметки на основании id
def delete_for_id():
    add_note.print_dict()
    delete_str = input("Введите id заметки, которую вы хотите удалить: ")
    note.dict_note.pop(int(delete_str))
    add_note.new_dict.pop(int(delete_str))
    add_note.whrite_to_json_file()