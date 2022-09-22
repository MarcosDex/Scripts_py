#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9).
farenheit = input("Digite a temperatura em Farenheit: ")

celsius = (5 * (float(farenheit) - 32) / 9)

print("%.2f graus celsius" % celsius)