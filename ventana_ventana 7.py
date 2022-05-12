import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi aplicacion")
        Button = QPushButton("Precioname")
        Button.setCheckable(True)
        Button.clicked.connect(self.the_button_was_clicked)
        Button.clicked.connect(self.the_button_was_toggled)
        # set the cental wifget of the window 
        self.setCentralWidget(Button) 
    def the_button_was_clicked(self):
        print("!Hiciste clic!")
    def the_button_was_toggled(self, checked):
        print("¿Comprobado?", checked)
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()


