import Py_notes.text as tf


def view_notes(notes):
    all_notes = notes.read()  # Получаем список всех заметок из экземпляра класса Notes.
    if all_notes:
        print(tf.all_list)
        for note in all_notes:
            print(f"ID: {note.id}, Заголовок: {note.title}, Текст: {note.text}")
    else:
        print(tf.empty_list)
