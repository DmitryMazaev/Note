import note
import add_note

def main():
    while True:
        #note.new_note()
        add_note.add_note(note.new_note())
        add_note.print_dict()

if __name__ == "__main__":
    main()