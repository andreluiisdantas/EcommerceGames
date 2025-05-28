import sqlite3
from usuario import Usuario

conexao = sqlite3.connect("data/database.db")
cursor = conexao.cursor()

class Vendedor(Usuario):
    def __init__(self, id, nome, cpf, email, senha, tipo):
        super().__init__(id, nome, cpf, email, senha, tipo="vendedor")

    def registrar_venda(self):
        pass
