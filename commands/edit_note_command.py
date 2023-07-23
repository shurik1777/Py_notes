from abc import ABC, abstractmethod


# Абстрактный класс для команд
class Command(ABC):

    @abstractmethod
    def execute(self):
        pass


# Конкретная команда для редактирования заметки
class EditNoteCommand(Command):

    def __init__(self, notes, id, title=None, text=None):
        self.notes = notes
        self.id = id
        self.title = title
        self.text = text

    def execute(self):
        self.notes.edit(self.id, self.title, self.text)
