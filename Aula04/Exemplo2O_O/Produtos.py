#define nome da classe
class Produto:
    #define o construtor da classse inicializando os atributos
    def __init__(self):
        #atributos private dois underline __define como atributo
        self.__nome = ""
        self.__valor = 0
        self.__quantidade = 0
    #Encapsulamento dos atributos 
    #instale a extencao Python Getter Setter
    # CRTL + SHIFT + P => Digite gene
    @property
    def _nome(self):
        return self.__nome

    @_nome.setter
    def _nome(self, value):
        self.__nome = value

    @property
    def _valor(self):
        return self.__valor

    @_valor.setter
    def _valor(self, value):
        self.__valor = value

    @property
    def _quantidade(self):
        return self.__quantidade

    @_quantidade.setter
    def _quantidade(self, value):
        self.__quantidade = value
    # metodo cadastrar Produto
    def cadastrarProduto(self):
        print(f"Cadastro de produto:")
        self.__nome = input("Digite o nome do produto:  ")
        self.__quantidade = int(input("Insira a quantidade do produto: "))
        self.__valor = float(input("Informe o valor do produto: "))
        print("Produto Cadastrado com Sucesso")

    # metodo mostrar produto
    def mostrarProduto(self):
        print("Dados do produtos:")
        print(f"Nome do produto: {self.__nome}")
        print(f"Quantidade: {self.__quantidade}")
        print(f"Valor: {self.__valor}")

    #metodo com retorno calcular total
    def calcularVlrTotal(self):
        return self._quantidade*self.__valor
