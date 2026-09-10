'''
Escreva um programa que leia o peso de uma pessoa na Terra e o número de um planeta e mostre o valor do seu peso neste planeta.
A relação de planetas é dada a seguir juntamente com o valor das gravidades relativas á Terra:
peso = pesodapessoa * gravidade
Exemplo se usuário digitar a opção 2,  o calculo será
peso = pesodapessoa * 0.88

| Número | Gravidade | Planeta  |
| -----: | --------: | -------- |
|      1 |      0,37 | Mercúrio |
|      2 |      0,88 | Vênus    |
|      3 |      0,38 | Marte    |
|      4 |      2,64 | Júpiter  |
|      5 |      1,15 | Saturno  |

'''
peso = float(input("Informe o peso de uma pessoa no planeta Terra:"))
op = int(input(f"Escolha o planeta para verificar esse peso {peso:.2f} em outro planeta:\n1-Mercurio\n2-Vênus\n3-Marte\n4-Jupiter\n5-Saturno"))

match op:
    case 1:
        gravidade = 0.37
        planeta = "Mercurio"
    case 2:
        gravidade = 0.88
        planeta = "Venus"
    case 3:
        gravidade = 0.38
        planeta = "Marte"
    case 4:
        gravidade = 2.64
        planeta = "Jupiter"
    case 5:
        gravidade = 1.15
        planeta = "Saturno"
    case _:
        planeta = "Categoria nao cadastrada"
        exit()

novoPeso = peso*gravidade 
print(f"Planeta escolhido: {planeta}\nPeso na Terra: {peso:.2f}Kg\nGravidade: {gravidade} da terra\nPeso no planeta {planeta}: {novoPeso:.2f}Kg")

