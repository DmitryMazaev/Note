from datetime import date

# Словарь, в котором ключом является уникальный id, значением - список, состоящий из даты, заголовка и текста заметки
dict_note = {}

class note: 
    def __init__(self, new_date, heading, text): 
        self.new_date = new_date 
        self.heading = heading
        self.text = text
    def __str__(self): 
        return "Заметка: " + str(self.new_date) + " " + self.heading + " " + self.text
    
# Функция по созданию экземпляра класса note
def new_note():
    print("Создание новой заметки:")
    new_note = note(new_date(), new_heading(), new_text())
    return new_note

# Функция по созданию заголовка заметки
def new_heading():
    heading = str(input("Введите заголовок заметки: "))
    return str(heading)

# Функция по созданию текста заметки
def new_text():
    text = str(input("Введите текст заметки: "))
    return str(text)

# Функция по определению даты создания заметки
def new_date():
    new_date = date.today()
    return new_date