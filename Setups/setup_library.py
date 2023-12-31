from Classes.library import Library


class LibrarySetup:
    @classmethod
    def setup_library(cls, data):
        library = Library("Main Library")
        for book_title, book_details in data.items():
            section_name = book_details["section"]
            library.addSection(section_name)
            library.sections[section_name].addBook(
                book_title, book_details["author"], book_details["cost"]
            )

        return library
