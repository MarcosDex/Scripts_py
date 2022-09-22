print ('Por favor insira as respostas da prova, elas possuem: a, b, c, d ou e\n')
questaccept = ('a','c','d','d','e','b','c','c','a','b','d','c','b','e','c','b','a','e','b','c')
questoes = []
n = 20
for x in range (0,20):
    enunciadoR = input('Insira a resposta do aluno referente a questão %d: ' % (x + 1))
    questoes.append(enunciadoR)
questaccept = sum(a == b for a, b in zip(questaccept, questoes))
overlap = questaccept / len(questoes) * 100
if overlap >= 60.0:
  print('Parabens, você conseguiu %d/100, logo esta classificado!' % (overlap))
else:
  print('Estude mais na proxima você atingiu %d/100, desclassificado!' % (overlap))

cadastrarnewaluno = input('\nDeseja cadastrar outra nota? (s,n): ')

while cadastrarnewaluno == 'S' or cadastrarnewaluno == 's':
    print('Por favor insira as respostas da prova, elas possuem: a, b, c, d ou e\n')
    questaccept = ('a', 'c', 'd', 'd', 'e', 'b', 'c', 'c', 'a', 'b', 'd', 'c', 'b', 'e', 'c', 'b', 'a', 'e', 'b', 'c')
    questoes = []
    n = 20
    for x in range(0, 20):
        enunciadoR = input('Insira a resposta do aluno referente a questão %d: ' % (x + 1))
        questoes.append(enunciadoR)
    questaccept = sum(a == b for a, b in zip(questaccept, questoes))
    overlap = questaccept / len(questoes) * 100
    if overlap >= 60.0:
        print('Parabens, você conseguiu %d/100, logo esta classificado!' % (overlap))
    else:
        print('Estude mais na proxima você atingiu %d/100, desclassificado!' % (overlap))
    cadastrarnewaluno = input('\nDeseja cadastrar outra nota? (s,n): ')
else:
    print('Fim do programa!')