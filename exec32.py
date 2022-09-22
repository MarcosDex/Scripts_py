#Faça um programa que cadastre o nome, a matrícula e duas notas de 13 alunos. Em seguida
#imprima a matrícula, o nome e a média de cada um deles.
students = []
for i in range(13):
    student = []
    print(f"\nVocê esta trabalhando no estudante {i+1}")
    name = input('Insira o nome do estudante: ')
    password = input('Insira uma senha de até 8 caracteres: ')
    while len(password) != 8:
        print('Senha possue menos de 8 caracteres!')
        password = input('Input the 8 digit password: ')
    grade1 = float(input('Insira a primeira nota 0 e 10: '))
    while grade1 < 0 or grade1 > 10:
        print('Notas invalidas!')
        grade1 = float(input('Insira a primeira nota entre 0 e 10: '))
    grade2 = float(input('Insira a segunda nota situada entre 0 e 10: '))
    while grade2 < 0 or grade2 > 10:
        print('Notas invalidas!')
        grade2 = float(input('Insira a nota situada entre 0 e 10: '))
    average = (grade1 + grade2) / 2
    student.append(name)
    student.append(password)
    student.append(average)
    print(student)
    students.append(student)
for i in range (13):
    print(students[i])