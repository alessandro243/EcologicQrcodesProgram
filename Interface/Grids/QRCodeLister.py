from Interface.Utils.cleanner import clearLayout
from Entities.QrMaker import QrMaker
from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt
from Interface.Utils.LockWindow import PopupDialog
from Interface.Utils.listLabels import makeLabelsGridLister

def QRCodeLister(self, layout1, layout2):
    from Interface.Grids.InitGrid import firstGrid
    from Interface.Grids.ScannerGrid import scannerGrid
    from Interface.Grids.QRCodeGeneratorGrid import qrCodeGenerator
    clearLayout(layout1)
    clearLayout(layout2)

    qr = QrMaker()
    line = QLineEdit()
    box = PopupDialog(self, layout1, layout2)
    box.exec()
    line.setFixedSize(50, 30)
    
    if not box.fechado:
        window = self.icreaseButton('Menu',200, 60, 1, 0, True, Qt.AlignTop, layout1, lambda: firstGrid(self, layout1, layout2))
        self.icreaseButton('Escanear QRCodes',200, 60, 2, 0, True, Qt.AlignTop, layout1, lambda: scannerGrid(self, layout1, layout2))
        self.icreaseButton('Gerar Qrcodes',200, 60, 3, 0, True, Qt.AlignTop, layout1, lambda: qrCodeGenerator(self, layout1, layout2))
        self.icreaseButton('',50, 60, 1, 4, False, Qt.AlignTop, layout1)
        self.icreaseButton('Valid',80, 30, 4, 2, True, Qt.AlignTop, layout1, lambda: makeLabelsGridLister(layout2, window, False))
        self.icreaseButton('Used',80, 30, 4, 3, True, Qt.AlignTop, layout1, lambda: makeLabelsGridLister(layout2, window, True))
        self.icreaseButton('', 600, 600, 4, 1, False, Qt.AlignTop, layout1)
        #self.icreaseButton('',50, 600, 4, 1, False, Qt.AlignTop, layout1)
        
    else:
        firstGrid(self, layout1, layout2)