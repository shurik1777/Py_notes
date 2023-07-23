from abc import ABC, abstractmethod


# Импортируем абстрактный базовый класс ABC и декоратор abstractmethod
# ABC - базовый класс для определения абстрактных классов, abstractmethod - декоратор для обозначения абстрактных методов.

class Command(ABC):
    """Абстрактный базовый класс для команд приложения."""

    # Создаем класс-команду для определения базового функционала всех команд

    @abstractmethod
    def execute(self):
        """Метод-команда, будет реализован в конкретных командах"""
        pass


class ReadNotesCommand(Command):
    """Команда для чтения заметок"""

    # Создаем класс-команду для чтения заметок

    def __init__(self, notes, filter_date=None):
        """Метод-конструктор для инициализации объекта"""
        self.notes = notes
        self.filter_date = filter_date

    def execute(self):
        """Метод-команда для чтения заметок. Вызывает метод read объекта notes"""
        return self.notes.read(self.filter_date)
