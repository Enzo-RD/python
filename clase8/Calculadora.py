#Definicion de clases
class Calculadora: #Calculadora estandar que opera con 2 numeros
    numero1: None
    numero2: None

    #constructor.
    def __init__(self, x, y):
        self.numero1 = x
        self.numero2 = y
        resultado = 0

#Operaciones, metodos.
    def sumar(self):
        self.resultado = self.numero1 + self.numero2
        return self.resultado
    def restar(self):
        self.resultado = self.numero1 - self.numero2
        return self.resultado
    def setValores(self, x, y):
        self.numero1 = x
        self.numero2 = y
    
if __name__ == "__main__":
    miCasio = Calculadora(10,30) #instaciacion de calculadora
    print(f"La suma es: {miCasio.sumar()}")
    print(f"La resta es: {miCasio.restar()}")

    miCasio.setValores(50, 50)
    print(f"La suma es: {miCasio.sumar()}")
    print(f"La resta es: {miCasio.restar()}")

    texas = Calculadora(45, 69)
    print(f"La suma es: {texas.sumar()}")
    print(f"La resta es: {texas.restar()}")