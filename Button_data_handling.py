## These are the python modules which has to be imported before using in our code
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
import sys

## Creating a main application and also the window
app = QApplication(sys.argv)
window = QMainWindow()

## Giving the title for the window
window.setWindowTitle("Button Data Handling")

## Defining a function for the button
def button_clicked(data):
    print("You clicked the button and the value is : ", data)

## Now defining the button parameters
button = QPushButton()
button.setText("Click")

## The below one will 
button.setCheckable(True)

## Locating the button in the window
window.setCentralWidget(button)
button.clicked.connect(button_clicked)

window.show()
app.exec()



