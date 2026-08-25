# 5) Dado uma lista com nomes [“Maria”, “João”, “Paulo”, “Magali”] 
# Digite um nome para localizar , se o nome pertence a lista , se 
# existir o nome na lista , mostre uma mensagem com o nome 
# encontrado, e pare a repetição, caso não encontre mostre nome 
# não encontrado. (UTILIZE FOR E IF)
localiza = input("Digite um nome para procurar na lista")

nomes = ["Maria", "João", "Paulo", "Magali"]

for i in nomes:
    if i.lower() == localiza.lower():
        print(f"{localiza}, foi encontrado na lista")
        break
    else:
        print(f"{localiza}, nao foi encontrado na lista")
        
