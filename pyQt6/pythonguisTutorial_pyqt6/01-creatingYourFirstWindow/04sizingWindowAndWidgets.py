from sys import argv
from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow
from PyQt6.QtCore import QSize, Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Aplicativo')
        bt = QPushButton('aperta me ')
        self.setFixedSize(QSize(400, 300))
        self.setCentralWidget(bt)

        

app = QApplication(argv)

window = MainWindow()


window.show()

app.exec()


