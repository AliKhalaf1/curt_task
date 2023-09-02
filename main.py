from Setups.firebase import Firebase
from Setups.setup_library import LibrarySetup
from Setups.UI import BookTableWidget
import sys
from PyQt5.QtWidgets import QApplication
from Setups.event_dispatcher import EventDispatcher
import sys

##Obeserver Class
event_dispatcher = EventDispatcher()

## Firebase Class
db = Firebase()

## importing the data from firebase
data = db.get()

##Setting up the library
library = LibrarySetup.setup_library(data)

library.showSections()

##Setting up the UI
app = QApplication(sys.argv)
window = BookTableWidget(library, event_dispatcher)

# subscribe the event dispatcher to the database and library
event_dispatcher.subscribe(db)
event_dispatcher.subscribe(library)


window.show()

sys.exit(app.exec_())
