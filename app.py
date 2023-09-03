import note
import add_note
import search_note
import delete_note
import edit_note

def main():
    print("Добро пожаловать в приложение Заметки!")
    while True:
        print("Выберите действие: ")
        command = int(input("1 - создание новой заметки, 2 - поиск заметки, 3 - редактирование заметки, 4 - удаление заметки, 5 - печать заметок, 6 - выход: "))
        if command == 1:
            a = note.new_note()
            add_note.add_note(a)

        if command == 2:
            print("Выберите критерий для поиска: ")
            command_search = int(input("1 - по заголовку, 2 - по тексту: "))

            if command_search == 1:
                search_note.search_for_heading()

            if command_search == 2:
                search_note.search_for_text()

        if command == 3:
            add_note.print_dict()
            edit_note.edit_note()

        if command == 4:
            print("Выберите критерий для удаления: ")
            command_delete = int(input("1 - по заголовку, 2 - по тексту, 3 - по id: "))
            
            if command_delete == 1:
                delete_note.delete_for_heading()

            if command_delete == 2:
                delete_note.delete_for_text()

            if command_delete == 3:
                delete_note.delete_for_id()

        if command == 5:
            add_note.print_dict()
        
        if command == 6:
            break



if __name__ == "__main__":
    main()