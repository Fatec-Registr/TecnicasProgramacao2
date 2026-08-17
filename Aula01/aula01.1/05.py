"""
Escrever um algoritmo para ler o custo de fabricação de uma pick-up, o custo de um caminhonete nova, é a soma do custo de fábrica, com a porcentagem do distribuidor e a porcentagem de outros impostos.

Supondo que o percentual do distribuidor seja de 38% e os outros impostos de 47% em cima do custo de fabricação.

Calcular e escrever o custo final da pick-up para o cliente.

Mostre o valor do imposto do distribuidor, o valor dos outros impostos, e o custo final da pick-up para o cliente.
"""

custo = float(input("Forneça o valor do custo de fabrica:\n"))
distribuicao = 0.38*custo
imposto = 0.47*custo
final = custo + distribuicao + imposto
print(f"Preço final: {final:.2f} reais\nPreço final = custo ({custo:.2f} reais) + distribuição({distribuicao:.2f}) reais + imposto ({imposto:.2f} reais)")