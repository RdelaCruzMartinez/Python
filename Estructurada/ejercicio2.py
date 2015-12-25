"""
2.Escribe un programa que pida por teclado el radio de una circunferencia,
y que a continuación calcule y escriba en pantalla la longitud de la
circunferencia y del área del círculo.
"""

def longitudAreaCircunferencia(radio):
	longitudCircun= radio * 3.1416 * 2
	areaCircun= 3.1416 * radio * radio
	print ("La longitud de la circunferencia es:",longitudCircun)
	print ("El area de la circunferencia es:",areaCircun)
	return None

radio = int(input("Por favor introduce el radio de la circunferencia: "))

longitudAreaCircunferencia(radio)

