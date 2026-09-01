'''
Observe a fórmula:  U=R * i, onde, 
U é a Tensão (em V), 
R é a Resistência (em Ώ) 
i  é a Corrente (em A). 
Construa um programa que apresente o seguinte menu e realize os 
cálculos: 
Por exemplo se a pessoa escolher a opção 2 , vai pedir para o usuário 
digitar o valor da Tensão(U) e a corrente(i) e calcular a Resistência(R)
**************** CÁLCULO DE GRANDEZAS ELÉTRICAS **********
1.Tensão (em Volt)                      -------------- U = R * i
2. Resistência (em Ohm)                 -------------- R = U /i
3. Corrente (em Ampére)                 -------------- i= U / R
******************* ************************************************
'''
op = int(input("Escolha o que esta tentando procurar:\n1.Tensão (em Volt)\n2. Resistência (em Ohm)\n3. Corrente (em Ampére)\n"))

match op:
    case 1:
        r = float(input("Informe o valor da resistencia (em Ohm):\n"))
        i = float(input("Informe o valor da corrente (em Ampére):\n"))
        u = r*i
        print(f"A tensao com a corrente {i:.2f} e resistencia {r:.2f} sera: {u:.2f} Volts")
    case 2:
        u = float(input("Informe o valor da tensao (em Volts):\n"))
        i = float(input("Informe o valor da corrente (em Ampére):\n"))
        r = u/i
        print(f"A resistencia com a corrente {i:.2f} e tensao {u:.2f} sera: {r:.2f} Ohm")
    case 3:
        r = float(input("Informe o valor da resistencia (em Ohm):\n"))
        u = float(input("Informe o valor da tensao (em Volts):\n"))
        i = u/r
        print(f"A a corrente  com a tensao {u:.2f} e resistencia {r:.2f} sera: {i:.2f} Amperes")
    case _:
        print("Opcao invalida")

