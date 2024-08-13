x = int(input("Ingrese el primer numero"))
y = int(input("Ingrese el segundo numero"))
if x>y:
    print("El mayor es", x)
    if (x % 2 == 0):
        print("El numeo es par")
    else:
        print("El numero es impar")
elif y>x:
    print("el mayor es", y)
    if (y % 2 == 0):
        print("El numeo es par")
    else:
        print("El numero es impar")
else:
    print("Los numeros son iguales")
    