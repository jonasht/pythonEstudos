from PyQt5.QtWidgets import *
import sys


class Window(QWidget):
    def __ini__(self):
        QWidget.__init__(self)
        self.setWindowTitle('ola')

        layout = QGridLayout()
        self.setLayout(layout)

        label = QLabel('ola mundo')
        layout.addWidget(label, 0,0)


app = QApplication(sys.argv)

screen = Window()
screen.show()

sys.exit(app.exec_())
