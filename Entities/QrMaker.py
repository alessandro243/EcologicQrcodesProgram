import string
import qrcode
import random
import datetime
import os
import time

from Utils.ultils import dirCleanner, resource_path
from Interface.Utils.Popup import mostrar_popup
from Utils.utilsdb import insertQr, IntegrityError
from Exceptions.Errors import DuplicateQrIDError
from Interface.Utils.listLabels import makeLabelsGrid

class QrMaker():
    def __init__(self):
        self.QrList = []

    def idGenerator_(self):
        IdNumbers = str(random.randint(0, 10000000))
        letters = ''.join(random.choices(string.ascii_letters, k=3))
        return IdNumbers + letters
    
    def QrCodeMakker(self, layout, window, line):
        today = datetime.datetime.now().date()
        k = line.text()
        try:
            value = int(k)
        except ValueError:
            mostrar_popup(window, "Error", "Digite apenas número!")
            line.clear()
            return


        qr_folder = resource_path("../Qrcodes")  

        dirCleanner(qr_folder)  

        if value > 1:
            for x in range(value):
                name = f'Qrcode{x}.png'
                idKey = self.idGenerator_()
                dir_ = os.path.join(qr_folder, name)
                qr = qrcode.make(idKey)
                qr.save(dir_)
                
                try:
                    insertQr("QrManager", idKey, 'Null', today, 'Null')
                except IntegrityError:
                    raise DuplicateQrIDError("Esse ID já existe no banco. Ele não será imprimido.")

                os.startfile(dir_, 'print')
                self.QrList.append(idKey)
            
            makeLabelsGrid(layout, self.QrList, window, False)
            self.QrList.clear()
            line.clear()
            return
        
        # caso value seja 1 ou None
        name = f'Qrcode.png'
        dir_ = os.path.join(qr_folder, name)
        idKey = self.idGenerator_()
        self.QrList.append(idKey)
        qr = qrcode.make(idKey)
        qr.save(dir_)

        try:
            insertQr("QrManager", idKey, 'Null', today, 'Null')
        except IntegrityError:
            raise DuplicateQrIDError("Esse ID já existe no banco. Ele não será imprimido.")
        
        os.startfile(dir_, 'print')
        makeLabelsGrid(layout, self.QrList, window)
        self.QrList.clear()
        line.clear()
