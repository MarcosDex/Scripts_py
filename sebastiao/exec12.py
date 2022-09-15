sexo = input('Escolha: M - Masculino / F - Feminino: ')
h = float(input('Altura:'))
m = 72.7 * h - 58
f = 62.1 * h - 44.7

if h < 0:
    print('Altura negativa????')

elif sexo == "m" or sexo == "M":
    print('Peso ideal do homem',m)

elif sexo == "f" or sexo == "F":
    print('Peso ideal da mulher',f)


