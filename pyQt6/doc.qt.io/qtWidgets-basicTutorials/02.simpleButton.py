import sys
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtCore import Slot


i = 0
# python func that logs the message to the console
@Slot()
def say_hello():
    global i
    i+=1
    print(f'button clicked, hello {i}')
    print('botao clicado, oi')

root = QApplication(sys.argv)

bt = QPushButton('click here')

bt.clicked.connect(say_hello)

bt.show()
root.exec()