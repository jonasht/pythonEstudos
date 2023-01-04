import sys
from PySide6.QtWidgets import QApplication, QLabel


root = QApplication(sys.argv)
label = QLabel('hello world/ola mundo')
label.show()
root.exec()