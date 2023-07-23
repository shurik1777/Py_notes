import os
from datetime import datetime

from models.notes import Notes
from commands.create_note_command import CreateNoteCommand
from commands.read_notes_command import ReadNotesCommand
from commands.edit_note_command import EditNoteCommand
from commands.delete_note_command import DeleteNoteCommand
from notes_app.commands.open_files import open_notes
from notes_app.commands.open_list_files import list_files


def print_menu():
    print("\nВыберите действие:")
    print("1 - добавить заметку")
    print("2 - удалить заметку")
    print("3 - редактировать заметку")
    print("4 - просмотреть заметки")
    print("5 - сохранить заметки в файл")
    print("6 - отобразить список файлов")
    print("7 - открыть базу заметок из файла")
    print("0 - выход")


def controller():
    notes = Notes.getInstance()

    while True:
        print_menu()
        choice = input("Выбор: ")

        if choice == '1':
            print('\nСоздание заметки:')
            id = input("id: ")
            title = input("Заголовок: ")
            text = input("Текст: ")
            c = CreateNoteCommand(notes, id, title, text)
            c.execute()

        elif choice == '2':
            print('\nУдаление заметки:')
            id = input("id: ")
            d = DeleteNoteCommand(notes, id)
            d.execute()

        elif choice == '3':
            print('\nРедактирование заметки:')
            id = input("id: ")
            title = input("Новый заголовок (Enter, чтобы оставить прежний): ")
            text = input("Новый текст (Enter, чтобы оставить прежний): ")
            e = EditNoteCommand(notes, id, title, text)
            e.execute()

        elif choice == '4':
            print('\nПросмотр заметок:')
            filter_date = input("Дата в формате (ГГГГ-ММ-ДД) (Enter, чтобы просмотреть все заметки): ")
            try:
                if filter_date:
                    filter_date = datetime.strptime(filter_date, '%Y-%m-%d').date()
                else:
                    filter_date = None
            except ValueError:
                print("Неверный формат даты!")
                continue
            r = ReadNotesCommand(notes, filter_date)
            notes_list = r.execute()
            if not notes_list:
                print("Нет заметок для показа.")
            for note in notes_list:
                print(note)
        elif choice == '5':
            print('\nСохранение заметок в файл:')
            file_ext = input("Формат файла (csv, json, both): ")
            if file_ext not in ('csv', 'json', 'both'):
                print(f"Неизвестный формат файла: {file_ext}")
                continue
            os.environ['file_ext'] = file_ext
            notes.saveToFile()
            print("Заметки успешно сохранены в файл.")
        elif choice == '6':  # Добавлен пункт "Отобразить список файлов"
            list_files()
        elif choice == '7':  # Добавлен пункт "Открыть базу заметок из файла"
            open_notes()

        elif choice == '0':
            break

        else:
            print('Некорректный выбор. Попробуйте еще раз.')
