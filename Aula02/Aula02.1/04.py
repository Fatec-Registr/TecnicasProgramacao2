"""
Na última Black Friday, o gerente de uma loja de perfumes colocou todo o seu estoque em promoção, de acordo com a tabela a seguir:

| Código | Condição de Pagamento          | Desconto (%) |
| -----: | ------------------------------ | -----------: |
|      1 | À vista (em espécie)           |          15% |
|      2 | Cartão de débito               |          10% |
|      3 | Cartão de crédito (vencimento) |           5% |

Construa um programa que solicite ao operador do caixa o preço total da compra, e escolha no menu a forma de pagamento. Ao fim, o programa deve informar o valor da compra e valor final a ser pago com desconto.
"""
preco = float(input("Informe o valor da compra:\n"))
op=int(input("Escolha uma das opçoes abaixo:\n1-À vista (em espécie)\n2-Cartão de débito\n3-Cartão de crédito."))
match op:
    case 1:
        desc = 0.15
        opcao="À vista"
    case 2:
        desc = 0.1
        opcao="Cartão de débito"
    case 3:
        desc = 0.05
        opcao="Cartão de crédito"
    case _:
        print("Opção invalida")

valorFinal=preco -(desc*preco)
print(f"O valor Inicial foi de {preco:.2f} reais\nOpcao de pagamento: {opcao}\nValor com Desconto: {valorFinal:.2f} reais")
    