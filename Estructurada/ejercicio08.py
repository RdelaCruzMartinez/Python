"""
8.Escribe un programa que pida por teclado dos números y que muestre
en pantalla uno de los dos mensajes siguientes en función de los
números leídos:
a) el primer número (valor) es mayor que el segundo(valor)(introduciendo el valor de los números en el mensaje)
b) el primer número (valor) es menor que el segundo (valor;
c) los dos números son iguales (valor).
"""

def comparador(a,b):
    if a > b:
        print ("%i es mas grande que %i" % (a,b))
    elif a == b:
        print ("los numeros son iguales:",a)
    else:
        print ("%i es mas grande que %i" % (b,a))


numberOne = int(input("Por favor introduce el primer número:"))
numberTwo = int(input("Por favor introduce el segundo número:"))

if __name__ == '__main__':
    comparador(numberOne,numberTwo)

