lista = []
x = 1

while x != 0:
    
    x = int(input("Ingrese la calificacion"))
    if(x != 0):
        lista.append(x)#guardar x en la lista

#promedio
sumador = 0
for x in range(len(lista)):
    sumador = sumador + lista[x]

promedio = sumador / len(lista)
print( "el promedio es ", promedio)

