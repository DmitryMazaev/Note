from datetime import date
dict_note = {}
class note: 
    def __init__(self, date, heading, text): 
        self.date = date 
        self.heading = heading
        self.text = text
    def __str__(self): 
        return "Заметка: " + self.date + " " + self.heading + " " + self.text

def new_note():
    print("Создание новой заметки:")
    new_note = note(new_date(), new_heading(), new_text())
    return new_note

def new_heading():
    heading = str(input("Введите заголовок заметки: "))
    return str(heading)

def new_text():
    text = str(input("Введите текст заметки: "))
    return str(text)

def new_date():
    new_date = date.today()
    return str(new_date)

