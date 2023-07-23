from models.note import Note
from datetime import datetime


# Фабрика для создания экземпляров заметок
class NoteFactory:

    @staticmethod
    def create(id, title, text):
        return Note(id, title, text, datetime.now(), datetime.now())
