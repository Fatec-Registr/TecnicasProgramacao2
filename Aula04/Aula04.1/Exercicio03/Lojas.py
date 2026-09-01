# Loja

# - razaoSocial: String
# - cpfCliente: String
# - valorCompra: double;
# - qtdItensComp: int;
# - valorTotalCompra: double;
class loja:
    def __init__(self):
        self.__razaoSocial=""
        self.__cpfCliente=""
        self.__valorCompra= 0
        self.__qtdItensComp= 0
        self.__valorTotalCompra= 0

    @property
    def _razaoSocial(self):
        return self.__razaoSocial

    @_razaoSocial.setter
    def _razaoSocial(self, value):
        self.__razaoSocial = value

    @property
    def _cpfCliente(self):
        return self.__cpfCliente

    @_cpfCliente.setter
    def _cpfCliente(self, value):
        self.__cpfCliente = value

    @property
    def _valorCompra(self):
        return self.__valorCompra

    @_valorCompra.setter
    def _valorCompra(self, value):
        self.__valorCompra = value

    @property
    def _qtdItensComp(self):
        return self.__qtdItensComp

    @_qtdItensComp.setter
    def _qtdItensComp(self, value):
        self.__qtdItensComp = value

    @property
    def _valorTotalCompra(self):
        return self.__valorTotalCompra

    @_valorTotalCompra.setter
    def _valorTotalCompra(self, value):
        self.__valorTotalCompra = value

       
# +inserirDadosLoja() : void
    def inserirDadosLoja(self) :
        print("Cadastro da Loja:")
        self.__razaoSocial= input("Insira a razao social:")
        self.__cpfCliente= input("Insira o CPF do cliente:")
        self.__valorCompra= float(input("Insira o valor da compra:"))
        self.__qtdItensComp= int(input("Insira a quantidade comprada:"))
    
# +mostrarDadosLoja(): String
# +calcularCompraLoja():double


# Principal

# if __name__ == "__main__":