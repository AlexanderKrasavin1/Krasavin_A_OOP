
from task_1 import Book # импортируем класс из первого задания для использования в этом блоке программы

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



class Library:
    def __init__(self, books=None): # конструктор, принимает аргумент "книги" по умолчанию ноль
            if books is None:
                books = []
            self.books = books

    def get_next_book_id(self):
            if not self.books:
                return 1 # если в списке не было книг, то следующий ID будет 1
            else:
                return self.books[-1].id_ + 1 # берем ID у последнего элемента из списка книг и возвращаем значение на единицу больше

    def get_index_by_book_id(self, book_id_):
            for i, book in enumerate(self.books): # список книг автоматически нумеруется от нуля
                if book.id_ == book_id_: # пробегаем циклом по пронумерованному списку и сравниваем каждую книгу с искомой по ID
                    return i # возвращаем индекс из пронумерованного списка по запрашиваемому ID книги
            raise ValueError("Книги с запрашиваемым id не существует") # если книги не нашлось, выдаём ошибку значения

if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(2))  # проверяем индекс книги с id = 1

