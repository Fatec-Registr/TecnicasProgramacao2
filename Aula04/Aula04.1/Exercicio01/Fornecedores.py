# Fornecedores

# - nomeFornecedor: String
# - nomeProduto: String
# - descricaoProduto: String

# + cadastrarFornecedor(): void
# + listarFornecedor(): void


# Principal

# if __name__ == "__main__":

class Fornecedor:
    def __init__(self):
        self.__nomeFornecedor =""
        self.__nomeProduto =""
        self.__descricaoProduto =""

    @property
    def _nomeFornecedor(self):
        return self.__nomeFornecedor

    @_nomeFornecedor.setter
    def _nomeFornecedor(self, value):
        self.__nomeFornecedor = value

    @property
    def _nomeProduto(self):
        return self.__nomeProduto

    @_nomeProduto.setter
    def _nomeProduto(self, value):
        self.__nomeProduto = value

    @property
    def _descricaoProduto(self):
        return self.__descricaoProduto

    @_descricaoProduto.setter
    def _descricaoProduto(self, value):
        self.__descricaoProduto = value

# + cadastrarFornecedor(): void
# + listarFornecedor(): void
    def cadastrarFornecedor(self):
        print("Cadastro de Fornecedor:")
        self.__nomeFornecedor = input("Informe o nome do fornecedor: ")
        self.__nomeProduto = input("Informe o nome do produto: ")
        self.__descricaoProduto = input("Informe uma descricao do produto: ")
        print("Cadastro do fornecedor feito com sucesso")
    def listarFornecedor(self):
        print(f"Fornecedores: \nNome: {self.__nomeFornecedor}.\nNome do produto: {self.__nomeProduto}.\nDescrição do Produto: {self.__descricaoProduto}.\n")
    