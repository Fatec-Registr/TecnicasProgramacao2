'''
Construa um programa que receba um número inteiro positivo informado pelo usuário. Caso ele seja par, o programa deve calcular o seu quadrado.
Mas, se ele for ímpar, deve ser calculado o seu cubo. Ao fim, o programa deve mostrar o valor calculado e dizer se o número é impar ou par.
Se o resto da divisão for zero, significa que o número é par if num % 2 == 0
'''
n = int(input("Informe um numero positivo"))
if n < 0 :
    print(f"Numero digitado negativo.")
elif n%2 == 0:
    valor = pow(n,2)
    resp = "par e quadrado sera, "
else:
    valor = pow(n,3)
    resp = "impar e o seu cubo sera, "
print(f"O numero {n} é {resp} {valor}")
    
