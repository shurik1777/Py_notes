import os

# Импортируем модуль os для работы с операционной системой

# Функция для отображения списка файлов в текущей директории
def list_files():
    """Функция для отображения списка файлов в текущей директории"""
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    # Создаем список файлов из текущей директории, используя метод listdir модуля os.
    # isfile - метод модуля os, который проверяет, является ли объект файлом.
    # '.' - переданный аргумент, означает текущую директорию.

    print("Список файлов:") # Выводим на экран заголовок.
    for f in files:
        print("|--", f) # Выводим на экран имя файла (в виде дерева).
