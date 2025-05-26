import sqlite3
import os

def conectar():
    caminho_banco = os.path.join(os.path.dirname(__file__), 'database.db')
    conexao = sqlite3.connect(caminho_banco)
    return conexao