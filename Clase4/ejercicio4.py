lista = []
x = 1

while x != 0 :
    x = int(input("Ingrese la calificacion"))
    if(x != 0 and (x == 1 or x == 5)): #condicion que solo guarda 1 o 5
        lista.append(x)#guardar x en la lista

#promedio
sumador = 0
for x in range(len(lista)):
    sumador = sumador + lista[x]

promedio = sumador / len(lista)
print("El promedio es ", promedio)