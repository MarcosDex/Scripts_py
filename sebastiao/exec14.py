peso = int(input("Entre com o peso: "))
excesso = peso - 50
multa = excesso * 4
if peso > 50:
    print('A mercadoria excedente foi de:',excesso,'Kg')
    print('O preço da multa foi de R$',multa,'Reais')
    print('O excesso de peso foi de ',excesso,'kg, portanto, a multa é de R$',multa,'Reais')
else:
    print('Valor abaixo de R$50 reais não é multado')