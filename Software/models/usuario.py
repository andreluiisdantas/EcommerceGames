import sqlite3
from controllers.criptografia import gerar_hash_senha

class Usuario:
    def __init__(self, id, nome, cpf, email, senha, tipo):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.senha = senha
        self.tipo = tipo

    def alterar_senha(self):
        conexao = sqlite3.connect("data/database.db")
        cursor = conexao.cursor()

        senha_atual = input("Digite sua senha atual: ")
        senha_atual_hash = gerar_hash_senha(senha_atual)

        cursor.execute("SELECT senha FROM usuarios WHERE id = ?", (self.id,))
        senha_salva = cursor.fetchone()[0]

        if senha_atual_hash != senha_salva:
            print("Senha atual incorreta.")
            conexao.close()
            return

        nova_senha = input("Digite a nova senha: ")
        nova_senha_confirm = input("Confirme a nova senha: ")

        if nova_senha != nova_senha_confirm:
            print("As senhas não conferem.")
            conexao.close()
            return

        nova_senha_hash = gerar_hash_senha(nova_senha)
        cursor.execute("UPDATE usuarios SET senha = ? WHERE id = ?", (nova_senha_hash, self.id))
        conexao.commit()
        conexao.close()
        print("Senha alterada com sucesso!")

    def mostrar_nome(self):
        print(f"Usuário: {self.nome}")

    def ver_produtos(self):
        conexao = sqlite3.connect("data/database.db")
        cursor = conexao.cursor()

        opcao = int(input("Selecione a opção:\n 1-Ver todos\n 2-Buscar Produto\n"))

        if opcao == 1:
            cursor.execute("SELECT nome, estoque, estoque_minimo FROM produtos")
            produtos = cursor.fetchall()

            if not produtos:
                print("Nenhum produto no estoque.")
            else:
                for nome, estoque, estoque_minimo in produtos:
                    print(f'Nome: {nome} | Estoque atual: {estoque} | Estoque mínimo: {estoque_minimo}')

        elif opcao == 2:
            nome_busca = input("Digite o nome do produto: ")
            cursor.execute("SELECT nome, estoque, estoque_minimo FROM produtos WHERE nome LIKE ?", (f"%{nome_busca}%",))
            produtos = cursor.fetchall()

            if not produtos:
                print("Nenhum produto encontrado.")
            else:
                for nome, estoque, estoque_minimo in produtos:
                    print(f'Nome: {nome} | Estoque atual: {estoque} | Estoque mínimo: {estoque_minimo}')
        else:
            print("Opção inválida.")

        conexao.close()

    def buscar_produtos(self):
        conexao = sqlite3.connect("data/database.db")
        cursor = conexao.cursor()

        nome_busca = input("Digite o nome do produto: ")
        cursor.execute("SELECT nome, estoque, preco FROM produtos WHERE nome LIKE ?", (f"%{nome_busca}%",))
        produtos = cursor.fetchall()

        if not produtos:
            print("Nenhum produto encontrado.")
        else:
            for nome, estoque, preco in produtos:
                print(f'Nome: {nome} | Estoque: {estoque} | Preço: R${preco:.2f}')

        conexao.close()
