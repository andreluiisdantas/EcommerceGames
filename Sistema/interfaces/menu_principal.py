from utilitarios.login import login

def menu_principal():
    while True:
        opcao = int(input("""
=== Menu Principal ===
1 - Fazer Login
2 - Sair
Escolha: """))

        if opcao == 1:
            login()
        elif opcao == 2:
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

menu_principal()
