#Faça um programa que peça do usuário o nome de 6 cidades, depois de inseridas verifique se há
#nomes iguais e havendo peça para que sejam inseridos novamente, e também crie a opção do usuário
#concatenar dados ao nome da cidade. E por fim, exiba qual o nome de cidade mais extenso.
cities = []
for i in range (0,6):
    inputs = input('Por favor insira a %d cidade: ' % (i + 1))
    if inputs in cities:
        inputs = input('Esse nome ja contem na lista, por favor insira outro: ')
    cities.append(inputs)
    answer = input('Você quer extender o nome da cidade? (y/n) ')
    if answer in ('Y', 'y'):
        extra = input('Coloque sua extensão:')
        cities[i] = cities[i] + extra
        print(cities[i])
print('O nome das cidade digitadas são: ', *cities)
longest = max(cities,key=len)
print(longest,'É o nome da maior cidade digitada!')