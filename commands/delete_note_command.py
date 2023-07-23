from abc import ABC, abstractmethod
# from models.notes import Notes


# Абстрактный класс для команд
class Command(ABC):

    @abstractmethod
    def execute(self):
        pass


# Конкретная команда для удаления заметки
class DeleteNoteCommand(Command):

    def __init__(self, notes, id):
        self.notes = notes
        self.id = id

    def execute(self):
        self.notes.delete(self.id)
