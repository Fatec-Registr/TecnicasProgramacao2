'''
A Secretaria de Meio Ambiente, que controla o índice de poluição, mantém três grupos de indústrias que são altamente poluentes do meio ambiente.
A tabela a seguir indica a ação a ser tomada pela Secretaria de acordo com o índice de poluição , leia o índice de poluição:
Ação                    Índice de Poluição
Considerar Aceitável    0  até 2

Suspender Atividades    3  até  5
Grupo1

Suspender Atividades    6  até 7
Grupo  2

Suspender atividade     Acima de 8
de todos grupos
'''
nivelPoluicao = int(input("Escreva o nivel de poluição:\n"))
match nivelPoluicao:
    case 0|1|2:
        print("Considerar Aceitável")
    case 3|4|5:
        print("Suspender Atividades Grupo 1")
    case 6|7:
        print("Suspender Atividades Grupo 2")
    case _:
        print("Suspender Atividades de todos grupos")
    