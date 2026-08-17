'''
CRIE UM ALGORITMO, PARA CALCULAR O VALOR DE UM MÓVEL COMPRADO, NAS LOJAS LUIZ BAHIA , PARA EFETUAR O CALCULO DO VALOR DE UMA PARCELA EM ATRASO. LEIA O VALOR DA PARCELA E A TAXA DE JUROS IMPOSTA PELA LOJA, E LEIA A QUANTIDADE DE MESES EM ATRASO. (TEMPO)

VALORATRASO = VALORP + (VALORP * (TAXA/100) * TEMPO)

MOSTRE O VALOR DO MÓVEL A SER PAGO COM ATRASO, MOSTRE O VALOR DA TAXA DE JUROS , O VALOR DE CADA PARCELA E A TAXA DE JUROS
'''
valorp = float(input("Informe o valor da parcela a ser paga:\n"))
taxa = float(input("Informe o valor da taxa de juros:\n"))
tempo= float(input("Informe a quantidade de meses em atraso:\n"))

valorAtraso = valorp + (valorp*(taxa/100)*tempo)

print(f"Valor Total Com Juros: {valorAtraso:.2f}\nTaxa de juros: {taxa:.2f}%\nTempo de atraso: {tempo} meses.\nValor da parcela: {valorp:.2f} reais")