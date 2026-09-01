#Define o arquivo Produtos importando a classe Produto
from Produtos import Produto

class Principal:
    @staticmethod # utiliza-se isso quando a classe Principal tera um metodo estatico chamado main
    def main():
        #instanciar o objeto da clsse Produto
        prod = Produto()
        prod.cadastrarProduto()
        prod.mostrarProduto()
        print(f"O valor total a pagar é R$ {prod.calcularVlrTotal():.2f}")

#Inicializamos o metodo main da classe Principal
if __name__=="__main__":
    Principal.main()

