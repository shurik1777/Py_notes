import os
import csv
import json
import chardet
import Py_notes.text as tf

from datetime import datetime
from dotenv import load_dotenv

from Py_notes.models.note_factory import NoteFactory
from Py_notes.models.note import Note

load_dotenv()


# JSON-сериализатор для преобразования объекта datetime в строку
class DateTimeJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        return json.JSONEncoder.default(self, obj)


# Класс заметок
class Notes:
    _instance = None

    @staticmethod
    def get_instance():
        if not Notes._instance:
            Notes._instance = Notes()
        return Notes._instance

    def __init__(self):
        if Notes._instance != None:
            raise Exception(tf.exception_in)  # Возбуждает исключение в случае повторного создания экземпляра класса.
        else:
            Notes._instance = self
            self.notes = []  # Список заметок.

    def create(self, id, title, text):
        """
        Метод для создания заметки.

        Parameters:
            id (str): Идентификатор заметки.
            title (str): Заголовок заметки.
            text (str): Текст заметки.
        """
        note = NoteFactory.create(id, title, text)
        self.notes.append(note)
        self.save_to_file()  # Сохраняет списки заметок в файл.
        print(tf.create_note, note)

    def delete(self, id):
        """
        Метод для удаления заметки по идентификатору.

        Parameters:
            id (str): Идентификатор заметки, которую нужно удалить.
        """
        note = self.get_note_by_id(id)
        if note:
            self.notes.remove(note)
            self.save_to_file()  # Сохраняет списки заметок в файл.
            print(tf.delete_note, note)
        else:
            print(tf.note_find, id)

    def edit(self, id, title=None, text=None):
        """
        Метод для редактирования заметки по идентификатору.

        Parameters:
            id (str): Идентификатор заметки, которую нужно отредактировать.
            title (str, optional): Новый заголовок заметки (если передан).
            text (str, optional): Новый текст заметки (если передан).
        """
        note = self.get_note_by_id(id)
        if note:
            if title:
                note.title = title
            if text:
                note.text = text
            note.modified = datetime.now()
            self.save_to_file()  # Сохраняет списки заметок в файл.
            print(tf.edited_note, note)
        else:
            print(tf.note_find, id)

    def read(self, filter_date=None):
        """
        Метод для чтения заметок.

        Parameters:
            filter_date (datetime, optional): Дата для фильтрации заметок по дате создания или изменения.

        Returns:
            list: Список заметок.
        """
        if not self.notes:
            return []  # Возвращаем пустой список, если заметок нет.
        if filter_date:
            # Фильтрация списка заметок по дате создания или изменения.
            filtered_notes = [note for note in self.notes if
                              note.created.date() == filter_date.date() or note.modified.date() == filter_date.date()]
            if filtered_notes:
                return filtered_notes
            else:
                return []
        return self.notes

    def get_note_by_id(self, id):
        """
        Метод для получения заметки по идентификатору.

        Parameters:
            id (str): Идентификатор заметки.

        Returns:
            Note or None: Возвращает объект заметки, если найдена, иначе возвращает None.
        """
        for note in self.notes:
            if note.id == id:
                return note
        return None

    def save_to_file(self):
        """
        Метод для сохранения заметок в файл.
        """
        notes = [note.to_dict() for note in self.notes]
        unique_ids = set()  # Множество для хранения уникальных идентификаторов заметок
        unique_notes = []  # Список для хранения заметок с уникальными идентификаторами

        for note in notes:
            if note['id'] not in unique_ids:
                unique_ids.add(note['id'])
                unique_notes.append(note)

        file_ext = os.getenv('file_ext', 'json')
        # Сохранение заметок в файлы формата JSON, CSV, или и обоих форматов.
        if file_ext == 'json':
            with open('notesJ.json', 'w') as f:
                json.dump(unique_notes, f, cls=DateTimeJSONEncoder)
        elif file_ext == 'csv':
            with open('notesC.csv', 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f, delimiter=';')
                writer.writerow(['id', 'title', 'text', 'created', 'modified'])
                for note in unique_notes:
                    writer.writerow([note['id'], note['title'], note['text'], note['created'], note['modified']])
        elif file_ext == 'both':
            with open('notesJ.json', 'w') as f_json:
                json.dump(unique_notes, f_json, cls=DateTimeJSONEncoder)
            with open('notesC.csv', 'w', newline='', encoding='utf-8') as f_csv:
                writer = csv.writer(f_csv, delimiter=';')
                writer.writerow(['id', 'title', 'text', 'created', 'modified'])
                for note in unique_notes:
                    writer.writerow([note['id'], note['title'], note['text'], note['created'], note['modified']])
        else:
            raise ValueError(f"Неподдерживаемый формат файла: {file_ext}")

    def load_from_file(self, file_name):
        """
        Метод для загрузки заметок из файла.

        Parameters:
            file_name (str): Имя файла, из которого нужно загрузить заметки.

        Returns:
            list: Список загруженных заметок.
        """
        notes = []
        file_ext = os.path.splitext(file_name)[1]
        if file_ext == ".csv":
            with open(file_name, 'rb') as f:
                result = chardet.detect(f.read())
                file_encoding = result['encoding']
            with open(file_name, newline='', encoding=file_encoding) as f:
                reader = csv.reader(f, delimiter=";")
                next(reader)  # пропускаем первую строку заголовка
                for row in reader:
                    created_date = datetime.strptime(row[3], "%Y-%m-%d %H:%M:%S")
                    updated_date = datetime.strptime(row[4], "%Y-%m-%d %H:%M:%S")
                    # Создание экземпляров заметок и добавление их в список.
                    notes.append(
                        Note(id=row[0], title=row[1], text=row[2], created=created_date, modified=updated_date))
        elif file_ext == ".json":
            with open(file_name, 'rb') as f:
                result = chardet.detect(f.read())
                file_encoding = result['encoding']
            with open(file_name, encoding=file_encoding) as f:
                data_json = json.load(f)
                for note in data_json:
                    created_date = datetime.strptime(note['created'], "%Y-%m-%d %H:%M:%S")
                    updated_date = datetime.strptime(note['modified'], "%Y-%m-%d %H:%M:%S")
                    # Создание экземпляров заметок и добавление их в список.
                    notes.append(Note.from_dict(note))
        else:
            raise ValueError(f"Неподдерживаемый формат файла: {file_ext}")

        return notes  # Возвращаем список загруженных заметок
