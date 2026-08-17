'''
Leia dois números e calcule a divisão do maior número pelo menor número . Verifique se os números são iguais, mostre mensagem avisando que os números são iguais
'''
n1 = float(input("Informe o valor de um numero:\n"))
n2 = float(input("Informe o valor de outro numero:\n"))
if n1==n2 :
    print("Os numeros escolhidos sao iguais")
else:
    if n1>n2 and n2 != 0:
        maior = n1
        menor = n2
        divisao=n1/n2
    elif n2>n1 and n1 != 0:
        maior = n2
        menor = n1
        divisao=n2/n1
    else :
        divisao = 0 
        
    print(f"O valor de primeiro numero é {n1} e  o segundo numero {n2} a divisao entre o maior numero com o menor  é {divisao}. ")