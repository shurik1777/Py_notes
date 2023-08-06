from Py_notes.models.note import Note  # импортируем класс Note из другого модуля
from datetime import datetime


# Фабрика для создания экземпляров заметок
class NoteFactory:

    @staticmethod
    def create(id, title, text):
        # Метод статического класса, который создает новый экземпляр класса Note с указанными параметрами.
        # id - id заметки, title - заголовок заметки, text - текст заметки.
        # created и modified будут установлены на текущие дату и время.
        return Note(id, title, text, datetime.now(), datetime.now())
