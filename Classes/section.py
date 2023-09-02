from .book import Book


class Section:
    def __init__(self, title):
        self.title = title
        self.books = {}

    def getTitle(self):
        return self.title

    def addBook(self, name, author, cost):
        book = Book(name, author, cost)
        self.books[name] = book

    def searchBookByTitle(self, title):
        return self.books.get(title, None)

    def searchBookByAuthor(self, author):
        return [book for book in self.books.values() if book.getAuthor() == author]

    def deleteBook(self, title):
        del self.books[title]

    def showBooks(self):
        print(f"Section: {self.title}")
        for book in self.books.values():
            print(
                f"Title: {book.getTitle()}, Author: {book.getAuthor()}, Cost: {book.getCost()}"
            )
