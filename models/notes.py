from datetime import datetime
import json
import csv
from models.note_factory import NoteFactory
from dotenv import load_dotenv
import os
import chardet

from notes_app.models.note import Note

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
    def getInstance():
        if not Notes._instance:
            Notes()
        return Notes._instance

    def __init__(self):
        if Notes._instance != None:
            raise Exception("Ошибка создания экземпляра класса Notes!")
        else:
            Notes._instance = self
            self.notes = []

    # Метод для создания заметок
    def create(self, id, title, text):
        note = NoteFactory.create(id, title, text)
        self.notes.append(note)
        self.saveToFile()
        print("Заметка создана:", note)

    # Метод для удаления заметок
    def delete(self, id):
        note = self.getNoteById(id)
        if note:
            self.notes.remove(note)
            self.saveToFile()
            print("Заметка удалена:", note)
        else:
            print("Не найдено заметки с id:", id)

    # Метод для редактирования заметок
    def edit(self, id, title=None, text=None):
        note = self.getNoteById(id)
        if note:
            if title:
                note.title = title
            if text:
                note.text = text
            note.modified = datetime.now()
            self.saveToFile()
            print("Заметка отредактирована:", note)
        else:
            print("Не найдено заметки с id:", id)

    # Метод для чтения заметок
    def read(self, filter_date=None):
        if not self.notes:
            print("Список заметок пуст!")
            return []
        if filter_date:
            filtered_notes = [note for note in self.notes if
                              note.created.date() == filter_date.date() or note.modified.date() == filter_date.date()]
            if filtered_notes:
                return filtered_notes
            else:
                return []
        return self.notes

    def getNoteById(self, id):
        for note in self.notes:
            if note.id == id:
                return note
        return None

    # Метод для сохранения заметок в файл
    def saveToFile(self):
        notes = [note.toDict() for note in self.notes]
        file_ext = os.getenv('file_ext', 'json')
        if file_ext == 'json':
            with open('notesJ.json', 'w') as f:
                json.dump(notes, f, cls=DateTimeJSONEncoder)
        elif file_ext == 'csv':
            with open('notesC.csv', 'w', newline='') as f:
                writer = csv.writer(f, delimiter=';')
                writer.writerow(['id', 'title', 'text', 'created', 'modified'])
                for note in notes:
                    writer.writerow(
                        [note['id'], note['title'], note['text'], note['created'], note['modified']])
        elif file_ext == 'both':
            with open('notesJ.json', 'w') as f_json:
                json.dump(notes, f_json, cls=DateTimeJSONEncoder)
            with open('notesC.csv', 'w', newline='') as f_csv:
                writer = csv.writer(f_csv, delimiter=';')
                writer.writerow(['id', 'title', 'text', 'created', 'modified'])
                for note in notes:
                    writer.writerow(
                        [note['id'], note['title'], note['text'], note['created'], note['modified']])
        else:
            raise ValueError(f"Неподдерживаемый формат файла: {file_ext}")

    # Метод для загрузки заметок из файла
    def loadFromFile(self, file_name):
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
                    notes.append(Note(id=row[0], title=row[1], text=row[2], created=created_date, modified=updated_date))
        elif file_ext == ".json":
            with open(file_name, 'rb') as f:
                result = chardet.detect(f.read())
                file_encoding = result['encoding']
            with open(file_name, encoding=file_encoding) as f:
                data_json = json.load(f)
                for note in data_json:
                    created_date = datetime.strptime(note['created'], "%Y-%m-%d %H:%M:%S")
                    updated_date = datetime.strptime(note['modified'], "%Y-%m-%d %H:%M:%S")
                    notes.append(Note.fromDict(note))
        else:
            raise ValueError(f"Неподдерживаемый формат файла: {file_ext}")

        self.notes = notes
