BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]



class Book:
        def __init__(self, id_: int, name: str, pages: int):
            self.name = None
            self.id_ = None
            self.pages = None
            self.set_id(id_)
            self.set_name(name)
            self.set_pages(pages)

        def set_id(self, id_):
            if id_ is not str:
                TypeError("Id - челое число")
            if id_ >= 0:
                self.id = id_
            else:
                TypeError("Id не может быть меньше нуля")

        def set_pages(self, pages):
            if pages is not int:
                TypeError("Количество страниц - целое число")
            if pages > 0:
                self.pages = pages
            else:
                ValueError("Количество страниц должно быть положительным числом")

        def set_name(self, name):
            if name is not str:
                TypeError("Имя должно быть строкой")
            self.name = name

        def __str__(self) -> str:
            return f'Книга "{self.name}"'

        def __repr__(self) -> str:
            return f'Book(id_={self.id}, name=\'{self.name}\', pages={self.pages})'



if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
