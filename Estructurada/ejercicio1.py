"""
1.Escribe un programa que pida por teclado un numero entero mostrando
un mensaje oportuno.A continuacion escribe en pantalla el numero leido,
el doble del número leido y el triple del mismo.
"""


def multiplicarNum(numero, multiplicador):
    try:
        a = int(numero)
        b = int(multiplicador) + 1
        contador = 1
        while b > contador:
            print (a * contador)
            contador += 1
    except ValueError:
        print("un valor introducido no es un numero entero")


numero = input("introduce un numero:")
multiplicador = input("introduce cuantas veces quieres multiplicar el numero:")

if __name__ == '__main__':
    multiplicarNum(numero,multiplicador)