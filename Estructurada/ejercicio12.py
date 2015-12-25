"""
12.Escribe un programa que pida por teclado dos números y que calcule y muestre
su suma solamente si:

a) los dos son pares 
b) el primero es menor que cincuenta y el segundo está dentro del intervalo
cerrado 100-500.

En el caso de que no se cumplan las condiciones, en vez de la suma ha de
visualizarse un mensaje de error.
"""

#Rutina
def sumacondicional(a,b):
    if a % 2 == 1 or b % 2 == 1:
        return -1
    elif a>50:
        return -2
    elif b>500 or b<100:
        return -3
    else:
        return a+b
    
#Programa
primerNumero=int(input("Introduce el primer número: "))
segundoNumero=int(input("Introduce el segundo número: "))

resultado=sumacondicional(primerNumero,segundoNumero)


if resultado == -1:
    print ("Uno o ambos números no son pares")
elif resultado == -2:
    print ("El primer número es mayor de 50")
elif resultado == -3:
    print ("El segundo número no se encuentra entre 100-500")
else:
    print (resultado)
