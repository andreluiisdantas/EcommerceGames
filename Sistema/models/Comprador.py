import sqlite3
from usuario import Usuario

conexao = sqlite3.connect("data/database.db")
cursor = conexao.cursor()

class Comprador(Usuario):
    def __init__(self, id, nome, cpf, email, senha, tipo):
        super().__init__(id, nome, cpf, email, senha, tipo="comprador")

    def buscar_estoque_minimo(self):
        nome = input("Digite o nome do produto: ")

        cursor.execute("SELECT nome, estoque, estoque_atual FROM produtos WHERE nome LIKE ?", (f"%{nome}%",))
        produtos = cursor.fetchall()

        if not produtos:
            print("Nenhum produto encontrado")
            return

        for produto in produtos:
            nome, estoque, estoque_atual = produto
            print(f'Nome: {nome} Estoque atual: {estoque} Estoque minimo: {estoque_atual}')

    def comprar_produtos(self):
        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o valor unitário do produto: "))
        quantidade = int(input("Digite a quantidade: "))

        cursor.execute("SELECT nome FROM produtos WHERE nome LIKE ?", (f"%{nome}%",))
        produtos = cursor.fetchall()

        if not produtos:
            print("Este produto não esta cadastrado no sistema, favor avisar o gestor para que seja cadastrado.")
            return

        # Atualizando a quantidade
        cursor.execute("SELECT quantidade_atual FROM produtos WHERE nome LIKE ?", (f"%{nome}%",))
        quantidade_atual = cursor.fetchall()
        quantidade_atual += quantidade
        cursor.execute("UPDATE produtos SET quantiade_atual = ? WHERER nome LIKE ?", (quantidade_atual, nome))

        # Atualizando preco
        cursor.execute("SELECT preco FROM produtos WHERE nome LIKE ?", (f"%{nome}%",))
        preco_atual = cursor.fetchall()
        preco_novo = preco_atual * 2
        cursor.execute("UPDATE produtos SET preco = ? WHERER nome LIKE ?", (preco_novo, nome))





