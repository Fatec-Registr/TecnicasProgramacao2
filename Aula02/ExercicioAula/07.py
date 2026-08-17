'''EXERCÍCIOS
Faça um algoritmo que leia: o RG do empregado , o ano de seu nascimento e o ano de seu ingresso na empresa, e  ano atual.
O programa deverá calcular e mostrar a idade e o tempo  de trabalho do empregado e o Rg do empregado.

idade =  anoatual– anonascimento
tempotrabalho = anaoatual– anoingresso
Para estar em condições de aposentadoria, um dos seguintes requisitos deve ser:

- Ter no mínimo 65 anos de idade. 
'Requerer aposentadoria’

- Ter o tempo trabalho no mínimo 30 anos.
'Requerer aposentadoria’

- Ter no mínimo 60 anos e ter trabalhado no mínimo 30 anos
'Requerer aposentadoria’
 
Caso não satisfaça nenhuma das condições mostre: 
'Não requerer Aposentadoria'''
rg = input("Digite o rg do empregado:\n")
anoAtual = int(input("Digite o ano atual:\n"))
nasc = int(input("Digite o ano de nascimento:\n"))
anoIngresso = int(input("Digite o ano de ingresso na empresa:\n"))

idade = anoAtual - nasc
trabalho = anoAtual - anoIngresso
print(f"RG do Colaborador: {rg}\nIdade: {idade}\nTempo de trabalho: {trabalho} ano\n")
if idade >= 60 and trabalho>=30:
    print(f"Requerer aposentadoria")
elif idade>=65 or trabalho>=30:
    print(f"Requerer aposentadoria")
else:
    print(f"Não requerer Aposentadoria")