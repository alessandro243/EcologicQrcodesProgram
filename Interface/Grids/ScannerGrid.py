from Interface.Utils.cleanner import clearLayout
from Interface.ConfirButtonsFunctions.ScannerRegister import RegisterQR
from PySide6.QtWidgets import QLineEdit, QLabel
from PySide6.QtCore import Qt

def scannerGrid(self, layout1, layout2):
    from Interface.Grids.ImportGrids import firstGrid
    from Interface.Grids.QRCodeGeneratorGrid import qrCodeGenerator
    from Interface.Grids.QRCodeLister import QRCodeLister
    clearLayout(layout1)
    clearLayout(layout2)
    
    Qline1 = QLineEdit()
    Qline1.setFixedSize(500, 30)
    Qline2 = QLineEdit()
    Qline2.setFixedSize(500, 30)

    self.icreaseButton('Menu',200, 60, 1, 0, True, Qt.AlignTop, layout1, lambda: firstGrid(self, layout1, layout2))
    self.icreaseButton('Gerar QRCodes',200, 60, 1, 1, True, Qt.AlignTop, layout1, lambda: qrCodeGenerator(self, layout1, layout2))
    self.icreaseButton('Listar Qrcodes',200, 60, 1, 2, True, Qt.AlignTop, layout1, lambda: QRCodeLister(self, layout1, layout2))
    self.icreaseButton('',50, 100, 1, 0, False, Qt.AlignTop, layout1)
    self.icreaseButton('',10, 50, 2, 0, False, Qt.AlignTop, layout1)
    self.icreaseLabel("CPF:", 2, 1, Qt.AlignTop, layout1,  "font-size: 16px;", 150, 100)
    layout1.addWidget(Qline1, 2, 2)
    #self.icreaseButton('',10, 10, 3, 0, False, Qt.AlignTop, layout1)
    self.icreaseLabel("Código:", 4, 1, Qt.AlignTop, layout1, "font-size: 16px;", 150, 100)
    layout1.addWidget(Qline2, 4, 2)
    self.icreaseButton('',200, 1200, 6, 0, False, Qt.AlignTop, layout1)
    self.icreaseButton('Registrar',150, 30, 5, 3, True, Qt.AlignTop, layout1, lambda :RegisterQR(self, Qline1, Qline2))

