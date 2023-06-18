from PySide6.QtWidgets import QApplication, QWidget
import sys
from Button_holder import Button_holder

app = QApplication(sys.argv)
window = Button_holder()
window.show()
app.exec()