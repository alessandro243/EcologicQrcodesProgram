from Entities.QrMaker import QrMaker
from Interface.Window import Window
import sys
from PySide6.QtWidgets import QApplication
from Utils.utilsdb import makeClientTable, makeQrTable

makeClientTable('Clients')
makeQrTable('QrManager')

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
