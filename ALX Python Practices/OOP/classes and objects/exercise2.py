"""
Create a Book class with attributes like title, author, and pages.
Implement both __str__ and __repr__ magic methods to provide 
different string representations of the book object.
"""
class Book: 
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} was written by {self.author} and it has {self.pages} pages"
    
    def __repr__(self):
        return f"{self.title} was written by {self.author} and it has {self.pages} pages"
    
    
book1 = Book("Fun in working together", "Ruth Nagbe", 30)
print(book1)
print(repr(book1))