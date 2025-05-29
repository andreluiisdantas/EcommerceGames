import sqlite3
from models.usuario import Usuario
from models.venda import Venda

class Vendedor(Usuario):
    def __init__(self, id, nome, cpf, email, senha, tipo="vendedor"):
        super().__init__(id, nome, cpf, email, senha, tipo)

    def registrar_venda(self):
        conexao = sqlite3.connect("data/database.db")
        cursor = conexao.cursor()

        nome_produto = input("Digite o nome do produto: ")
        cursor.execute("SELECT id, preco, estoque FROM produtos WHERE nome LIKE ?", (f"%{nome_produto}%",))
        resultado_produto = cursor.fetchone()

        if not resultado_produto:
            print("Produto não encontrado.")
            conexao.close()
            return

        id_produto, preco_unitario, estoque_atual = resultado_produto

        try:
            quantidade = int(input("Digite a quantidade: "))
        except ValueError:
            print("Quantidade inválida.")
            conexao.close()
            return

        if quantidade > estoque_atual:
            print("Estoque insuficiente para a venda.")
            conexao.close()
            return

        venda = Venda(
            id_produto=id_produto,
            id_vendedor=self.id,
            quantidade=quantidade,
            valor_unitario=preco_unitario
        )
        venda.registrar_venda()
        conexao.close()
