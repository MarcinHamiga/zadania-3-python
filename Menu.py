from Note import *

class Menu:

    def __init__(self):
        self.notebook = Notebook()
        self.options = {
            "1":self.show_notes,
            "2":self.search_notes,
            "3":self.add_note,
            "4":self.modify_note,
            "5":self.quit
        }

    def show_menu(self):
        while True:
            self.run()

    def run(self):
        cmd = input("1. Show notes\n2. Search notes\n3. Add a note\n4. Modify a note\n5. Exit\n> ")
        match cmd:
                case "1":
                    self.options[cmd](self.notebook.notes)
                case "2":
                    self.options[cmd]()
                case "3":
                    self.options[cmd]()
                case "4":
                    while True:
                        try:
                            id_ = int(input("Which note do you want to modify? (id)\n> "))
                            break
                        except ValueError:
                            print("Please, enter an integer!")
                    self.options[cmd](id_)
                case "5":
                    self.options[cmd]()
                case _:
                    print("Unknown command")

    def show_notes(self, notes: list):
        for note in notes:
            print(f"id#{note.id} {note.date} [{note.tag}] {note.text}")

    def search_notes(self):
        phrase = input("Enter a phrase you want to search for\n> ")
        if phrase is None or phrase == "":
            self.show_notes(self.notebook)
        else:
            output_notes = self.notebook.search(phrase)
            match len(output_notes):
                case 0:
                    print("No notes including the searched phrase")
                case _:
                    self.show_notes(output_notes)
    
    def add_note(self):
        text = input("Enter the text of the note\n> ")
        tag = input("Enter a tag/tags\n> ")
        self.notebook.new_note(text=text, tag=tag)

    def modify_note(self, id_):
        cmd = input("Do you want to modify the tag(t) or the content?(c) (t/c)\n> ")
        match cmd:
            case "c":
                content = input("Enter the new content of the note\n> ")
                self.notebook.modify_text(id_, content)
            case "t":
                tag = input("Enter the new tag/tags of the note\n> ")
                self.notebook.modify_tag(id_, tag)

    def quit(self):
        exit()

if __name__ == "__main__":
    menu = Menu()
    menu.show_menu()