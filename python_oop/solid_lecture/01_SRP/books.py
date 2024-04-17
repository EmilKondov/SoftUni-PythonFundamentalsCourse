class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page

class Library:
    def __init__(self, books):
        self.books: List[Book] = books


    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, title: str):
        to_remove = [b for b in self.books if b.title == title]

        if not to_remove:
            raise ValueError("No such book title")



    def find_book_title(self, title):
        book = [b for b in self.books if b.title == title]


