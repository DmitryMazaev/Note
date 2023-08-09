import note

dict_note = {}

def add_note(new_note):
    new_id()
    dict_note[new_id()] = new_note

def new_id():
    id = len(dict_note)
    return id

def print_dict():
    for v in dict_note.values():
        print(v)