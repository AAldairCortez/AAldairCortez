import sys
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QComboBox, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi Aplicacion Qt5")
        widget = QComboBox()
        widget.addItems(["Uno", "Dos", "Tres"])
        widget.currentIndexChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)
        self.setCentralWidget(widget)

    def index_changed(self, i):
        print(i)
    def text_changed(self, s):
        print(s)

app = QApplication(sys.argv)
ventana = MainWindow()
ventana.show()
app.exec_()
