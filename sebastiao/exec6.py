#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
import math

raio = int(input('Digite o raio:'))
area = math.pi*raio**2
area314 = 3.14*raio**2

if raio < 0:
    print('Não existem raios negativos')
else:
    print('A area da circunferencia é de:',area)
    print('A area da circunferencia é de:',area314)

