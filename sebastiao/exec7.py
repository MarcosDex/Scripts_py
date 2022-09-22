#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
lado = int(input("Digite o tamanho do lado do quadrado: "))
area = float(lado) * float(lado)

if lado < 0:
    print('Não existem lados negativos')
else:
    print("O dobro da area do quadrado é: ",area * 2)
    print(area)