estudar = input('Digite o periodo que você estuda - M: Matutino, V: Vespertino ou N: Noturno: ')

if estudar == 'M' or estudar == 'm':
    print('Bom dia flor do dia você é aluno(a) matutino, tenha uma otima manha ^-^')
elif estudar == 'V' or estudar == 'v':
    print('Boa tarde mestre(a) você é aluno(a) vespertino, tenha uma otima tarde ^-^')
elif estudar == 'N' or estudar == 'n':
    print('Boa noite flor da noite você é aluno(a) noturno, tenha uma otima noite ^-^')
else:
    print('Comando invalido')