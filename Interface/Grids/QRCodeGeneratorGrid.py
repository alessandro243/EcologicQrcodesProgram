from PySide6.QtWidgets import QPushButton, QLabel, QLineEdit
from Entities.QrMaker import QrMaker
from Interface.Utils.cleanner import clearLayout
from PySide6.QtCore import Qt
from Interface.Utils.LockWindow import PopupDialog

def qrCodeGenerator(self, layout1, layout2):
    from Interface.Grids.InitGrid import firstGrid
    from Interface.Grids.ScannerGrid import scannerGrid
    from Interface.Grids.QRCodeLister import QRCodeLister
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
        self.icreaseButton('Listar Qrcodes',200, 60, 3, 0, True, Qt.AlignTop, layout1, lambda: QRCodeLister(self, layout1, layout2))
        self.icreaseButton('',50, 60, 1, 4, False, Qt.AlignTop, layout1)
        #self.icreaseButton('',300, 60, 2, 0, False, Qt.AlignTop, layout1)
        self.icreaseLabel("Qtd:", 3, 3, Qt.AlignRight, layout1,  "font-size: 16px;", 30, 100)
        layout1.addWidget(line, 3, 4)
        self.icreaseButton('Ok',60, 30, 3, 5, True, Qt.AlignLeft, layout1, lambda: qr.QrCodeMakker(layout2, window, line))
        self.icreaseButton('',200, 400, 5, 0, False, Qt.AlignTop, layout1)
        self.icreaseButton('',2400, 60, 3, 6, False, Qt.AlignTop, layout1)
        self.icreaseButton('',100, 60, 3, 2, False, Qt.AlignTop, layout1)
        self.icreaseButton('',400, 60, 3, 7, False, Qt.AlignTop, layout1)
        
    else:
        firstGrid(self, layout1, layout2)