#funciones matematicas
def suma(a,b):
    return a + b
def resta(a,b):
    return a - b
def multiplicacion(a,b):
    return a * b
def division(a,b):
    if(b == 0):
        return "no se puede dividir por 0"
    else:
        return a/b
def raiz(a,b = 2):
    return a ** (1/b)

if __name__ == '__main__':
    print("La suma de 3 y 4 son", suma(3,4))
    print("La resta de 3 y 4 son", resta(3,4))
    print("La multipliccacion de 3 y 4 son", multiplicacion(3,4))
    print("La division de 3 y 4 son", division(3,4))
    print("La raiz de", raiz(3))