#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#a. o produto do dobro do primeiro com metade do segundo.
#b. a soma do triplo do primeiro com o terceiro.
#c. o terceiro elevado ao cubo.
int1 = input("Digite o primeiro inteiro: ")
int2 = input("Digite o segundo inteiro: ")
real = input("Digite um numer real: ")

produto = (int(int1) * 2) * (int(int2) / 2)

soma = (int(int1) * 3) + float(real)

potencia = float(real)**3

print('Produto do dobro do primeiro com metade do segundo:',produto)
print('Soma do triplo do primeiro com o terceiro:',soma)
print('Numero real elevado ao cubo:',potencia)