"""
1.Escribe un programa que pida por teclado un numero entero mostrando
un mensaje oportuno.A continuacion escribe en pantalla el numero leido,
el doble del número leido y el triple del mismo.
"""


def multiplicarNum(numero, multiplicador):
	try:
	    print ('Tu numero inicial es:', numero)
	    contador = 1
	    while multiplicador > 0:
		    print (numero * contador)
		    contador = contador + 1
		    multiplicador -= 1
	except ValueError:
		print ('Error, el valor introducido no es un numero entero')
	except TypeError:
		print ('Error, el segundo valor introducido no es un numero entero')


numero = input("Por favor introduce un numero entero: ")
multiplicador = int(input("introduce cuantas veces quieres multiplicarlo:")
multiplicarNum(numero, multiplicador)
