import sqlite3
from usuario import Usuario

conexao = sqlite3.connect("data/database.db")
cursor = conexao.cursor()

class Adminstrador(Usuario):
    def __init__(self, id, nome, cpf, email, senha, tipo):
        super().__init__(id, nome, cpf, email, senha, tipo="Administrador")

    def cadastrar_usuario(self):
        nome = input("Digite o nome do novo colaborador: ")
        cpf = input("Digite o CPF do novo colaborador: ")
        email = input("Digite o e-mail do novo colaborador: ")
        senha = input("Digite a senha inicial: ")
        tipo = input("Digite o tipo do colaborador:\n - Vendedor\n - Comprador\n").lower()

        cursor.execute("INSERT INTO usuarios (nome, cpf, email, senha, tipo) VALUES (?, ?, ?, ?, ?)",(nome, cpf, email, senha, tipo))

    def buscar_vendas(self):

        cursor.execute("SELECT produto_id, vendedor_id, comprador_id, quantidade, data, valor_total FROM vendas")
        vendas = cursor.fetchall()

        if not vendas:
            print("Nenhum produto encontrado")
            return

        for venda in vendas:
            id_produto, id_vendedor, id_comprador, quantidade, data, valor_total = venda
            print(f"""
Código produto: {id_produto}
Código vendedor: {id_vendedor}
Código comprador: {id_comprador}
Quantidade: {quantidade}
Data: {data}
Valor total: R${valor_total:2.f}
""")

    def buscar_estoque_minimo(self):
        nome = input("Digite o nome do produto: ")

        cursor.execute("SELECT nome, estoque, estoque_minimo FROM produtos WHERE nome LIKE ?", (f"%{nome}%",))
        produtos = cursor.fetchall()

        if not produtos:
            print("Nenhum produto encontrado")
            return

        for produto in produtos:
            nome, estoque, estoque_minimo = produto
            print(f'Nome: {nome} Estoque atual: {estoque} Estoque minimo: {estoque_minimo}')

    def adicionar_produtos(self):
        nome = input("Digite o nome do produto: ")
        preco = input("Digite o preço do produto: ")
        estoque_minimo = input("Digite o estoque minimo do produto: ")
        estoque = 0

        cursor.execute("INSERT INTO PRODUTOS (nome, preco, estoque, estoque_minimo) VALUES (?, ?, ?, ?, )",(nome, preco, estoque, estoque_minimo))

    def baixar_relatorio(self):
        pass


