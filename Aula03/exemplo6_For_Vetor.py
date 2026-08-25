# lê os valores e armazena em uma lista (vetor)
# commando append para adicionar os dados no vetor

lista= []
for i in range(1,6):
    num = int(input(f"digite o {i}º numero:"))
    lista.append(num)

print ("Numeros armazenados na lista:")
for i in lista:
    print(i)