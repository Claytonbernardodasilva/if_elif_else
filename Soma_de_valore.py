while True:
    valores = []
    sair_do_programa = False
    i = 1  # Iniciamos um contador manual

    # Coleta dos 5 valores usando while
    while i <= 5:
        entrada = input(f"Digite o {i}° valor (ou 'sair' para encerrar): ")
        
        if entrada.lower() == 'sair':
            sair_do_programa = True
            break
            
        try:
            valor = float(entrada)  # Ou int() se preferir inteiros
            valores.append(valor)
            i += 1  # Só avançamos quando o valor for válido
        except ValueError:
            print("Valor inválido! Digite um número ou 'sair'.")
            # Não incrementamos i, então repete a mesma posição

    # Sai do programa se solicitado
    if sair_do_programa:
        print("Programa encerrado.")
        break
    
    # Calcula e mostra a soma
    soma = sum(valores)
    print("A soma dos valores é:", soma)
    print("-" * 30)

    