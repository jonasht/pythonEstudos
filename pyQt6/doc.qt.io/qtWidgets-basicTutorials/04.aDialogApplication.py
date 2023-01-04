import sys
from PySide6.QtWidgets import (QLineEdit,
                               QPushButton,
                               QApplication,
                               QVBoxLayout,
                               QDialog)




class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.edit = QLineEdit('escreve seu nome')
        self.button = QPushButton('mostrar saudacoes ')

        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)

        self.setLayout(layout)

        self.button.clicked.connect(self.greetings)

    def greetings(self):
        print(f'ola {self.edit.text()}')

        
if __name__ == "__main__":
    root = QApplication(sys.argv)

    form = Form()
    form.show()

    sys.exit(root.exec())
    