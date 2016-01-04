"""
16. Escribe un programa que escriba en pantalla los 30 primeros números
naturales (del 1 al 30), así como su media aritmética.
"""

def imprimir_rangos(inicial,final):
    while inicial != final:
        print(inicial)
        inicial += 1
    print (inicial)

inicial = int(input('Introduce el numero inicial:'))
final   = int(input('Introduce el numero final del rango:'))

if __name__ == '__main__':
    imprimir_rangos(inicial,final)

