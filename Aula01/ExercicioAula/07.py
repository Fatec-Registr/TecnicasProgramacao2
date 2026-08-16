# 7. Faça um algoritmo que leia nome a idade de uma pessoa, e escreva quantos dias essa pessoa já viveu. Considerar ano com 365 dias. Atenção mostre o nome e quantidade de dias que a pessoa viveu

nome = input("informe o nome da pessoa:\n")
idade = int(input(f"Infome a idade em anos do(a) {nome}:\n"))
dias = 365*idade

print(f"O(a) {nome} possui aproximadamente {dias} dias de vida")