from datetime import date

def new_note():
    print("Создание новой заметки:")
    new_note = (str(new_date()) + " " + new_heading() + " " + new_text())
    return new_note

def new_heading():
    heading = str(input("Введите заголовок заметки: "))
    return heading

def new_text():
    text = str(input("Введите текст заметки: "))
    return text

def new_date():
    new_date = date.today()
    return new_date