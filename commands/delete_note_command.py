from abc import ABC, abstractmethod


# Специальный модуль для поддержки Абстрактных базовых классов
# ABC - Абстрактный базовый класс - используется для определения интерфейса,
# необходимого для реализации классам-потомкам.

class Command(ABC):
    """Абстрактный класс для команд"""

    @abstractmethod
    def execute(self):
        """Абстрактный метод для выполнения команды"""
        pass


class DeleteNoteCommand(Command):
    """Конкретная команда для удаления заметки"""

    def __init__(self, notes, id):
        """Конструктор класса DeleteNoteCommand"""
        self.notes = notes  # Объект класса Notes, с которым команда работает.
        self.id = id  # Идентификатор заметки.

    def execute(self):
        """Метод выполнения команды"""
        self.notes.delete(self.id)  # Вызываем метод delete объекта класса Notes,
        # передаем ему идентификатор заметки для удаления.
