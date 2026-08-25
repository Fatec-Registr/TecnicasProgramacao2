localiza = input("Digite uma fruta: ")

frutas=["banana","maça","manga","abacate","pera","kiwi"]

for i in frutas:
    if i == localiza:
        print(f"{localiza}, foi encontrada")
        break
    else:
        print(f"{localiza}, nao encontrada até o momento")
        