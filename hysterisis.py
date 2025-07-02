while True:
    print("\n--- calculadora de tração---")
    print("Digite 'sair' a qualquer momento para encerrar")

    Tracao_cinta = float(input("Digite a tração da cinta: "))
    Alongamento_da_cinta = float(input("Digite o alongamento da cinta: "))

    Hysteresys = Tracao_cinta / Alongamento_da_cinta

    if Hysteresys < 18.5:
        print("Hysterisys boa")
    elif 18.5 <= Hysteresys < 25:
        print ("Hysterisys média")
    elif 25 <= Hysteresys < 35:
        print("Hysterisys ruim")
    else:
        print("sem correlação")
