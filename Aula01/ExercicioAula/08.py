#8. Leia três números , faça a soma dos números, calcule a potência do valor da soma, elevado ao quadrado. Mostre o valor da soma e da potência. pow(soma,2)

n1= float(input("Digite o valor para o primeiro numero:\n"))
n2= float(input("Digite o valor para o segundo numero:\n"))
n3= float(input("Digite o valor para o terceiro numero:\n"))

soma= n1+n2+n3
potencia = pow(soma,2)

print(f"{n1}+{n2}+{n3}= {soma}\n({n1}+{n2}+{n3})²= {potencia}")