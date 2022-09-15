nota1 = int(input('coloque a media da primeira unidade'))
nota2 = int(input('colqoue a media da segunda unidade'))
nota3 = int(input('coloque a media da terceira unidade'))
nota4 = int(input('coloque a media da quarta unidade'))
media = nota1+nota2+nota3+nota4
mediaanual = media/4

if mediaanual >= 7:
    print('Aluno passou deboassa')

elif mediaanual == 6:
    print('Aluno passou por um triz')

elif mediaanual < 0:
   print('Não existem notas negativa')


else:
    print('Aluno reprovado')



if mediaanual >= 0:
    print('A media dos quatro bimestres do aluno foi:',media, 'Enquanto sua media anual foi:', mediaanual)

