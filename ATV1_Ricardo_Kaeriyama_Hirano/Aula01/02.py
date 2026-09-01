'''
2. Um veiculo se desloca, em uma determinada velocidade, receba do usuário a variação do deslocamento do veículo (em metros) e a variação do tempo percorrido (em segundo). Ao fim, o programa deve calcular a velocidade média, em m/s. (vm= d /t)
'''

d = float(input("Informe a distancia em metros a qual o veiculo deslocou:\n"))
t = float(input(f"Informe o tempo em segundos ao qual ocorreu o deslocamento:\n"))
vm= d/t
print(f"Sabendo que a distancia percorrida é {d:.2f} metros e o tempo disso ocorrer foi {t:.2f} segundos, temos que a suam velociade media é de {vm:.2f} m/s. ")