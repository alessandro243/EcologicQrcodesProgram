from PySide6.QtWidgets import QMessageBox

def mostrar_popup(self, tittle, content):
    QMessageBox.information(self, tittle, content)