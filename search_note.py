import add_note
import note

def search_note():
    search_for_heading()



def search_for_heading():
    search_str = str(input("Введите заголовок заметки, которую вы ищете: "))
    for v in note.dict_note.values():
        v.