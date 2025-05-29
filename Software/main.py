from models.Administrador import Administrador
from models.Vendedor import Vendedor
from models.Comprador import Comprador
from controllers.criptografia import gerar_hash_senha
from controllers.autenticacao import fazer_login

def menu_administrador(admin):
    while True:
        print("""
Menu Administrador:
1 - Cadastrar usuário
2 - Buscar vendas
3 - Buscar estoque mínimo
4 - Adicionar produtos
5 - Baixar relatório
6 - Alterar senha
0 - Logout
""")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            admin.cadastrar_usuario()
        elif opcao == "2":
            admin.buscar_vendas()
        elif opcao == "3":
            admin.buscar_estoque_minimo()
        elif opcao == "4":
            admin.adicionar_produtos()
        elif opcao == "5":
            admin.baixar_relatorio()
        elif opcao == "6":
            admin.alterar_senha()
        elif opcao == "0":
            print("Logout...")
            break
        else:
            print("Opção inválida.")

def menu_vendedor(vendedor):
    while True:
        print("""
Menu Vendedor:
1 - Registrar venda
2 - Ver produtos
3 - Alterar senha
0 - Logout
""")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            vendedor.registrar_venda()
        elif opcao == "2":
            vendedor.ver_produtos()
        elif opcao == "3":
            vendedor.alterar_senha()
        elif opcao == "0":
            print("Logout...")
            break
        else:
            print("Opção inválida.")

def menu_comprador(comprador):
    while True:
        print("""
Menu Comprador:
1 - Buscar estoque mínimo
2 - Comprar produtos
3 - Alterar senha
0 - Logout
""")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            comprador.buscar_estoque_minimo()
        elif opcao == "2":
            comprador.comprar_produtos()
        elif opcao == "3":
            comprador.alterar_senha()
        elif opcao == "0":
            print("Logout...")
            break
        else:
            print("Opção inválida!")

def main():
    print("Bem-vindo ao sistema de gerenciamento!")

    while True:
        opcao = input("""
Selecione uma opção:
1 - Login
2 - Sair
""")
        if opcao == "1":
            usuario = fazer_login()
            if usuario:
                id_, nome, cpf, email, senha, tipo = usuario
                if tipo == "administrador":
                    admin = Administrador(id_, nome, cpf, email, senha, tipo)
                    menu_administrador(admin)
                elif tipo == "vendedor":
                    vendedor = Vendedor(id_, nome, cpf, email, senha)
                    menu_vendedor(vendedor)
                elif tipo == "comprador":
                    comprador = Comprador(id_, nome, cpf, email, senha, tipo)
                    menu_comprador(comprador)
                else:
                    print("Tipo de usuário desconhecido.")
        elif opcao == "2":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
