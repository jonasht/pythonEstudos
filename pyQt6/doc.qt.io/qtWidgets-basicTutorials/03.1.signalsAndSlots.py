import sys
from PySide6.QtWidgets import QApplication, QPushButton


def function():
    print('the .function. has been called')
    print('a funcao foi chamada')

root = QApplication()
button = QPushButton('call function')
button.clicked.connect(function)

button.show()
sys.exit(root.exec())

