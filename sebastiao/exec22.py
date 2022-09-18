alfa = input("Informe uma letra ou consoante:")
a = 'A'
aA = 'a'
e = 'e'
eE = 'E'
i = 'i'
iI = 'I'
o = 'o'
oO = 'O'
u = 'u'
uU = 'U'
if alfa == a or alfa == aA:
    print('vogal')
elif alfa == e or alfa == eE:
    print('Vogal')
elif alfa == i or alfa == iI:
    print('Vogal')
elif alfa == o or alfa == oO:
    print('Vogal')
elif alfa == u or alfa == uU:
    print('Vogal')
else:
    print('Consoante')




if alfa.isalnum():
    print('Isto é um numero')