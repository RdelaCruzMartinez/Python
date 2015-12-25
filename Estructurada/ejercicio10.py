"""
10.Modifica el programa anterior para que en vez de mostrar un mensaje genérico
en el caso de que alguno o los dos números sean negativos, escriba una salida
diferenciada para cada una de las situaciones que se puedan producir,
utilizando los siguientes mensajes:
a) No se calcula la suma porque el primer número es negativo.
b) No se calcula la suma porque el segundo número es negativo.
c) No se calcula la suma porque los dos números son negativos.
"""
numberOne= int(input("Introduce el primer número:"))
numberTwo= int(input("introduce el segundo número:"))

if numberOne >-1:
    if numberTwo >-1:
        print (numberOne + numberTwo)
    else:
       print("No se calcula la suma porque el segundo número es negativo")
        
if numberOne <0:
    if numberTwo <0:
        print("No se calcula la suma porque los dos números son negativos")
    else:
        print ("No se calcula la suma porque el primer número es negativo")
    

input("Presiona cualquier tecla para salir")
