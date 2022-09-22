#Faça um programa que cadastre o nome, a altura, o peso, o cpf e sexo de algumas pessoas. Com
#os dados cadastrados, em seguida localizar uma pessoas através do seu CPF e imprimir o seu IMC.
#Obs.: Solicitar ao usuário se deseja cadastrar mais pessoas ou parar.
people = []
while True:
    person = []
    name = input('\nColoque o nome da pessoa: ')
    gender = input('Coloque seu genero (m/f): ')
    while gender not in ('M', 'm', 'F', 'f'):
        print('Binarie?')
        gender = input('Digite seu genero Masculino ou Feminino (m/f): ')
    height = float(input('Coloque sua altura em Metros: '))
    weight = float(input('Coloque seu peso em KG: '))
    cpf = input('Digite seu CPF: ')
    while len(cpf) != 11:
        print('Erro 404 - o CPF informado não contem 11 digito!')
        cpf = input('Coloque seu CPF: ')
    imc = (weight / (height * height))
    person.append(name)
    person.append(gender)
    person.append(height)
    person.append(weight)
    person.append(cpf)
    person.append(imc)
    people.append(person)
    answer = input('\nQuer adicionar outra pessoa?(y/n) ')
    if answer in ('Y', 'y'):
        continue
    elif answer in ('N', 'n'):
        break
    else:
        print('Comando desconhecido!')
        answer = input('\nQuer adicionar outra pessoa? (y/n) ')
call = input('\nColoque um cpf para achar uma pessoa: ')
while len(call) != 11:
    print('Erro 404 - o CPF informado não contem 11 digito!')
    call = input('Coloque um cpf para achar a pessoa: ')
for elem in people:
    if call in elem:
        print('\n')
        print(elem)