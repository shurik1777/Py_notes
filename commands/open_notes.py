import os
import Py_notes.text as tf
from Py_notes.models.notes import Notes


def open_notes():
    """Функция для открытия выбранной базы заметок в формате CSV или JSON"""

    print(tf.file_name)
    file_name = input()  # Читаем ввод пользователя.
    csv_file = f"{file_name}.csv"  # Формируем название CSV файла.
    json_file = f"{file_name}.json"  # Формируем название JSON файла.

    notes = Notes.get_instance()  # Получаем экземпляр класса Notes
    notes_list = []  # Объявляем переменную notes_list здесь

    if os.path.exists(csv_file):
        notes_list = notes.load_from_file(csv_file)  # Сохраняем список загруженных заметок
    elif os.path.exists(json_file):
        notes_list = notes.load_from_file(json_file)  # Сохраняем список загруженных заметок
    else:
        print(tf.file_not_found1, {file_name}, tf.file_not_found2)

    # Добавляем загруженные заметки в список notes
    notes.notes.extend(notes_list)

    # Вместо вызова view_notes(notes), вы можете вывести сообщение об успешном добавлении файла.
    print(tf.file_added_successfully, {file_name})
