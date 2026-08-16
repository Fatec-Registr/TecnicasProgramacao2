#11. Um cliente de um supermercado, comprou um determinado produto. Leia a descrição do produto (nome), a quantidade comprada e o preço unitário. Calcular e escrever o total a pagar e a descrição do produto.
produto = input("Descreva o nome do produto: ")
qtd = int(input(f"Informe a quantidade comprado do(a) {produto}."))
preco = int(input(f"Informe preço do(a) {produto}."))
total = qtd*preco
print(f"{produto}:\nPreço Unitario: {preco:.2f} reais\nQuantidade: {qtd}.\nValor Total: {total:.2f} reais")