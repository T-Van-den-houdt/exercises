class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        for b in self.books:
            if b.title == book.title and b.author == book.author:
                self.books.remove(b)

    def search_books(self, search_string):
        search_result = []
        for book in self.books:
            if search_string.lower() in book.author.lower() or search_string.lower() in book.title.lower():
                search_result.append(book)
        return search_result
