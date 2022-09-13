idade = int(input('digite sua idade'))
acompado = input("voce esta acompanhado de um adutlo? sim ou não")

if (acompado == "sim") or idade >= 18:
    print("entrada liberada")
else:
    print("entrada proibida")