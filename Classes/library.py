from .section import Section


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Library(metaclass=SingletonMeta):
    def __init__(self, title):
        self.title = title
        self.sections = {}
        self.profit = 0

    def addSection(self, section):
        if section not in self.sections:
            self.sections[section] = Section(section)
        return self.sections[section]

    def searchBookByTitle(self, title):
        for section in self.sections.values():
            book = section.searchBookByTitle(title)
            if book:
                return book
        print("Book not found")
        return None

    def searchBookByAuthor(self, author):
        result = []
        for section in self.sections:
            result.extend(section.searchBookByAuthor(author))
        return result

    def sell_a_book(self, title):
        for section in self.sections.values():
            book = section.searchBookByTitle(title)
            if book:
                self.profit += book.getCost()
                section.deleteBook(title)
                print("Book sold")
                return book
        print("Book not found")
        return None

    def getTotalProfit(self):
        return self.profit

    def showSections(self):
        for section in self.sections.values():
            section.showBooks()

    def get_total_number_of_books(self):
        total = 0
        for section in self.sections.values():
            total += len(section.books)
        return total
