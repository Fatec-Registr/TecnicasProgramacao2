'''
Construa um programa que solicite ao usuário dois números positivos.
Em seguida, o programa deve apresentar o seguinte menu.

1.  Média ponderada, com pesos 2 e 3, respectivamente
2. Quadrado da soma dos 2 números 
3. Cubo do menor número 
Escolha uma opção:

De acordo com a opção informada, o programa deve calcular a operação apresentada no menu. Se a opção escolhida for inválida, o programa deve mostrar a mensagem “Opção inválida” e ser encerrado. 
Calculo media ponderada: media =(num1 * 2 + num2 * 3) /5

'''
n1= float(input("Informe o valor do primeiro numero:\n"))
n2= float(input("Informe o valor do segundo numero:\n"))

print("Escolha uma das opçoes:\n1.  Média ponderada, com pesos 2 e 3, respectivamente \n2. Quadrado da soma dos 2 números \n3. Cubo do menor número\n")
opcao = int(input("Escolha uma opção (1,2 ou 3):"))
if opcao == 1 :
    resultado= (n1*2+n2*3)/5
elif opcao == 2:
    resultado = pow((n1+n2),2)
elif opcao == 3:
    if n1>n2:
        resultado = pow(n2,3)
    else:
        resultado = pow(n1,3)
else:
    print("Valor invalido\n")
    opcao = "invalida"
    resultado= "Error"
print(f"Sendo o primeiro numero {n1}e {n2} o segundo e a esolha for o {opcao}, temos: \nREsultado: {resultado}")

