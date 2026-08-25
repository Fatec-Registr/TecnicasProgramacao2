'''
Faça um algoritmo  que, leia a categoria e salário de um Funcionário .
A empresa irá dar um aumento de salário aos seus funcionários de acordo com a categoria de cada empregado.
O aumento seguirá a seguinte regra:
Funcionários das categorias A  ganharão 10% de aumento sobre o salário
Funcionários das categorias B ganharão 15% de aumento sobre o salário
Funcionários das categorias C  ganharão 25% de aumento sobre o salário
Mostre o salário atual e salário com aumento
'''
cat = input("Informar a categoria do funcionario (A, B ou C)")
salario = float(input("Informe o salario do funcionario:"))

match cat.lower():
    case "a":
        desc = 0.1
        aumento = "10%"
        categoria = "A"
    case "b":
        desc = 0.15
        aumento = "15%"
        categoria = "B"
    case "c":
        desc = 0.25
        aumento = "25%" 
        categoria = "C"
    case _:
        desc = 0.0
        aumento = "null"
        categoria ="null"
        print(f"Categoria {cat} não cadastrado.")

salarioFinal = salario + salario*desc
print(f"Sendo:\nCategoria:{cat}\nSalario Inicial: {salario:.2f} reais\nPorcentagem de aumento: {aumento}\nSalario Final: {salarioFinal:.2f} ")

    