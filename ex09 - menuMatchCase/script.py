menuOpcoes = int(input("Digite o valor entre 1 e 4: "))


match menuOpcoes:
    case 1:
        nomeCompleto = input("Digite seu nome completo: ")
        idade = int(input("Digite sua idade: "))
        print( "- " * 5 + "Cadastro do aluno" + " -" * 5)
        print(f"Nome: {nomeCompleto}")
        print(f"Idade: {idade}")
        print("-" * 37)
    case 2:
        print("-" * 5 + "Suas notas" + "-" * 5)
        print("Matematica: 7")
        print("Português: 10")
        print("Fisica: 6")
        print("-" * 20)
    case 3:
        print("Atualize os dados de seu cadastro!!")
    case 4:
        print("Sistema desligado")
    case _:
        print("Digite um valor valido")
