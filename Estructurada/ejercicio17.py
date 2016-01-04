
"""
Escribe un programa que calcule la suma de los numeros pares por un lado
y de los impares por otro, de los numeros comprendidos entre dos numeros
introducidos por teclado
"""

def imprimir_suma_par_impar(inicial,final):
    pares   = 0
    impares = 0
    while inicial != final + 1:
        if inicial % 2 == 0:
            pares = pares + inicial
        else:
            impares = impares + inicial
        inicial += 1
    print ('La suma de los numeros pares es:', pares)
    print ('La suma de los numeros impares es:', impares)

inicial = int(input('Introduce el numero inicial:'))
final   = int(input('Introduce el numero final del rango:'))

if __name__ == '__main__':
    imprimir_suma_par_impar(inicial,final)