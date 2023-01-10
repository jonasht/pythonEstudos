import sys
from PyQt6.QtWidgets import QApplication, QWidget


app = QApplication(sys.argv)


janela = QWidget()

# definir o tamanho
janela.resize(500, 400)
janela.setWindowTitle('app')
janela.show()


app.exec()

