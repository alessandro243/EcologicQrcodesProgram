from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QScrollArea, QGridLayout
from Interface.Utils.cleanner import clearLayout
from Utils.utilsdb import foundQrCodes

def makeLabelsGrid(layout, list, window, validator):
    clearLayout(layout)
    scroll = QScrollArea()
    scroll.setWidgetResizable(True)
    container = QWidget()
    grid_ = QGridLayout()
    container.setLayout(grid_)
    scroll.setWidget(container)
    scroll.setFixedSize(950, 250)

    layout.addWidget(scroll, 0, 0, 1, 1)

    if validator:
        for x, y in enumerate(list):
            if len(y) > 2:
                saida = f'Código: {y[0]} {10* ' '} Data de emissão: {y[1]} {10* ' '} CPF do cliente: {y[2]} {10* ' '} Data de uso: {y[3]} {10* ' '} Pontos do cliente: {y[4]}'
            else:
                saida = f'Código: {y[0]} {10* ' '} Data de emissão: {y[1]}'
            window.icreaseLabel(saida, x, 0, Qt.AlignLeft, grid_, "font-size: 13px;", 900, 20)
        return

    for x, y in enumerate(list):
        window.icreaseLabel(f'Código do QRcode registrado: {y}', x, 0, Qt.AlignLeft, grid_, "font-size: 13px;", 700, 15)
        #self.icreaseLabel("Qtd:", 3, 3, Qt.AlignRight, layout1,  "font-size: 16px;", 30, 100)

def makeLabelsGridLister(layout, window, value):
    lista = foundQrCodes('QrManager', value)
    makeLabelsGrid(layout, list(lista), window, True)
    