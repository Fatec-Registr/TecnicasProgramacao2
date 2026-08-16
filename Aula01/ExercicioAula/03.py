#3. Calcular a área da circunferência de um poço da aguá, cujo formato é circular. Para isso, o usuário deve informar o valor do raio. (área = 3.14 * r²)

from math import pi

raio = float(input("Informe o raio da circuferencia em centimetros: \n"))
area =  pi*(pow(raio,2))
print(f"Sabendo que o raio da cicuferencia é {raio:.2f} cm. Sua area sera de {area:.2f} cm²")
2
