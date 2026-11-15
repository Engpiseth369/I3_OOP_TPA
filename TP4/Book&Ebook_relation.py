class Book:
    def __init__(self, title, author, price):
        self.title = title
        self._price = None
        self.author = author
        self.price = price
        
    def display_info(self):
        print(f"{self.title} by {self.author}: ${self.price:.2f}")
class Ebook(Book):
    def __init__(self, title, author, price, file_size_mb):
        super().__init__(title, author, price)
        self.file_size_mb = file_size_mb
    
    def display_info(self):
        super().display_info()
        print(f"File Size: {self.file_size_mb} MB")

book = Book("Clean Code", "Robert C. Martin", 35.50)
print(book.price)
book.price = 40
print(book.price)

try: 
    book.price = -5
except ValueError as e:
    print("Error:", e)

ebook = Ebook("Python Crash Course", "Eric Matthes", 25.00, 4.2)
ebook.display_info()

        
    
        
        