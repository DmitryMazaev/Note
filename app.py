import note
import add_note
import search_note

def main():
    
    print("Добро пожаловать в приложение Заметки!")
    while True:
        print("Выберите действие: ")
        command = int(input("1 - создание новой заметки, 2 - поиск заметки "))
        if command == 1:
            a = note.new_note()
            add_note.add_note(a)
            add_note.print_dict()
            #print (a.heading)
        if command == 2:
            search_note.search_note()




if __name__ == "__main__":
    main()