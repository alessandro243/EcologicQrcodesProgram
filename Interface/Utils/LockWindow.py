from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton
from Interface.Utils.Popup import mostrar_popup
import sys

class PopupDialog(QDialog):
    def __init__(self, self_, layout1, layout2, parent=None,):
        from Interface.Window import Window
        super().__init__(parent)
        self.key = Window.senha
        self.self_ = self_
        self.layout1 = layout1
        self.layout2 = layout2
        self.setWindowTitle("Senha de acesso")
        self.setFixedSize(300, 100)
        self.fechado = False

        layout = QVBoxLayout(self)

        layout.addWidget(QLabel("Digite a Senha:"))
        self.edit = QLineEdit()
        layout.addWidget(self.edit)

        ok = QPushButton("OK")
        ok.clicked.connect(self.on_ok)
        layout.addWidget(ok)

    def on_ok(self):
        writedPassword = self.edit.text()
        
        if writedPassword == self.key:
            self.accept()
            return

        elif writedPassword == '':
            mostrar_popup(self, 'Invalid Key', 'Digite uma senha!')
            self.edit.clear()    

        else:
            mostrar_popup(self, 'Invalid Key', 'A senha digitada está incorreta!')
            self.edit.clear()
    
    def closeEvent(self, event):
        self.fechado = True
        super().closeEvent(event)