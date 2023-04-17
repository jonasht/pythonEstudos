from sys import argv
from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow
from PyQt6.QtCore import QSize, Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.bt_is_checked = True
        
        self.setWindowTitle('Aplicativo')
        self.bt = QPushButton('aperta me ')
        self.bt.setCheckable(True)
        
        self.bt.released.connect(self.bt_was_released)

        self.bt.setChecked(self.bt_is_checked)


        self.setCentralWidget(self.bt)
        
    def bt_was_released(self):
        self.bt_is_checked = self.bt.isChecked()
        
        print('=-'*30+'=')
        print(self.bt_is_checked)

        print('=-'*30+'=')
        

        


        

app = QApplication(argv)

window = MainWindow()


window.show()

app.exec()


