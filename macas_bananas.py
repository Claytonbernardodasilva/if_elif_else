vendas_macas = int(input("quantidade vendida de maçãs: "))
vendas_bananas = int(input("quantidade vendidade de banadas: "))

if vendas_macas > vendas_bananas:
    print("As maças tiveram maior venda!")
elif vendas_bananas > vendas_macas:
    print("As bananas tiveram maior venda!")
else:
    print("Houve empate entre maças e bananas!")
    