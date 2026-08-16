#10. Calcular e apresentar o valor do volume de uma lata de tinta, no formato de um cilindro .Utilize a fórmula: VOLUME = pi * raio² * ALTURA

from math import pi
altura = float(input("Informe a altura em centimetro da lata de tinta:\n"))
raio = float(input("Informe o raio em centimetro da lata de tinta:\n"))

volume = pi*altura*pow(raio,2)
print(f"Send o a altura da lata de tinta {altura:.2f} cm e seua raio de {raio:.2f} cm temos que seu volume sera de {volume:.2f}cm³.")