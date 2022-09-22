#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
salariohora = int(input("Digite o quanto voce ganha por hora: "))
horasmensais = int(input("Digite a quantidade de horas que voce trabalha por mes: "))

salario = float(salariohora) * float(horasmensais)

if salario < 0 or horasmensais < 0:
    print('As coisas estão ruins meu nobre, mas salario negativo e/ou horario negativo(s) da uma pegada')
else:
    print('Voce ganha R$',salario, 'por mes')