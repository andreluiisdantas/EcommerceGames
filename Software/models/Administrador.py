import sqlite3
import pandas as pd
from models.usuario import Usuario
from controllers.criptografia import gerar_hash_senha

class Administrador(Usuario):
    def __init__(self, id, nome, cpf, email, senha, tipo):
        super().__init__(id, nome, cpf, email, senha, tipo)

    def cadastrar_usuario(self):
        nome = input("Digite o nome do novo colaborador: ")
        cpf = input("Digite o CPF do novo colaborador: ")
        email = input("Digite o e-mail do novo colaborador: ")
        senha = input("Digite a senha inicial: ")
        senha_hash = gerar_hash_senha(senha)
        tipo = input("Digite o tipo do colaborador:\n - vendedor\n - comprador\n").lower()

        conexao = sqlite3.connect("data/database.db")
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
        if cursor.fetchone():
            print("Erro: já existe um usuário com esse email.")
            conexao.close()
            return

        cursor.execute("""
            INSERT INTO usuarios (nome, cpf, email, senha, tipo)
            VALUES (?, ?, ?, ?, ?)
        """, (nome, cpf, email, senha_hash, tipo))

        conexao.commit()
        conexao.close()
        print("Usuário cadastrado com sucesso.")

    def buscar_vendas(self):
        conexao = sqlite3.connect("data/database.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT id_produto, id_vendedor, quantidade, data, valor_total FROM vendas")
        vendas = cursor.fetchall()
        conexao.close()

        if not vendas:
            print("Nenhuma venda registrada.")
            return

        for venda in vendas:
            id_produto, id_vendedor, quantidade, data, valor_total = venda
            print(f"""
Produto: {id_produto}
Vendedor: {id_vendedor}
Quantidade: {quantidade}
Data: {data}
Valor total: R$ {valor_total:.2f}
""")

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

    def adicionar_produtos(self):
        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: "))
        estoque_minimo = int(input("Digite o estoque mínimo do produto: "))
        estoque = 0

        conexao = sqlite3.connect("data/database.db")
        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO produtos (nome, preco, estoque, estoque_minimo)
            VALUES (?, ?, ?, ?)
        """, (nome, preco, estoque, estoque_minimo))
        conexao.commit()
        conexao.close()

    def baixar_relatorio(self):
        conexao = sqlite3.connect("data/database.db")
        cursor = conexao.cursor()

        cursor.execute("SELECT id_produto, id_vendedor, quantidade, data, valor_total FROM vendas")
        vendas = cursor.fetchall()
        if vendas:
            df_vendas = pd.DataFrame(vendas, columns=["id_produto", "id_vendedor", "quantidade", "data", "valor_total"])
            df_vendas.to_excel("data/relatorio_vendas.xlsx", index=False)
            print("Relatório de vendas salvo em relatorio_vendas.xlsx")
        else:
            print("Nenhuma venda encontrada para gerar relatório.")

        cursor.execute("SELECT nome, preco, estoque, estoque_minimo FROM produtos")
        produtos = cursor.fetchall()
        if produtos:
            df_produtos = pd.DataFrame(produtos, columns=["nome", "preco", "estoque", "estoque_minimo"])
            df_produtos.to_excel("data/relatorio_estoque.xlsx", index=False)
            print("Relatório de estoque salvo em relatorio_estoque.xlsx")
        else:
            print("Nenhum produto encontrado para gerar relatório.")

        conexao.close()
