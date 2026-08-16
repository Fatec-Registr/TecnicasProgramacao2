#12. Calcule quantos azulejos são necessários para azulejar uma parede. É necessário conhecer a altura da parede , a sua largura , e a altura do azulejo e sua largura . Leia os dados em seguida calcule a área da parede , e do azulejo , em seguida calcule a quantidade de azulejos necessários.
altura = float(input("Informe a altura da parede em centimetros:\n"))
largura = float(input("Informe a largura da parede em centimetros:\n"))
alturaAzulejo = float(input("Informe a altura do azulejo em centimetros:\n"))
larguraAzulejo = float(input("Informe a largura do azulejo em centimetros:\n"))

areaParede = altura*largura
areaAzulejo = alturaAzulejo*larguraAzulejo
qtd = areaParede/areaAzulejo

print(f"Area da parede: {areaParede}cm²\nArea da azulejo: {areaAzulejo}cm²\nQuantidade de azulejo: {qtd:.1f}.")