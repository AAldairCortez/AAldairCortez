import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi Aplicacion")
        Button = QPushButton("Presioname!")
        self.setCentralWidget(Button)
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

