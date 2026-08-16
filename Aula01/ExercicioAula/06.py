#6. Escreva um algoritmo para ler o salário mensal atual de um servidor público e a porcentagem de aumento do seu salário. Calcular e escrever o valor do novo salário. ns= (salario * porc)/100 + salario
salarioAtual=float(input("Informe o salario mensal atual do servidor:\n"))
aumentoPercentual=float(input("Informe o percentual de aumento do servidor:\n"))

ns = (salarioAtual * aumentoPercentual)/100 + salarioAtual

print(f"Tendo o salario atual de {salarioAtual:.2f} reais e aumento percentual de {aumentoPercentual:.2f}% o seu novo salario sera de {ns:.2f} reais")