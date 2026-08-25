# A função split le varios valores de um vetor 
# só devemos digitar os valores com espaço

num =  input("Digite os numeros deixando espaço entre eles: ")
vetor =[int(i) for i in num.split()]

print("Valores armazenados: ", vetor)