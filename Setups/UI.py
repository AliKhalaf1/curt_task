import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QLineEdit,
    QWidget,
    QPushButton,
)
import json
from .event_dispatcher import EventDispatcher


class BookTableWidget(QMainWindow):
    def __init__(self, library, event_dispatcher):
        super().__init__()
        self.event_dispatcher = event_dispatcher
        self.setWindowTitle("Book Information")
        self.setGeometry(100, 100, 800, 400)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Search Box for searching by title
        self.search_by_title = QLineEdit(self)
        self.search_by_title.setPlaceholderText("Search by Title")
        self.layout.addWidget(self.search_by_title)
        self.search_by_title.textChanged.connect(self.search_books_by_title)

        # Search Box for searching by author
        self.search_by_author = QLineEdit(self)
        self.search_by_author.setPlaceholderText("Search by Author")
        self.layout.addWidget(self.search_by_author)
        self.search_by_author.textChanged.connect(self.search_books_by_author)

        # Create a table
        self.tableWidget = QTableWidget(self)
        self.layout.addWidget(self.tableWidget)
        self.tableWidget.setRowCount(library.get_total_number_of_books())
        self.tableWidget.setColumnCount(
            5
        )  # Title, Author, Cost, Section, Delete Button
        # Set column headers
        self.tableWidget.setHorizontalHeaderLabels(
            ["Title", "Author", "Cost", "Section", ""]
        )
        self.populate_table(library)

    def populate_table(self, library):
        row = 0
        for section in library.sections.values():
            for book in section.books.values():
                self.tableWidget.setItem(row, 0, QTableWidgetItem(book.getTitle()))
                self.tableWidget.setItem(row, 1, QTableWidgetItem(book.getAuthor()))
                self.tableWidget.setItem(row, 2, QTableWidgetItem(str(book.getCost())))
                self.tableWidget.setItem(row, 3, QTableWidgetItem(section.getTitle()))

                # Create a delete button for each book
                delete_button = QPushButton("Delete", self)
                delete_button.clicked.connect(lambda _, row=row: self.delete_book(row))
                self.tableWidget.setCellWidget(row, 4, delete_button)

                row += 1

    def search_books_by_title(self):
        search_text = self.search_by_title.text().strip().lower()
        for row in range(self.tableWidget.rowCount()):
            title_item = self.tableWidget.item(row, 0)
            title = title_item.text().strip().lower()
            if search_text in title:
                self.tableWidget.setRowHidden(row, False)
            else:
                self.tableWidget.setRowHidden(row, True)

    def search_books_by_author(self):
        search_text = self.search_by_author.text().strip().lower()
        for row in range(self.tableWidget.rowCount()):
            title_item = self.tableWidget.item(row, 1)
            title = title_item.text().strip().lower()
            if search_text in title:
                self.tableWidget.setRowHidden(row, False)
            else:
                self.tableWidget.setRowHidden(row, True)

    # def delete_book(self, row):
    #     title_item = self.tableWidget.item(row, 0)
    #     title = title_item.text()

    def delete_book(self, row):
        title_item = self.tableWidget.item(row, 0)
        title = title_item.text()
        self.event_dispatcher.sell_a_book(title)
        self.tableWidget.removeRow(row)
