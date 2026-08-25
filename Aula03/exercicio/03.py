# 3) Leia a tabuada e faça a sequência utilizando whilede 1 a 10 
# mostrando os resultados da tabuada:
# Tabuada de:4
# 4 x 1 = 4
# 4 x 2 = 8
# 4 x 3 = 12
# 4 x 4 = 16
# 4 x 5 = 20
# 4 x 6 = 24
# 4 x 7 = 28
# 4 x 8 = 32
# 4 x 9 = 36
# 4 x 10 = 40
i = 1
num = int(input("Digite um numero qual sera feito a tabuada do 1 ao 10 desse numero:"))
while i <= 10 :
    res = num*i
    i +=1
    print(f"{num} X {i-1} = {res}")