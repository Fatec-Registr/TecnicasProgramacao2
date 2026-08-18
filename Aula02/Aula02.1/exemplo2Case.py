op = int(input("Digite um numero de 1 a 6:\n"))

match op:
    case 1| 2 |3:
        print("O numero escolhido foi 1 ou 2 ou 3:")
    case 4| 5 |6:
        print("O numero escolhido foi 4 ou 5 ou 6:")
    case _:
        print("Opcao Invalida")