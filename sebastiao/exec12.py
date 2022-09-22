#Tendo como dados de entrada a altura de uma pessoa, construa um programa que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
#Nota de marcos = 'Professor, eu fiz a 12 e a 13 juntas pra poupar tempo que o enunciado de uma é o mesmo da outra' entre algumas aspas
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


