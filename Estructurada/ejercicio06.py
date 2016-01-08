"""
6.Escribe un programa que pida por teclado dos valores de tipo numérico
que se han de guardar en sendas variables.
¿Qué instrucciones habría que utilizar para intercambiar su contenido?
(es necesario utilizar una variable auxiliar).
Para comprobar que el algoritmo ideado es correcto, muestra en pantalla el
contenido de las variables una vez leídas, y vuelve a mostrar su contenido
una vez hayas intercambiado sus valores.
"""

def intercambiar_valores(primerValor, segundoValor):
    cambioValor = primerValor
    primerValor = segundoValor
    segundoValor = cambioValor
    print("Ahora el primer valor es:",primerValor)
    print("Ahora el segundo valor es:",segundoValor)

primerValor = int(input("Por favor introduce el primer valor:" ))
segundoValor = int(input("Por favor introduce el segundo valor:"))
print ("Tu primer valor es:",primerValor)
print ("Tu segundo valor es:",segundoValor)

intercambiar_valores(primerValor, segundoValor)