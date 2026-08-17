'''
Construa um programa que receba o nome e peso de duas pessoas e mostre o nome e o peso da pessoa mais pesada ,e verifica se as pessoas tem o mesmo peso.
'''
nome1=input("Informe o nome da primeira pessoa: \n")
nome2=input("Informe o nome da segunda pessoa: \n")
peso1=float(input("Informe o peso da primeira pessoa:\n"))
peso2=float(input("Informe o peso da segunda pessoa:\n"))
if peso1==peso2:
    print(f"O peso do(a) {nome1} e {nome2} sao iguais {peso1} quilos.")
elif peso1>peso2:
    print(f"O peso do {nome1} é maior que {nome2}.")
else:
    print(f"O peso do {nome2} é maior que {nome1}.")