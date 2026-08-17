#UM FUNCIONÁRIO DE UMA LOJA DE COMPONENTES ELETRÔNICOS , PAGA A SEU VENDEDOR UM FIXO DE R$1500 POR MÊS, MAIS UM BÔNUS DE R$150 POR ITEM VENDIDO. FAÇA UM ALGORITMO QUE LEIA A QUANTIDADE DE ITENS VENDIDOS E CALCULE O SALÁRIO TOTAL DO FUNCIONÁRIO. MOSTRE A QUANTIDADE DE ITENS VENDIDOS E O SALÁRIO TOTAL DO FUNCIONÁRIO.
salarioFixo = 1500
bonus = 150
qtd = int(input("Informe a quantidade de itens vendidos:\n"))

salarioTotal = salarioFixo + qtd*bonus

print(f"O salario total do funcionario com o bonus seria {salarioTotal:.2f} reais.")