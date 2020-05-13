import sys
from PySide2.QtWidgets import (QLineEdit, QPushButton, QApplication,
    QVBoxLayout, QDialog)
from managers.ApiManager import ApiManager

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.ApiManager = ApiManager()

        # Create widgets
        self.edit = QLineEdit("Write your api key here")
        self.button = QPushButton("Connect")

        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)

        # Set dialog layout
        self.setLayout(layout)

        # Add button signal to greetings slot
        self.button.clicked.connect(self.joke)

    # Greets the user
    def joke(self):
        # Connects to the api
        self.ApiManager.get_key(self.edit.text())
        # Prints a random joke
        print(self.ApiManager.joke())

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec_())