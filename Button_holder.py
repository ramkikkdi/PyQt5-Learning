from PySide6.QtWidgets import QPushButton,QMainWindow

class Button_holder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Button Holder Application")
        button = QPushButton("Press Me")
        self.setCentralWidget(button)
