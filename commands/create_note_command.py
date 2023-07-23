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


class CreateNoteCommand(Command):
    """Конкретная команда для создания заметки"""

    def __init__(self, notes, id, title, text):
        """Конструктор класса CreateNoteCommand"""
        self.notes = notes  # Объект класса Notes, с которым команда работает.
        self.id = id  # Идентификатор заметки.
        self.title = title  # Заголовок заметки.
        self.text = text  # Текст заметки.

    def execute(self):
        """Метод выполнения команды"""
        self.notes.create(self.id, self.title, self.text)  # Вызываем метод create объекта класса Notes,
        # передаем ему идентификатор, заголовок и текст заметки для создания.
