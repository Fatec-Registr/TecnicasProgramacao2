#4. Sabendo que área = (base*altura)/2, construa um programa para calcular a área de triângulo retângulo
base = float(input("Informe em centimetro a base do triangulo:\n"))
altura = float(input("Informe em centimetro a altura do triangulo:\n"))
area = base*altura/2
print(f"Sabedo que a base do triangulo é {base:.2f} cm e a altura é {altura:.2f}, temos que sua area sera {area:.2f} cm².")