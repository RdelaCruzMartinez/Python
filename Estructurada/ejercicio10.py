"""
10.Modifica el programa anterior para que en vez de mostrar un mensaje genérico
en el caso de que alguno o los dos números sean negativos, escriba una salida
diferenciada para cada una de las situaciones que se puedan producir,
utilizando los siguientes mensajes:
a) No se calcula la suma porque el primer número es negativo.
b) No se calcula la suma porque el segundo número es negativo.
c) No se calcula la suma porque los dos números son negativos.
"""


numberOne = int(input("Introduce el primer número:"))
numberTwo = int(input("introduce el segundo número:"))


if numberOne and numberTwo < 0:
    print ("No se calcula la suma porque los dos números son negativos")
elif numberOne < 0:
    print ("No se calcula la suma porque el primer número es negativo")
elif numberTwo < 0:
    print ("No se calcula la suma porque el segundo número es negativo")
else:
    print(numberOne + numberTwo)
