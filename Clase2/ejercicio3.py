#Operadores aritmeticos
#Imprimir la suma de 3 + 4
print("La suma de 3 + 4 es ", 3+4)

#Resolver todas las operaciones : 10-4, 10*4, 10/4, 10%4, 10//4, 10**4
print("El resultado de las siguientes operaciones10-4, 10*4, 10/4, 10%4, 10//4, 10**4 es ", 10-4, 10*4, 10/4, 10%4, 10//4, 10**4)

#Resolver la ecuacion cuadratica 2x**2 - 7x + 3 = 0
a = 2
b = -7
c = 3
print(" Los resultados para la ecuacion cuadratica 2x**2 - 7x + 3 = 0 son: ")
print("x1", (-b+((((b**2)-4*a*c))**(1/2)))/(2*a))
print("x2", (-b-((((b**2)-4*a*c))**(1/2)))/(2*a))

#operaciones con cadenas de texto
print("SNPP " + "CTFPPJ " + "Programacion PYTHON")

print("Aula " + str(2102) )

#Operaciones mixtas
print("Tun chi " * 5 )
print("Ja " * (2 ** 3))

#operadores de comparacion
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)

#Operaciones con cadenas de texto
print( "python" > "python")
print( "aaaa" >= "abaa")  #Ordenacion alfabetica por ASCII
print( len("aaaa") >= len("abaa"))  #cuenta caracteres

print("python" != "PYTHON")

###Operadores logicos
print( 10 > 4 and "Z" > "A" )
print( 10 > 4 or "Z" > "A" )
print( not(10 > 4) and "Z" > "A" )
