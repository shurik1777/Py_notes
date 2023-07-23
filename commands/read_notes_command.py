from abc import ABC, abstractmethod


# Абстрактный класс для команд
class Command(ABC):

    @abstractmethod
    def execute(self):
        pass


# Конкретная команда для чтения заметок
class ReadNotesCommand(Command):

    def __init__(self, notes, filter_date=None):
        self.notes = notes
        self.filter_date = filter_date

    def execute(self):
        return self.notes.read(self.filter_date)
