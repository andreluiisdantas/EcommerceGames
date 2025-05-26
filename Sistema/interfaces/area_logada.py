def area_logada(usuario):
    tipo = usuario["tipo"].lower()

    print(f"\nBem-vindo à área logada, {usuario['nome']} ({usuario['tipo']})!")

    while True:
        print("\n=== Menu ===")

        if tipo == "administrador":
            print("1 - Gerenciar usuários")
            print("2 - Realizar vendas")
            print("3 - Realizar compras")
            print("4 - Ver estoque")
            print("5 - Ver relatórios")
            print("6 - Ver caixa")
        elif tipo == "vendedor":
            print("1 - Fazer vendas")
        elif tipo == "comprador":
            print("1 - Realizar compra")
        elif tipo == "estoquista":
            print("1 - Ver estoque")
            print("2 - Ver relatório")

        print("0 - Logout")

        opcao = input("Escolha uma opção: ")

        if tipo == "administrador":
            if opcao == "1":
                print("Gerenciando usuários...")
            elif opcao == "2":
                print("Abrindo interface de vendas...")
            elif opcao == "3":
                print("Abrindo interface de compras...")
            elif opcao == "4":
                print("Mostrando estoque...")
            elif opcao == "5":
                print("Gerando relatórios...")
            elif opcao == "6":
                print("Visualizando caixa...")
            elif opcao == "0":
                print("Logout realizado.")
                break
            else:
                print("Opção inválida.")
        elif tipo == "vendedor":
            if opcao == "1":
                print("Abrindo interface de vendas...")
            elif opcao == "0":
                print("Logout realizado.")
                break
            else:
                print("Opção inválida.")
        elif tipo == "comprador":
            if opcao == "1":
                print("Abrindo interface de compras...")
            elif opcao == "0":
                print("Logout realizado.")
                break
            else:
                print("Opção inválida.")
        elif tipo == "estoquista":
            if opcao == "1":
                print("Mostrando estoque...")
            elif opcao == "2":
                print("Mostrando relatórios de estoque...")
            elif opcao == "0":
                print("Logout realizado.")
                break
            else:
                print("Opção inválida.")
