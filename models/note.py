from datetime import datetime


class Note:
    def __init__(self, id=None, title=None, text=None, created=None, modified=None):
        # Конструктор класса, который принимает параметры и инициализирует их экземпляром класса. id - id заметки,
        # title - заголовок заметки, text - текст заметки, created - дата и время создания заметки, modified - дата и
        # время последнего изменения заметки.
        self.id = id
        self.title = title
        self.text = text
        self.created = created or datetime.now()
        self.modified = modified or datetime.now()

    def to_dict(self):
        # Метод, который преобразует заметку в словарь.
        return {
            'id': self.id,
            'title': self.title,
            'text': self.text,
            'created': self.created.strftime('%Y-%m-%d %H:%M:%S'),
            'modified': self.modified.strftime('%Y-%m-%d %H:%M:%S')
        }

    @classmethod
    def from_dict(cls, note_dict):
        # Метод, который создает экземпляр класса из словаря.
        created = datetime.strptime(note_dict['created'], '%Y-%m-%d %H:%M:%S')
        modified = datetime.strptime(note_dict['modified'], '%Y-%m-%d %H:%M:%S')
        return cls(note_dict['id'], note_dict['title'], note_dict['text'], created, modified)

    def __str__(self):
        # Метод, который возвращает строковое представление заметки.
        return 'id: {}, title: {}, text: {}, created: {}, modified: {}'.format(self.id, self.title, self.text,
                                                                               self.created.strftime(
                                                                                   '%Y-%m-%d %H:%M:%S'),
                                                                               self.modified.strftime(
                                                                                   '%Y-%m-%d %H:%M:%S'))

