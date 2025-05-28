print("Olá, Seja bem-vindo ao sistema de gerenciamento")

while True:
    opcao = int(input("""
Selecione uma opção:
1 - Login
2 - Sair
"""))

    if opcao == 1:
        print("Entrando...")
    elif opcao == 2:
        print("Saindo...")
        break
    else:
        print("Opção invalida! Tente novamente.")