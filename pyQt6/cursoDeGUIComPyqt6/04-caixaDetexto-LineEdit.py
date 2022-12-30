import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit



def func1():
    print('o botao da func1 foi apertada')
    lb.setText('botao 1 foi clicado')    
    lb.adjustSize()

def func2():
    print('o botao da func2 foi apertada')
    lb.setText('botao 2 foi clicado')    
    lb.adjustSize()

def func3():
    valor = le.text()
    lb.setText(valor)
    lb.adjustSize()

app = QApplication(sys.argv)


janela = QWidget()

# definir o tamanho
janela.resize(800, 800)
janela.setWindowTitle('app')

# botao =-=-=-=-=-=-=-=-=-=-=-=-=-=
bt = QPushButton('botao 1', janela)
bt.setGeometry(100, 100, 150, 80)
bt.clicked.connect(func1)

bt2 = QPushButton('botao 2', janela)
bt2.setGeometry(100, 200, 150, 80)
bt2.clicked.connect(func2)

bt3 = QPushButton('botao 3', janela)
bt3.setGeometry(100, 300, 150, 80)
bt3.clicked.connect(func3)

# label =-=-=-=-=-=-=-=-=-=-=-=-=
lb = QLabel('este eh um texto', janela)
lb.move(400,100)
lb.setStyleSheet('font-size:30px')

# lineEdit
le = QLineEdit("", janela)
le.setGeometry(500, 200, 150, 50)
# mostrar
janela.show()

n = 1


app.exec()

