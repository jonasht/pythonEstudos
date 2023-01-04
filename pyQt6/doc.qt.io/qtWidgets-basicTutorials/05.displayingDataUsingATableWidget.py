import sys
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem

colors = [('vermelho', 'Red', '#FF0000'),
          ('verde', 'Green', '#00FF00'),
          ('azul', 'Blue', '#0000FF'),
          ('preto', 'Black', '#000000'),
          ('branco', 'White', '#FFFFFF'),
          ('verdeEletrico', 'Electric Green', '#41CD52'),
          ('AzulEscuro', 'Dark Blue', '#222840'),
          ('Amarelo', 'Yellow', '#F9E56d')]


def get_rgb_from_hex(code):
    code_hex = code.replace("#", "")
    rgb = tuple(int(code_hex[i:i+2], 16) for i in (0, 2, 4))
    return QColor.fromRgb(rgb[0], rgb[1], rgb[2])

app = QApplication()

table = QTableWidget()
table.setRowCount(len(colors))
table.setColumnCount(len(colors[0]) + 1)
table.setHorizontalHeaderLabels(['Nome', 'Name', 'Hex Code', 'Color'])


for i, (nome, name, code) in enumerate(colors):
    item_nome = QTableWidgetItem(nome)
    item_name = QTableWidgetItem(name)
    item_code = QTableWidgetItem(code)
    item_color = QTableWidgetItem()
    item_color.setBackground(get_rgb_from_hex(code))
    table.setItem(i, 0, item_nome)
    table.setItem(i, 1, item_name)
    table.setItem(i, 2, item_code)
    table.setItem(i, 3, item_color)
    
table.show()
sys.exit(app.exec())