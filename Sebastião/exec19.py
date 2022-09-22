#Crie um programa para preencher um vetor (lista) com números inteiros e solicitar um número do
#teclado. Pesquisar se esse número existe no vetor. Se existir, imprimir em qual posição do vetor (lista)
#foi digitado. Se não existir, imprimir mensagem que não existe.
procurar = int(input('Digite algum caractere situado entre 0 e 9 para procurar:'))

pain = [0,1,2,3,4,5,6,7,8,9]

if procurar > 9:
    print('Não existe esse numero na vetorização')
else:
    for n, valor in enumerate(pain):
        print(f"Índice={n} | Valor={valor}")