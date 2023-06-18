# Importing the Packages required for the application
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow,QPushButton
import sys

## Creating a application
app = QApplication(sys.argv)

## Creating a QWidget
window = QMainWindow()
window.setWindowTitle("Button Actions")

## Defining a function for the button
def button_clicked():
    print("Button clicked, Didn't you")

button = QPushButton()
button.setText("Click Me!")
window.setCentralWidget(button)
button.clicked.connect(button_clicked)

## Note: Instead of placing the button directly on the window, we can keep like the button.show()
## But also remember that the title of the window will not be displayed as the one like we have given
## So that the button will emerge itself in the window
window.show()
app.exec()
