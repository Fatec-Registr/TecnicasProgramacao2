#For para percorrer ua lista e verificar a quantidade de caracteres
nomes =["Felipe", "Maria", "Luiza", "Paulo","Josefina"]
for i in nomes:
    if len(i) != 4:
     continue
    print(f"Esse nome tem 4 letras {i}")

    if i == "Paulo":
     break
print("Terminou a execucao, tchau")