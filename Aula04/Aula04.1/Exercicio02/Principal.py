from Passagens import Passagem

class Principal:
    @staticmethod
    def main():
        p = Passagem()
        p.cadastrarDadosPassageiros()
        p.cadastrarDadosPassagem()
        p.mostrarDadosPassageiros()
        p.mostrarDadosPassagem()

if __name__=="__main__":
    Principal.main()