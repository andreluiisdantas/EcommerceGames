import sqlite3

conexao = sqlite3.connect("data/database.db")
cursor = conexao.cursor()


class Usuario:
    def __init__(self, id, nome,cpf, email, senha, tipo):
        self.id = id
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.senha = senha
        self.tipo = tipo

    def autentica_senha(self):
        pass

    def buscar_tipo(self):
        pass

    def mostrar_nome(self):
        pass

    def ver_produtos(self):
        opcao = int(input("Selecione a opção:\n 1-Ver todos\n 2-Buscar Produto"))

        while True:
            if opcao == 1:
                cursor.execute("SELECT nome, estoque, estoque_minimo FROM produtos ")
                produtos = cursor.fetchall()

                if not produtos:
                    print("Nenhum no estoque")
                    return

                for produto in produtos:
                    nome, estoque, estoque_minimo = produto
                    print(f'Nome: {nome} Estoque atual: {estoque} Estoque minimo: {estoque_minimo}')
                break
            elif opcao == 2:
                nome = input("Digite o nome do produto: ")

                cursor.execute("SELECT nome, estoque, estoque_minimo FROM produtos WHERE nome LIKE ?", (f"%{nome}%",))
                produtos = cursor.fetchall()

                if not produtos:
                    print("Nenhum produto encontrado")
                    return

                for produto in produtos:
                    nome, estoque, estoque_minimo = produto
                    print(f'Nome: {nome} Estoque atual: {estoque} Estoque minimo: {estoque_minimo}')
            else:
                print("Opção invalidade, tente novamente")

    def buscar_produtos(self):
        nome = input("Digite o nome do produto: ")

        cursor.execute("SELECT nome, quantidade, preco FROM produtos WHERE nome LIKE ?", (f"%{nome}%",))
        produtos = cursor.fetchall()

        if not produtos:
            print("Nenhum produto encontrado")
            return

        for produto in produtos:
            nome, quantidade, preco = produto
            print(f'Nome: {nome} Quantidade: {quantidade} Preço: R${preco:.2f}')




