class EventDispatcher:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def sell_a_book(self, book_name):
        for subscriber in self.subscribers:
            subscriber.sell_a_book(book_name)
