tamanho = float(input('Quantos metros quadrados devem ser pintados: '))

litros = tamanho / 3.0
latas = int(litros / 18.0)

if tamanho <= 0:
    print('Não precisa comprar latas')

else:
    litros % 18 != 0
    latas += 1
    print('Voce deverá comprar', latas, 'latas.')
    print('O valor total é:', latas * 80)




