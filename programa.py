nome = input("coloque seu nome")
senha = input("insira sua senha")
while nome == senha:
    print("sua senha deve ser diferente do seu nome")
    senha = input("senha: ")
else:
    print("cadastro aprovado")