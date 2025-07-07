while True:
    print ("\n--- Calculadora de IMC ---")
    print("Digite 'sair' a qualquer momento para encerrar")

    Peso = float (input("Digite seu peso em kg: "))
    Altura = float (input("Digite sua Altura em metros: "))

    imc = Peso / (Altura ** 2)

    if imc < 18.5:
        print ("Abaixo do Peso")
    elif 18.5 <= imc < 25:
        print ("Peso Ideal")
    elif 25 <= imc < 30:
        print ("Sobrepeso")
    elif 30 <= imc < 35:
        print("Obesidade Grau 1")
    elif 35 <= imc < 40:
        print("Obesidade Grau 2")
    else:
        print ("Obsedidade Grau 3 (Mórbida0)")
