import datetime as dt
from itertools import count


class Note:
    _ids = count(0)
    def __init__(self, text, tag):
        self.text = text
        self.tag = tag
        self.date = dt.datetime.now()
        self.id = next(self._ids)


    def match(self, cmp):
        if cmp in self.text or cmp in self.tag:
            return True
        else:
            return False
class Notebook:
    
    def __init__(self):
        self.notes = []

    def new_note(self, text, tag):
        self.notes.append(Note(text, tag))

    def modify_text(self, id_, text):
        for note in self.notes:
            if note.id == id_:
                note.text = text
                break
        print("No note with the given ID")

    def modify_tag(self, id_, tag):
        for note in self.notes:
            if note.id == id_:
                note.tag = tag

    def search(self, text):
        output = []
        for note in self.notes:
            if note.match(text):
                output.append(note)
        return output