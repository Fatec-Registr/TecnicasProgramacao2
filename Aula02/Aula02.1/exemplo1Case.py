op = int(input("1-Sacar\n2-Extrato\n3-Sair\n"))

match op:
    case 1: 
        print("Voce escolheu sacar")
    case 2:
        print("Voce escolheu o extrato")
    case 3:
        print("Saindo....")
        exit
    case _:
        print("Opcao inválida")
