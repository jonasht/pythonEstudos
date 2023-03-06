from sys import argv
from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow
from PyQt6.QtCore import QSize, Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Aplicativo')
        bt = QPushButton('aperta me ')
        bt.setCheckable(True)
        bt.clicked.connect(self.bt_was_clicked)
        bt.clicked.connect(self.bt_was_toggled)

        self.setCentralWidget(bt)
    def bt_was_clicked(self):
        print('=-'*30+'=')
        print(f"{'botao foi clicado':^60}")
        print(f"{'button was clicked':^60}")
        
        print('=-'*30+'=')
        
    def bt_was_toggled(self, checked):
        print('checked:', checked)

        


        

app = QApplication(argv)

window = MainWindow()


window.show()

app.exec()


