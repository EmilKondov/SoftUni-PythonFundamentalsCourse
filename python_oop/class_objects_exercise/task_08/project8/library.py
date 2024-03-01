from typing import List
from project8.user import User
class Library:
    def __init__(self):
        self.user_records: List = []
        self.books_available = {}
        self.rented_books = {{}}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        pass

    def return_book(self, author:str, book_name:str, user: User):
        pass

