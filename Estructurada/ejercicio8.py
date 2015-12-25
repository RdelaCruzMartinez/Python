"""
8.Escribe un programa que pida por teclado dos números y que muestre
en pantalla uno de los dos mensajes siguientes en función de los
números leídos:
a) el primer número (valor) es mayor que el segundo(valor)(introduciendo el valor de los números en el mensaje)
b) el primer número (valor) es menor que el segundo (valor;
c) los dos números son iguales (valor).
"""


numberOne= int(input("Por favor introduce el primer número:"))
numberTwo= int(input("Por favor introduce el segundo número:"))

if numberOne > numberTwo:
    print (numberOne,"es mayor")
if numberTwo > numberOne:
    print (numberTwo,"es mayor")
elif numberOne == numberTwo:
    print ("Los dos números son iguales")

input ("Presiona cualquier tecla para salir")
