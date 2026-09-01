# Criando a Classe en Python
class Pessoa:
    # construtor = iniciar os atributos com valores
    def __init__(self,nome,nasc):
        #definição de atributos público
        self.nome = nome
        self.nasc = nasc

    #Criação do metodo de calcular idade
    def calcularIdade(self):
        ano = int(input("Digite o ano atual: "))
        return ano - self.nasc

# Instanciar o objeto da classe pessoa
p1 = Pessoa('ricardo',1989)
#chamar o metodo calcular idade
print(p1.calcularIdade()) 