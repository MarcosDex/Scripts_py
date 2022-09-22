#Faça um Programa que leia três números e mostre-os em ordem decrescente.
#Fiz um plus e coloquei-os em ordem crescente também.
number1 = float(input('Digite um numero:'))
number2 = float(input('Digite mais um numero:'))
number3 = float(input('Digite o ultimo numero:'))

if number1 < number3:
    number1, number3 = number3, number1
elif number1 < number2:
    number1, number2 = number2, number1
elif number2 < number3:
    number2, number3 = number3, number2
print(f'A ordem descrescente é: {number1},{number2} e {number3}')

if number1 > number3:
    number1, number3 = number3, number1
elif number1 > number2:
    number1, number2 = number2, number1
elif number2 > number3:
    number2, number3 = number3, number2
print(f'A ordem crescente é: {number1}, {number2} e {number3}')