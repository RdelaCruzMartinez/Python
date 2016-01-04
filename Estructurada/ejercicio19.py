"""
19.Lee por teclado 5 números enteros positivos, y escribe cuál es el mayor de los
números introducidos.
"""



def mayorDos(a,b):
    if a > b:
        return a
    else:
        return b

def mayorCinco(a):
    pasoUno=mayorDos(a[3:4], a[4:5])
    pasoDos=mayorDos(a[1:2], a[2:3])
    pasoTres=mayorDos(pasoUno,pasoDos)
    resultado=mayorDos(a[0:1],pasoTres)
    return resultado

contenedorNum=[]
contador=5
while contador > 0:
    numero=(int(input('Introduce un número: ')))
    contenedorNum.append(numero)
    contador=contador-1

    
print('El mayor número es:',mayorCinco(contenedorNum))

