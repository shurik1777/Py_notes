import os
import Py_notes.text as tf  # Импортируем модуль text.py и задаем для него псевдоним tf.
from Py_notes.commands.open_notes import open_notes  # Импортируем функцию open_notes из модуля commands.open_files.
from Py_notes.view.view import view_notes
from Py_notes.models.notes import Notes  # Импортируем класс Notes из модуля models.notes.
from commands.create_note_command import \
    CreateNoteCommand  # Импортируем класс CreateNoteCommand из модуля commands.create_note_command.
from commands.edit_note_command import \
    EditNoteCommand  # Импортируем класс EditNoteCommand из модуля commands.edit_note_command.
from commands.delete_note_command import \
    DeleteNoteCommand  # Импортируем класс DeleteNoteCommand из модуля commands.delete_note_command.
from commands.open_list_files import list_files  # Импортируем функцию list_files из модуля commands.open_list_files.


def print_menu():
    # Функция выводит на экран текст меню, используя текст из модуля text.py.
    print(*tf.menu, sep='')


def controller():
    # Функция управления приложением.
    notes = Notes.get_instance()

    while True:
        print_menu()
        choice = input(tf.choice)

        if choice == '1':
            # Пункт меню "Создать заметку".
            print(tf.input_id)
            id = input("> ")
            print(tf.input_title)
            title = input("> ")
            print(tf.input_text)
            text = input("> ")
            c = CreateNoteCommand(notes, id, title, text)  # создаем команду для создания заметки
            c.execute()  # вызываем метод execute для выполнения команды

        elif choice == '2':
            # Пункт меню "Удалить заметку".
            print(tf.input_id)
            id = input("> ")
            d = DeleteNoteCommand(notes, id)  # создаем команду для удаления заметки
            d.execute()  # вызываем метод execute для выполнения команды

        elif choice == '3':
            # Пункт меню "Редактировать заметку".
            print(tf.input_id)
            id = input("> ")
            print(tf.new_values)
            print(tf.input_title)
            title = input("> ")
            print(tf.input_text)
            text = input("> ")
            e = EditNoteCommand(notes, id, title, text)  # создаем команду для редактирования заметки
            e.execute()  # вызываем метод execute для выполнения команды

        elif choice == '4':
            # Пункт меню "Показать все заметки".
            view_notes(notes)

        elif choice == '5':
            # Пункт меню "Сохранить заметки в файл".
            print(tf.saving_to_a_file)
            file_ext = input(tf.file_ext)
            if file_ext not in ('csv', 'json', 'both'):  # если формат файла неверный, цикл начинается заново
                print(tf.unknown_file_format)
                continue
            os.environ['file_ext'] = file_ext  # сохраняем формат файла в переменную окружения
            notes.save_to_file()  # сохраняем заметки в файл
            print(tf.successfully_saved)

        elif choice == '6':
            # Пункт меню "Отобразить список файлов".
            list_files()  # вызываем функцию для вывода списка файлов

        elif choice == '7':
            # Пункт меню "Открыть базу заметок из файла".
            open_notes()  # вызываем функцию для открытия файла с заметками

        elif choice == '0':
            break  # выходим из цикла

        else:
            print(tf.invalid_choice)  # выводим сообщение об ошибке, если выбран неверный пункт меню
