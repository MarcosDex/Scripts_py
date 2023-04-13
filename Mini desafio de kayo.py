array = []

while True:

    print("\nMENU")
    print("1 - Listar")
    print("2 - Adicionar")
    print("3 - Remover")
    print("4 - Sair do programa")

    escolha = input("Digite o número da opção desejada: ")


    if escolha == "1":
        print("Array atual:", array)


    elif escolha == "2":
        while True:
            valor = input("Digite o valor a ser adicionado: ")
            array.append(valor)
            print("Valor adicionado com sucesso.")
            continuar = input("Deseja adicionar mais valores? (S/N): ")
            if continuar.upper() != "S":
                break



    elif escolha == "3":
        if len(array) == 0:
            print("Não há elementos no array.")
        else:
            removido = array.pop()
            print("Elemento removido:", removido)


    elif escolha == "4":
        print("Programa encerrado.")
        break


    else:
        print("Opção inválida. Tente novamente.")
