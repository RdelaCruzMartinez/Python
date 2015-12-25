"""
20.Repite el programa anterior, pero chequeando que el usuario no introduzca
números negativos. Si se da esta circunstancia hay que visualizar un mensaje
de error, forzando al usuario a que introduzca números positivos.
"""


def mayorDos(a,b):
    if a>b:
        return a
    else:
        return b


def mayorCinco(a):
    pasoUno=mayorDos(a[3:4], a[4:5])
    pasoDos=mayorDos(a[1:2], a[2:3])
    pasoTres=mayorDos(pasoUno,pasoDos)
    resultado=mayorDos(a[0:1],pasoTres)
    return resultado
    
contador=5
contenedorNum=[]
while contador > 0:
    numero=(int(input('Introduce un número: ')))
    while numero < 0:
        print ('Error, porfavor introduce un número POSITIVO')
        numero=(int(input('Introduce un número: ')))
    contenedorNum.append(numero)
    contador=contador-1

    
print('El mayor número es:',mayorCinco(contenedorNum))
