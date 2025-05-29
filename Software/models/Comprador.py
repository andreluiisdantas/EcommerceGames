import sqlite3
from models.usuario import Usuario

class Comprador(Usuario):
    def __init__(self, id, nome, cpf, email, senha, tipo):
        super().__init__(id, nome, cpf, email, senha, tipo)

    def buscar_estoque_minimo(self):
        nome = input("Digite o nome do produto: ")
        conexao = sqlite3.connect("data/database.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT nome, estoque, estoque_minimo FROM produtos WHERE nome LIKE ?", (f"%{nome}%",))
        produtos = cursor.fetchall()
        conexao.close()

        if not produtos:
            print("Nenhum produto encontrado")
            return

        for nome, estoque, estoque_minimo in produtos:
            print(f'Nome: {nome} | Estoque atual: {estoque} | Estoque mínimo: {estoque_minimo}')

    def comprar_produtos(self):
        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o valor unitário do produto: "))
        quantidade = int(input("Digite a quantidade: "))

        conexao = sqlite3.connect("data/database.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT id, preco, estoque FROM produtos WHERE nome LIKE ?", (f"%{nome}%",))
        produto = cursor.fetchone()

        if not produto:
            print("Este produto não está cadastrado no sistema.")
            conexao.close()
            return

        produto_id, preco_atual, estoque_atual = produto
        novo_estoque = estoque_atual + quantidade
        novo_preco = preco * 2

        cursor.execute("UPDATE produtos SET estoque = ?, preco = ? WHERE id = ?", (novo_estoque, novo_preco, produto_id))
        conexao.commit()
        conexao.close()
        print("Compra registrada e estoque atualizado.")
