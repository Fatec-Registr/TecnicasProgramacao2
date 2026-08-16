#5. Leia dois números , efetuar os cálculos com as operações de adição, subtração, multiplicação e divisão de um número pelo outro.
n1 = float(input("Informe o valor do primeiro numero:\n"))
n2 = float(input("Informe o valor do segundo numero:\n"))

soma= n1+n2
subtracao= n1-n2
multiplicacao= n1*n2
divisao = n1/n2

print(f"{n1}+{n2}={soma:.2f}\n{n1}-{n2}={subtracao:.2f}\n{n1}*{n2}={multiplicacao:.2f}\n{n1}/{n2}={divisao:.2f}\n")