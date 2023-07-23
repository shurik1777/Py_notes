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


class EditNoteCommand(Command):
    """Конкретная команда для редактирования заметки"""

    def __init__(self, notes, id, title=None, text=None):
        """Конструктор класса EditNoteCommand"""
        self.notes = notes  # Объект класса Notes, с которым команда работает.
        self.id = id  # Идентификатор заметки.
        self.title = title  # Новый заголовок заметки (если передан).
        self.text = text  # Новый текст заметки (если передан).

    def execute(self):
        """Метод выполнения команды"""
        self.notes.edit(self.id, self.title, self.text)  # Вызываем метод edit объекта класса Notes.
        # Передаем ему идентификатор, новый заголовок и текст заметки для редактирования.
