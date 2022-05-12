import sys
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi Aplicacion")
        widget = QLabel("Hola Python")
        font = widget.font()
        font.setPointSize(30)
        widget.setFont(font)
        widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)
ventana = MainWindow()
ventana.show()
app.exec_()
