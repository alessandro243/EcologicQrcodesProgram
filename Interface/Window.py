from PySide6.QtWidgets import QLabel, QWidget, QGridLayout, QVBoxLayout, QHBoxLayout, QPushButton
from Interface.Grids.ImportGrids import firstGrid

class Window(QWidget):
    senha = '2025'
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janelinha Rápida")
        self.sizeConfig()

        layout = QVBoxLayout()
        layout1 = QGridLayout()
        layout2 = QGridLayout()

        layout.addLayout(layout1)
        layout.addLayout(layout2)

        self.setLayout(layout)
        self.makeGrid(layout1, layout2)

    def sizeConfig(self):
        self.setFixedSize(1000, 600)

    def icreaseButton(self, text, width, hight, positionx, positiony, visible, align, layout, func=None):
        btn = QPushButton(text)

        if func is not None:
            btn.clicked.connect(func)

        if not visible:
            btn.setFlat(True)
            btn.setStyleSheet("background: transparent; border: none;")
            btn.setEnabled(False)
        
        btn.setFixedSize(width, hight)
        layout.addWidget(btn, positionx, positiony, align)
        return self
    
    def icreaseLabel(self, text, positionx, positiony, align, layout, style, width, hight):
        label = QLabel(text)
        label.setStyleSheet(style)
        label.setFixedSize(width, hight)
        layout.addWidget(label, positionx, positiony, align)
        return self
        
    def makeGrid(self, layout1, layout2):
        firstGrid(self, layout1, layout2)