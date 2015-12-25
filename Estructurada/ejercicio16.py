"""
16. Escribe un programa que escriba en pantalla los 30 primeros números
naturales (del 1 al 30), así como su media aritmética.
"""
numeros=0
total=0

while numeros <30:
    numeros=numeros+1
    total=total + numeros
    print (numeros)
    

print (total / numeros)
input ("Presiona cualquier tecla para salir")
