import note
import search_note
import add_note

def edit_note():
    edit_str = input("Введите id заметки, которую вы хотите изменить: ")
    note.dict_note[int(edit_str)] = note.new_note()
    add_note.write_to_new_dict(int(edit_str))
    add_note.whrite_to_json_file()
    