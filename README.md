## Данный код - это программа заметок, разбитая на модули:
1. В модуле controller определены функции print_menu и controller, которые выводят на экран меню и управляют основной логикой программы, соответственно.
2. В модуле notes определяется класс заметок, реализующий logics приложения.Copy
3. В модуле command определяются команды приложения, используемые для изменения состояния объектов класса Notes.
4. В модуле open_files и list_files определены функции, которые реализуют работу с файлами.

### Вся программа построена на принципе модель-представление-контроллер (MVC).

#### Примененные solid-принципы:
1. Single responsibility principle (принцип единой ответственности) - каждый класс отвечает за одну конкретную задачу, и вся логика приложения находится в классе Notes.
2. Open/closed principle (принцип открытости/закрытости) - класс Notes открыт для расширения (для добавления новых команд) и закрыт для изменения (изменение состояния заметок только через команды).
3. Liskov substitution principle (принцип подстановки Барбары Лисков) - все команды приложения (CreateNoteCommand, DeleteNoteCommand, EditNoteCommand, ReadNotesCommand) удовлетворяют интерфейсу абстрактного класса Command.
4. Dependency inversion principle (принцип инверсии зависимостей) - на верхних уровнях программы объекты класса Notes и команд создаются через методы класса их производителей, что позволяет легко изменять поведение всей программы заменой только одной фабрики (или команды, или класса работы с БД, или драйвера файловой системы и т.д.)
5. Interface segregation principle (принцип разделения интерфейса) - классы команд реализуют только один метод execute.

#### Применены следующие паттерны:

1. Команда - все действия, связанные с изменением состояния объектов Notes, инкапсулированы в командах. Команды реализуют общий интерфейс Command с методом execute.
2. Фабрика - для создания объектов класса заметок применяется фабрика NoteFactory.
3. Синглтон - для класса Notes использован паттерн Singleton, что позволяет существовать только одному экземпляру класса в рамках всей программы.
4. Шаблонный метод - в классе Notes выделены шаблонные методы для работы с заметками create, delete, edit, read., которые используются классами команд.
