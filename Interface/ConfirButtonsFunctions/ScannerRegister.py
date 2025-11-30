from Exceptions.Errors import InvalidCPF
from Utils.utilsdb import clientFounder, insertClient, codeValidator, codeUpdater, sumPoints, pointsUpdater
from Interface.Utils.Popup import mostrar_popup
import datetime

def validar_cpf(cpf: str) -> bool:

    cpf = ''.join(filter(str.isdigit, cpf))
    if len(cpf) != 11:
        return False
    
    if cpf == cpf[0] * 11:
        return False

    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma * 10 % 11) % 10
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma * 10 % 11) % 10

    return cpf[-2:] == f"{digito1}{digito2}"

def RegisterQR(self, line1, line2):
    text1 = line1.text().replace("-", "").replace(".","")
    text2 = line2.text()

    if not validar_cpf(text1):
        mostrar_popup(self, "CPF inválido", "O CPF informado não é um CPF válido!")
        raise InvalidCPF("CPF inválido")
        
    
    clientes = clientFounder('Clients',text1)
    code = codeValidator('QrManager', text2)

    if len(clientes) > 0:
        clientes = clientes[0]

    if len(clientes) < 1:
        print("O CPF não foi encontrado. Registrando CPF...")
        insertClient('Clients', text1, 0)
    
    if len(code) > 0:
        code = code[0]

    if len(code) < 1:
        mostrar_popup(self, "Código desconhecido", "O código não é um código válido!")
    elif len(code) > 0:
        today = datetime.datetime.now().date()
        print(code[0], code[1])
        
        if int(code[1]) > 0:
            mostrar_popup(self, "Código inválido", "O código não é um código válido!")
            return
        else:
            print('Estou aqui')
            codeUpdater("QrManager", text2, text1, True, today)
            pontos = sumPoints('Clients', 10, text1)
            mostrar_popup(self, "Promoção registrado!", f"10 pontos adquiridos, faltam apenas {100-pontos} para adquirir a promoção.")
            if pontos >= 100:
                mostrar_popup(self, "Promoção atingida!", "Imprimindo cartão de desconto")
                pointsUpdater('Clients', text1)
