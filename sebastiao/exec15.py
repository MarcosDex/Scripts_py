qnt_ganha = float(input('Quanto ganha por hora? '))
horas_trabalhadas = int(input('Horas trabalhadas por mês: '))

salario_bruto = qnt_ganha * horas_trabalhadas
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05

if qnt_ganha < 0:
    print('A coisa ta dificil ein amigo!')

elif horas_trabalhadas < 0:
    print('Ta ganhando sem trabalhar? alo Elon musk')

else:
    print ('+ Salário Bruto : R$ %.2f' %salario_bruto)
    print ('- IR: R$ %.2f' %ir)
    print ('- INSS: R$ %.2f' %inss)
    print ('- Sindicato: R$ %.2f' %sindicato)
    print ('= Salário Liquido : R$ %.2f' %(salario_bruto - ir - inss - sindicato))