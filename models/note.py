from datetime import datetime


class Note:
    def __init__(self, id=None, title=None, text=None, created=None, modified=None):
        self.id = id
        self.title = title
        self.text = text
        self.created = created or datetime.now()
        self.modified = modified or datetime.now()

    def toDict(self):
        return {
            'id': self.id,
            'title': self.title,
            'text': self.text,
            'created': self.created.strftime('%Y-%m-%d %H:%M:%S'),
            'modified': self.modified.strftime('%Y-%m-%d %H:%M:%S')
        }

    @classmethod
    def fromDict(cls, note_dict):
        created = datetime.strptime(note_dict['created'], '%Y-%m-%d %H:%M:%S')
        modified = datetime.strptime(note_dict['modified'], '%Y-%m-%d %H:%M:%S')
        return cls(note_dict['id'], note_dict['title'], note_dict['text'], created, modified)

    def __str__(self):
        return 'id: {}, title: {}, text: {}, created: {}, modified: {}'.format(self.id, self.title, self.text,
                                                                               self.created.strftime(
                                                                                   '%Y-%m-%d %H:%M:%S'),
                                                                               self.modified.strftime(
                                                                                   '%Y-%m-%d %H:%M:%S'))
# # Класс заметки
# class Note:
#     def __init__(self, id, title, text, created, modified):
#         self.id = id
#         self.title = title
#         self.text = text
#         self.created = created
#         self.modified = modified
#
#     # Метод для преобразования заметки в словарь
#     def toDict(self):
#         return {
#             'id': self.id,
#             'title': self.title,
#             'text': self.text,
#             'created': self.created,
#             'modified': self.modified
#         }
#
#     def __str__(self):
#         return 'id: {}, title: {}, text: {}, created: {}, modified: {}'.format(self.id, self.title, self.text,
#                                                                                self.created.strftime(
#                                                                                    '%Y-%m-%d %H:%M:%S'),
#                                                                                self.modified.strftime(
#                                                                                    '%Y-%m-%d %H:%M:%S'))
