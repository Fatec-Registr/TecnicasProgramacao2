#Faça um algoritmo que leia o ano de nascimento de uma pessoa, e leia o nome da pessoa, leia o ano atual e escreva quantos anos essa pessoa tem, e mostre o nome digitado.

anoAtual= int(input("Informe o anoa atual:\n"))
nome = input("Informe o nome da pessoa:\n")
anoNasc= int(input("Informe o ano de nascimento:\n"))
idade = anoAtual - anoNasc

print(f"Nome: {nome}\nIdade: {idade}")
