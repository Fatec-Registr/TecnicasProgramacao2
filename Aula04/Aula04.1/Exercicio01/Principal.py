from Fornecedores import Fornecedor

class Principal:
    @staticmethod
    def main():
        f = Fornecedor()
        f.cadastrarFornecedor()
        f.listarFornecedor()

if __name__=="__main__":
    Principal.main()
