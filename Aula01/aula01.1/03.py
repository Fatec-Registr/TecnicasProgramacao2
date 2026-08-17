'''
Faça um programa que leia uma temperatura em graus Celsius e converta-a para graus Fahrenheit. A fórmula de conversão é:
F = C * 1.8 + 32
Sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.
'''

c = float(input("Informe o valor da temperatuta em graus Celsius: "))
f = c *1.8 + 32
print(f"Sendo a temperatura {c}°C sua temperatura em Fahrenheit seria {f:.2f}°F")

