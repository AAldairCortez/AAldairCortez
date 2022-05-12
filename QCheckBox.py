import sys
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QCheckBox, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi Aplicacion")
        widget = QCheckBox("Hola soy un checkbox")
        widget .setCheckState(Qt.Checked)
        widget.stateChanged.connect(self.show_state)
        self.setCentralWidget(widget)
    def show_state(self, s):
        print(s == Qt.Checked)
        print(s)
    
app = QApplication(sys.argv)
ventana = MainWindow()
ventana.show()
app.exec_()