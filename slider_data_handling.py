## Make sure that the Slider has been imported here in the module import section
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QSlider
from PySide6.QtCore import Qt
import sys

## Creating a main application and also the window
app = QApplication(sys.argv)
window = QMainWindow()

## Giving the title for the window
window.setWindowTitle("Slider Data Handling")

## Defining a function for the slider
def respond_to_slider(data):
    print("The slider is moved to the position :  ", data)

slider = QSlider(Qt.Horizontal)
slider.setMinimum(1)
slider.setMaximum(100)

slider.setValue(25)
slider.valueChanged.connect(respond_to_slider)

## Application execution code
slider.show()
app.exec()

## Remember that for slider the function is valueChanged and for the button it is button clicked
## Whenever the action on the widgets changes (Click for button and slide for the slider)
## The function which gets binded to the widget will get called