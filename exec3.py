tempestadef = int(input("digite sua tempestade"))
if tempestadef < 61 and tempestadef == 1:
    print("tempestade fraca")
elif tempestadef >= 62 and tempestadef <= 118:
    print("tempestade  tropical")
elif tempestadef >= 119 and tempestadef <= 152:
    print("tempestade tempestuosa")
elif tempestadef >= 153 and tempestadef <= 168:
    print("tempestade formação 1")
elif tempestadef >= 169 and tempestadef <= 200:
    print("tempestade formação 2")
elif tempestadef >= 201 and tempestadef <= 220:
    print("tempestade formação 3")
elif tempestadef >= 221 and tempestadef <= 240:
    print("tempestade formação 4")
elif tempestadef >= 241 and tempestadef >= 249:
    print("voce esta no olho de uma tempestade FUJA")
else:
    print("voce não corre risco de tempestade na area")