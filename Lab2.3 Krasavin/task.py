class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str): # описываем конструктор базового класса и его атрибуты
        self._name = name
        self._author = author

    @property
    def name(self) -> str: #атрибут name и author делаем свойствами, причем только с геттерами, так как впоследствии они меняться не могут
        return self._name

    @property
    def author(self) -> str:
        return self._author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book): # инициализируем подкласс PaperBook, унаследовав от Book
    """ Дочерний класс бумажной книги. Наследуется от базового класса книги. """
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author) # используем конструктор базового класса и добавляем "местный" конструктор с атрибутом pages
        self.pages = pages

    @property # делаем pages свойством; геттер:
    def pages(self) -> int:
        return self.pages

    @pages.setter #сеттер + проверки на тип и положительность страниц с выдачей соответствующих ошибок
    def pages(self, pages: int) -> None:
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно иметь значение 'int' ")
        if pages <= 0:
            raise ValueError("Количество страниц не может быть меньше или равным нулю")
        self._pages = pages # защищенному атрибуту _pages присваиваем значение pages

    # магический метод __str__ унаследуем от базового класса, так как нет изменений

    def __repr__(self): # переопределяем магический метод __repr__, потому что появился атрибут pages
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages = {self.pages!r} )"



class AudioBook(Book): # инициализируем подкласс AudioBook, унаследовав от Book
    """ Дочерний класс аудиокниги. Наследуется от базового класса книги."""
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author) # используем конструктор базового класса и добавляем "местный" конструктор с атрибутом duration
        self.duration = duration

    @property # делаем duration свойством; геттер:
    def duration(self) -> int:
        return self.duration

    @duration.setter #сеттер + проверки на тип (в данном случае float) и положительность длины записи с выдачей соответствующих ошибок
    def duration(self, duration: float) -> None:
        if not isinstance(duration, float):
            raise TypeError("Продолжительность записи должна иметь тип 'float' ")
        if duration <= 0:
            raise ValueError("Длина записи не может быть меньше или равной нулю")
        self._duration = duration # защищенному атрибуту _duration присваиваем значение duration
    def __str__(self): # переопределяем магический метод __str__, так как речь идет уже об аудиокниге
        return f"Аудиокнига {self.name}. Автор {self.author}"

    def __repr__(self): # переопределяем магический метод __repr__, потому что появился атрибут duration
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration = {self.duration!r} )"
