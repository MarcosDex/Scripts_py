#Faça um Programa que converta metros para centímetros.
metro = int(input('Digite quantos metros precisa converter:'))
cm = metro*100

if cm < 0:
    print('Não existem centimetros negativos')

elif cm >= 0:
    print(cm,'Centimetros')