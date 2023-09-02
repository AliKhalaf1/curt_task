class Book:
    def __init__(self, title, author, cost):
        self.title = title
        self.author = author
        self.cost = cost

    def getTitle(self):
        return self.title

    def getAuthor(self):
        return self.author

    def getCost(self):
        return self.cost

    def print_book_details(self):
        print(f"Title: {self.title}, Author: {self.author}, Cost: {self.cost}")
