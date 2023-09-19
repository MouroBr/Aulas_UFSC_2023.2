numero_01 = float(input())
numero_02 = float(input())
numero_03 = float(input())

if numero_01 == numero_02 == numero_03:
    print("valores iguais")

elif numero_01 > numero_02 and numero_01 > numero_03:
    print(numero_01)
elif numero_02 > numero_03 and numero_02 > numero_03:
    print(numero_02)
else:
    print(numero_03)
