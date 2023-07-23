import os
from models.notes import Notes

notes = Notes.getInstance()


# Функция для открытия выбранной базы заметок в формате CSV или JSON
def open_notes():
    print("Введите название файла заметок (без расширения): ")
    file_name = input()
    csv_file = f"{file_name}.csv"
    json_file = f"{file_name}.json"
    if os.path.exists(csv_file):
        notes.loadFromFile(csv_file)
        print(f"Заметки из файла {csv_file} успешно загружены.")
    elif os.path.exists(json_file):
        notes.loadFromFile(json_file)
        print(f"Заметки из файла {json_file} успешно загружены.")
    else:
        print(f"Файл {file_name} не найден.")