from Book import Book
from Book import availability

class Library:
    def __init__(self, numberBook, BookList):
        self.numberBook = numberBook
        self.BookList = BookList
    
    def borrow(self, bookTitle, studentNumber):
        for book in self.BookList :
            if book.title == bookTitle and book.availability.status == "Available":
                self.book = book
                self.book.availability.status = "Checked Out"
                self.book.availability.studnetnumber = studentNumber
                print(f"{bookTitle} is assigned to studentNumber")
                return
        print(f"{bookTitle} X book is not available")
    
    def returnBook(self, booktitle, studentNumber):
        self.book = book
        self.book.availability.status = "Available"
        self.book.availability.studnetnumber = ""

    def checkAvaibility(self, bookTitle):
        for book in self.BookList:
            if book.title == bookTitle :
                return f"Book name : {book.title} - Book Status : {book.availability.status}"

    def getAllBook(self):
        for book in self.BookList:
            print(f"{book}")

if __name__ == "__main__":
    books = [
        Book("Python Basics", "John Doe", availability("Available", 0)),
        Book("Data Science 101", "Jane Smith", availability("Checked Out", 2)),
        Book("Machine Learning", "Andrew Ng", availability("Available", 3)),
        Book("Deep Learning", "Ian Goodfellow", availability("Checked Out", 4)),
        Book("Fluent Python", "Luciano Ramalho", availability("Available", 5)),
        Book("Effective Java", "Joshua Bloch", availability("Available", 0)),
        Book("Design Patterns", "Erich Gamma", availability("Checked Out", 6)),
        Book("Clean Code", "Robert C. Martin", availability("Available", 0)),
        Book("Artificial Intelligence", "Stuart Russell", availability("Checked Out", 7)),
        Book("Natural Language Processing", "Dan Jurafsky", availability("Available", 0)),
    ]

    my_lib = Library(10, books)

    my_lib.getAllBook()
    print("------------")
    print(my_lib.checkAvaibility("Design Patterns"))
    print("-----------")
    my_lib.borrow("Python Basics", 8)
    my_lib.borrow("Design Patterns", 10)
    print("-----------")
    my_lib.getAllBook()
