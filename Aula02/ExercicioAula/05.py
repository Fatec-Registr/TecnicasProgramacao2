'''
Leia a altura de 3 pessoas. Ao fim, o programa deve mostrar as estaturas em ordem decrescente. Mostrar a pessoa de maior altura , altura mediana , e menor altura
'''
altura1 = float(input("Digite a altura da primeira pessoa:\n"))
altura2 = float(input("Digite a altura da segunda pessoa:\n"))
altura3 = float(input("Digite a altura da terceira pessoa:\n"))

if altura1 > altura2 and altura1 > altura3:
    maior = altura1
    if altura2 > altura3 :
        medio = altura2
        menor = altura3
    elif altura3 > altura2:
        medio = altura3
        menor = altura2
    else:
        medio = menor = altura2
elif altura2 > altura1 and altura2 > altura3:
    maior = altura2
    if altura1 > altura3 :
        medio = altura1
        menor = altura3
    elif altura3 > altura1:
        medio = altura3
        menor = altura1
    else:
        medio = menor = altura1
elif altura3 > altura1 and altura3 > altura2:
    maior = altura3
    if altura1 > altura2 :
        medio = altura1
        menor = altura2
    elif altura2 > altura1:
        medio = altura2
        menor = altura1
    else:
        medio = menor = altura1
else:
    maior=medio=menor=altura1
    
print(f"{maior:.2f},{medio:.2f},{menor:.2f}")