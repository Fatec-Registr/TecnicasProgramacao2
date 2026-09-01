#9. Uma cidade está realizando uma eleição municipal. Leia o número de votos brancos, nulos e válidos. Faça a soma do número total de eleitores. Calcular e escrever o percentual que cada um representa, em relação ao total de eleitores. percbrancos<-(votosbrancos* 100) / totaleleitores

branco = float(input("Informe o numero de votos em branco:\n"))
nulos = float(input("Informe o numero de votos nulos:\n"))
validos = float(input("Informe o numero de votos em validos:\n"))

total =  branco + nulos + validos

percBranco = (branco/total)*100
percNulos = (nulos/total)*100
percValidos = (validos/total)*100

print(f"O valores percentuais de votos sao:\nBranco: {percBranco:.2f}%\nNulos: {percNulos:.2f}%\nValidos: {percValidos:.2f}%")
