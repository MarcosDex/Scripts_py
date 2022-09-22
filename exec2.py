nome = input('coloque seu nome: ')
idade = int(input("coloque sua idade: "))
salario = int(input("Qual seu salario?"))
sexo = input("M/F")
estcivil = input("s,c,v,d")
while len(nome) <= 3:
    nome = input("seu nome é pequeno")
while (idade < 0) or (idade > 150):
    idade = int(input("vc deve ter entre 0 a 150 anos"))
while (salario < 0):
    salario = float(input("a coisa ta difcil, mas n tem salario negativo: "))
while (sexo!="f") and (sexo!="m"):
    while (estcivil!="s") and (estcivil!="c") and (estcivil!="v") and (estcivil!="d"):
        print("nao tem estado civil")
        estcivil = input("deve ser s,c,v ou d")