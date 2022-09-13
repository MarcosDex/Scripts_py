nota = int(input("insira uma nota"))
while (nota < 0) or (nota > 10 ):
    nota = int(input("não pode ser menor que 0 ou maior que 10 man /n / tente novamente:"))
    print("nota vlaida")