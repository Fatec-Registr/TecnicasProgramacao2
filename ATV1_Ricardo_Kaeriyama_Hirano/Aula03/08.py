# 8) Leia 10 números e verifique e se são números pares ou ímpares 
# , e mostre os números pares e os números ímpares
# (UTILIZE FOR E IF)
# Digite o 7º número: 54
# Digite o 8º número: 63
# Digite o 9º número: 12
# Digite o 10º número: 10
# O número 23 é impar:
# O número 53 é impar
# O número 65 é impar
# O número 44 é par
# O número 42 é par
# O número 23 é impar
# O número 54 é par
# O número 63 é impar
# O número 12 é par
# O número 10 é par
numeros =[]
for i in range(1,11):
    numero = int(input(f"Digite o {i}º número: "))
    numeros.append(numero)
print("\n")
for num in numeros:
    if num%2==0:
        resultado = "par"
    else:
        resultado = "impar"

    print(f"O numero {num} é {resultado}")



