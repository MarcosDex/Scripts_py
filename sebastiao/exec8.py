salariohora = int(input("Digite o quanto voce ganha por hora: "))
horasmensais = int(input("Digite a quantidade de horas que voce trabalha por mes: "))

salario = float(salariohora) * float(horasmensais)

if salario < 0 or horasmensais < 0:
    print('As coisas estão ruins meu nobre, mas salario negativo e/ou horario negativo(s) da uma pegada')
else:
    print('Voce ganha R$',salario, 'por mes')