x = int(input("Ingrese el primer numero "))
y = int(input("Ingrese el segundo numero "))
for z in range(x, y+1):
    if z%2 == 0:
        print(z)