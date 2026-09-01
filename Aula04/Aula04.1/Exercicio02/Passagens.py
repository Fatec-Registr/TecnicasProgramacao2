# Passagem

# -nomePassageiro : String
# - telefone: String
# - RG: String
# - localViagem: String
# - data: String
# - horário: String
# - numpoltrona: String
class Passagem:
    def __init__(self):
        self.__telefone =""
        self.__nomePassageiro = ""
        self.__rg = ""
        self.__localViagem = ""
        self.__data = ""
        self.__horario = ""
        self.__numPoltrona = ""

    @property
    def _nomePassageiro(self):
        return self.__nomePassageiro

    @_nomePassageiro.setter
    def _nomePassageiro(self, value):
        self.__nomePassageiro = value

    @property
    def _rg(self):
        return self.__rg

    @_rg.setter
    def _rg(self, value):
        self.__rg = value

    @property
    def _localViagem(self):
        return self.__localViagem

    @_localViagem.setter
    def _localViagem(self, value):
        self.__localViagem = value

    @property
    def _data(self):
        return self.__data

    @_data.setter
    def _data(self, value):
        self.__data = value

    @property
    def _horario(self):
        return self.__horario

    @_horario.setter
    def _horario(self, value):
        self.__horario = value

    @property
    def _numPoltrona(self):
        return self.__numPoltrona

    @_numPoltrona.setter
    def _numPoltrona(self, value):
        self.__numPoltrona = value




# + cadastrarDadosPassageiros(): void
    def cadastrarDadosPassageiros(self):
        print("Cadastro de Passageiro:")
        self.__telefone = input("Insira o telefone do Passageiro: ")
        self.__nomePassageiro = input("Insira o Nome do Passageiro: ")
        self.__rg = input("Insira o RG do passageiro: ")
        print("Cadastro do Passageiro feito com sucesso")
# + cadastrarDadosPassagem():void
    def cadastrarDadosPassagem(self):
        print("Cadastro da Passagem:")
        self.__localViagem = input("Insira o local da Viagem : ")
        self.__data = input("Insira a data da Viagem : ")
        self.__horario = input("Insira o horario da Viagem : ")
        self.__numPoltrona = input("Insira o numero da poltrona : ")
        print("Cadastro da Passagem feito com sucesso")
    
# + mostrarDadosPassageiro():void
    def mostrarDadosPassageiros(self):
        print(f"Dados do Passageiro:\nTelefone: {self.__telefone}.\nNome: {self.__nomePassageiro}.\nRG:{self.__rg}.\n")   
# + mostrarDadosPassagem():void
    def mostrarDadosPassagem(self):
        print(f"Dados da Passagem:\nLocal da viagem:  {self.__localViagem}.\nData da Viagem: {self.__data}.\nHorario da Viagem: {self.__horario}.\nNumero da poltrona: {self.__numPoltrona}.\n")

