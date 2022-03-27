class BookDB:

    books = []
    def __init__(self, book=None):
        self.books.append(book)
    
    def add(self, book):
        self.books.append(book)
    
    def get_books(self):
        return self.books
