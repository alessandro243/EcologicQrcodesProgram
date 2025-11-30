from PySide6.QtCore import Qt
from Interface.Utils.cleanner import clearLayout

def externa(func):
    def inner(*args):
        return func(*args)
    return inner

def firstGrid(self, layout1, layout2):
    from Interface.Grids.ImportGrids import scannerGrid
    from Interface.Grids.QRCodeGeneratorGrid import qrCodeGenerator
    from Interface.Grids.QRCodeLister import QRCodeLister
    
    clearLayout(layout1)
    clearLayout(layout2)
    self.icreaseButton('',200, 20, 0, 0, False, Qt.AlignTop, layout1)
    self.icreaseButton('Gerar QRCodes',200, 60, 1, 0, True, Qt.AlignTop, layout1, lambda: qrCodeGenerator(self, layout1, layout2))
    self.icreaseButton('Escanear QRCodes',200, 60, 1, 1, True, Qt.AlignTop, layout1, lambda: scannerGrid(self, layout1, layout2))
    self.icreaseButton('Listar Qrcodes',200, 60, 1, 2, True, Qt.AlignTop, layout1, lambda: QRCodeLister(self, layout1, layout2))
    self.icreaseButton('',300, 60, 1, 4, False, Qt.AlignTop, layout1)
    self.icreaseButton('',200, 1000, 2, 0, False, Qt.AlignTop, layout1)
