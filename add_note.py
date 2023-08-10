import note

#dict_note = {}

def add_note(new_note):
    new_id()
    note.dict_note[new_id()] = new_note

def new_id():
    id = len(note.dict_note)
    return id

def print_dict():
    for v in note.dict_note.values():
        print(v)

