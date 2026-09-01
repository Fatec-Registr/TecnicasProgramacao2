# 7) Digite 7 nomes e armazene esses valores em uma lista e 
# mostre os nomes que foram armazenados , e sua posição na lista.
# (UTILIZE FOR)

# Digite o 1º nome: luiz
# Digite o 2º nome: claudio

# Nomes Digitados:
# O 1º nome armazenado é luiz
# O 2º nome armazenado é claudio
nomes = []
i= 0
for i in range (1,8):
    nome = input(f"Digite o {i}º nome: ")
    nomes.append(nome)
print(f"Nomes digitados:")
for i in range (1,8):
    print(f"O {i}º nome armazenado é: {nomes[i-1]}")
    

# i = 0
# for i in nomes:
#     i +=1
#     print(f" O {i}º nome armazenado é {nome[i]} ")