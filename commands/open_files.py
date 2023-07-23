import os
from Py_notes.models.notes import Notes

# Импортируем модуль os для работы с операционной системой
# импортируем класс Notes для работы с заметками

notes = Notes.get_instance()  # Создаем экземпляр класса Notes


def open_notes():
    """Функция для открытия выбранной базы заметок в формате CSV или JSON"""

    print("Введите название файла заметок (без расширения): ")
    # Выводим на экран приглашение ввести имя файла заметок.

    file_name = input()  # Читаем ввод пользователя.
    csv_file = f"{file_name}.csv"  # Формируем название CSV файла.
    json_file = f"{file_name}.json"  # Формируем название JSON файла.

    if os.path.exists(csv_file):  # Проверяем, существует ли CSV файл.
        notes.load_from_file(csv_file)  # Если существует, загружаем заметки из файла.
        print(f"Заметки из файла {csv_file} успешно загружены.")
    elif os.path.exists(json_file):  # Проверяем, существует ли JSON файл.
        notes.load_from_file(json_file)  # Если существует, загружаем заметки из файла.
        print(f"Заметки из файла {json_file} успешно загружены.")
    else:  # Если ни один файл не существует, выводим сообщение об ошибке.
        print(f"Файл {file_name} не найден.")
