'''
Segundo uma tabela médica, o peso ideal está relacionado com a altura e o sexo.
Elabore um algoritmo que leia a altura e o sexo(M/F) de uma pessoa, calcule e mostre o  seu peso ideal, utilizando as seguintes fórmulas.
Para Masculino :  (72.7*altura)–58
Para Feminino :  (62.1*altura)–44.7
No final mostre a altura ,o sexo e peso ideal
'''
altura = float(input("Informe a altura da pessoa:\n"))
sexo = input ("Informe o sexo biologico da pessmo (M/F)")
if sexo == 'M'or sexo == 'm':
    peso = (72.7*altura) - 58
elif sexo == 'F'or sexo == 'f':
    peso = (62.1*altura) - 44.7
else :180
print('Informado o sexo de maneira errado.')

print(f"O peso ideal da pessoa é {peso:.2f}.")