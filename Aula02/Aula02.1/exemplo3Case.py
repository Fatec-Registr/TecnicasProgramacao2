cla = input("Digite a classificação A,B ou C:")
match cla.upper():
    case "A":
        print("Classificação esta no nivel 1")
    case "B":
        print("Classificação esta no nivel 2")
    case "C":
        print("Classificação esta no nivel 3")
    case _:
        print("Classificação invalida")