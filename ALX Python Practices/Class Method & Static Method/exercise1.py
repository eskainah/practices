"""
Create a class Book with a class variable total_books to count the number of book instances created.
Implement a class method display_total_books() to display the total number of books created.
"""
class Book:
    total_books = 0

    def __init__(self, book_title):
        self.book_title = book_title
        Book.total_books += 1

    @classmethod 
    def display_total_books(cls):
        print(f"Total books created is: ", cls.total_books)

book1 = Book("Looking up and afar")

Book.display_total_books()