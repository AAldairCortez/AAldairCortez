from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import Qt
import sys
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi aplicacion")
        Button = QPushButton("Precioname")
        Button.setCheckable(True)
        Button.clicked.connect(self.the_button_was_clicked)
        self.setCentralWidget(Button) 
    def the_button_was_clicked(self):
        print("!Hiciste clic!")
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()