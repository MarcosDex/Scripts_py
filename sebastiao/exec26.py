preco1 = float(input("Digite o preço do primeiro produto: "))
preco2 = float(input("Digite o preço do segundo produto: "))
preco3 = float(input("Digite o preço do terceiro produto: "))

if preco1 < preco2:
    if preco1 < preco3:
        print("Você deve comprar o primeiro produto!")
    else:
        print("Você deve comprar o terceiro produto!")
else:
    if preco2 < preco3:
        print("Vocè deve comprar o segundo produto!")
    else:
        print("Você deve comprar o terceiro produto!")
