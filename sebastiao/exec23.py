n1 = int(input('Digite sua nota: '))
n2 = int(input('Digite sua 2° nota: '))

nota = (n1 + n2) / 2

if nota >= 7 and nota < 10:
    print('Você foi Aprovado!!')
elif nota >= 10:
    print('Você foi aprovado com Distinção!')
elif n1 < 0 or n2 < 0:
    print('O aluno foi tão ruim assim para merecer notas negativas?')
else:
    print('Infelizmente você foi reprovado')