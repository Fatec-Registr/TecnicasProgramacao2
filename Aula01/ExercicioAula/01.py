#1. Construa um programa para calcular, altura em cm, no qual um usuário informe a sua estatura em metros e o programa converta-a para centímetros. (cm = m *100)

altura = float(input("Digite o  valor da altura em metros: \n"))
cm = altura*100
print(f"O valor da altura de {altura:.2f} metros é de {cm} centimetros")