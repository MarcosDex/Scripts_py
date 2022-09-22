#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de
#um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando
#este link (em minutos)
arquivo = float(input("Digite do tamanho do arquivo em MegaByte: "))
link = float(input("Digite a velocidade do link em Mbps: "))
tempo = ((arquivo * 8) / link) / 60

if arquivo < 0 or link < 0:
    print('Você não esta tentando baixar nada')
else:
    print("O tempo aproximado de download é de %.2f minutos" %tempo)