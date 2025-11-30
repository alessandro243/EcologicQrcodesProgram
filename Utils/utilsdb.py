import sqlite3
from sqlite3 import IntegrityError
import os, sys

def get_connection():
    import sys, os, sqlite3

    # Se estiver rodando como EXE
    if hasattr(sys, "_MEIPASS"):
        base_path = sys._MEIPASS

    else:
        # Raiz do projeto quando rodando em Python normal
        base_path = os.path.dirname(os.path.abspath(sys.argv[0]))

    # Caminho correto do banco
    db_path = os.path.join(base_path, "Baks", "tabels.sqlite3")

    return sqlite3.connect(db_path)



def makeQrTable(tabela):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        f'CREATE TABLE IF NOT EXISTS {tabela} '
        '('
        'ID TEXT PRIMARY KEY, '
        'DATA TIMESTAMP, '
        'USED BOOLEAN, '
        'CPF_CLIENTE TEXT, '
        'DATA_USE TIMESTAMP'
        ')'
        )
    
    cursor.close()
    conn.close()

def makeClientTable(tabela):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f'CREATE TABLE IF NOT EXISTS {tabela} '
    '('
    'CPF CHAR(11) PRIMARY KEY,'
    'POINTS INTEGER'
    ')'
    )
    cursor.close()
    conn.close()

#makeClientTable('Clients')
#makeQrTable('QrManager')

def insertQr(tabela, id, date1, cpf, date2, used=False):
    conn = get_connection()
    cursor = conn.cursor()
    quere = f'INSERT INTO {tabela} (ID, CPF_CLIENTE, DATA, DATA_USE, USED) values(?, ?, ?, ?, ?)'
    cursor.execute(quere, (id, date1, cpf, date2, used))
    conn.commit()
    
    cursor.close()
    conn.close()

def insertClient(tabela, cpf, points):
    conn = get_connection()
    cursor = conn.cursor()
    quere = f'INSERT INTO {tabela} (CPF, POINTS) VALUES (?, ?)'
    cursor.execute(quere, (cpf, points))
    conn.commit()
    
    cursor.close()
    conn.close()

def clientFounder(tabela, cpf):
    conn = get_connection()
    cursor = conn.cursor()
    quere = f"SELECT CPF FROM {tabela} WHERE CPF = '{cpf}'"
    cursor.execute(quere)
    retorno = cursor.fetchall()
    cursor.close()
    conn.close()
    return retorno

def codeValidator(tabela, codigo):
    conn = get_connection()
    cursor = conn.cursor()
    quere = f"SELECT ID, USED FROM {tabela} WHERE ID = '{codigo}'"
    cursor.execute(quere)
    retorno = cursor.fetchall()
    cursor.close()
    conn.close()
    return retorno

def codeUpdater(tabela, id, cpf, used, day):
    conn = get_connection()
    cursor = conn.cursor()
    quere = f"UPDATE {tabela} SET CPF_CLIENTE = ?, USED = ?, DATA_USE = ? WHERE ID = ?"

    cursor.execute(quere, (cpf, used, day, id))
    conn.commit()
    cursor.close()
    conn.close()

def foundPoints(tabela, cpf):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT POINTS FROM {tabela} WHERE CPF = '{cpf}'")
    retorno = cursor.fetchall()
    cursor.close()
    conn.close()
    return retorno

def sumPoints(tabela, pnts, cpf):
    pnt = foundPoints(tabela, cpf)[0][0]
    npnt = pnt + pnts
    conn = get_connection()
    cursor = conn.cursor()
    quere = f"UPDATE {tabela} SET POINTS = ? WHERE CPF = ?"
    cursor.execute(quere, (npnt, cpf))
    conn.commit()
    cursor.close()
    conn.close()
    return npnt

def pointsUpdater(tabela, cpf):
    conn = get_connection()
    cursor = conn.cursor()
    quere = f"UPDATE {tabela} SET POINTS = ? WHERE CPF = ?"

    cursor.execute(quere, (0, cpf))
    conn.commit()
    cursor.close()
    conn.close()

def foundQrCodes(tabela, used):
    conn = get_connection()
    cursor = conn.cursor()

    if used:
        quere = f'''
            SELECT 
                q.ID,
                q.DATA,
                q.CPF_CLIENTE,
                q.DATA_USE,
                c.POINTS
            FROM {tabela} AS q
            INNER JOIN Clients AS c
                ON q.CPF_CLIENTE = c.CPF
            WHERE q.USED = 1
        '''
    else:
        quere = f'''
            SELECT 
                ID,
                DATA
            FROM {tabela}
            WHERE USED = 0
        '''

    cursor.execute(quere)
    retorno = cursor.fetchall()
    cursor.close()
    conn.close()

    return retorno

#insertClient('Clients', '06574965705', 0)
#insertTest('QrManager')