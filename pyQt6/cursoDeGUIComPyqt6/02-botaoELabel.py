import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel


app = QApplication(sys.argv)


janela = QWidget()

# definir o tamanho
janela.resize(800, 800)
janela.setWindowTitle('app')

# botao
bt = QPushButton('botao 1', janela)
bt.setGeometry(100, 100, 150, 80)
bt.setStyleSheet('background-color:darkgreen;color:red')

# label
lb = QLabel('este eh um texto', janela)
lb.move(400,100)
lb.setStyleSheet('color:yellow')

# mostrar
janela.show()



app.exec()

