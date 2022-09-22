#Faça um programa que exiba na tela a quantidade de acertos de cada aluno em uma prova, e
#caso a nota seja igual ou maior que 60% da quantidade de questões exiba “Classificado”, se não
#“Desclassificado”. Para isso crie uma TUPLA que receba o cartão gabarito com as 20 questões, cada
#uma com cinco alternativas identificadas por A, B, C, D e E., Depois crie uma lista para cada Aluno e
#receba as 20 questões da prova dele e diga se o aluno está Classificado ou Desclassificado. Ao final,
#pergunte se o usuário deseja cadastrar outro aluno ou finalizar o programa.
#Obs.: Utilizar os conceitos vistos em sala de (Tupla, Lista, Estrutura Condicionais e Repetições);
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