import firebase_admin
from firebase_admin import db, credentials
import json


class Firebase:
    @classmethod
    def __init__(cls):
        cred = credentials.Certificate("Setups/creds.json")

        firebase_admin.initialize_app(
            cred,
            {
                "databaseURL": "https://curt-task-d5de4-default-rtdb.europe-west1.firebasedatabase.app/"
            },
        )
        cls.ref = db.reference("/")

        data = json.load(open("Setups/books.json"))
        cls.ref.set(data)

    @classmethod
    def get(cls):
        return cls.ref.get()

    @classmethod
    def sell_a_book(cls, book):
        cls.ref.child(book).delete()


if __name__ == "__main__":
    Firebase()
    print(Firebase.get())
    # firebase.sell_a_book("Little Women")
    print(Firebase.get())
