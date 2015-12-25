"""
22.Repite el programa anterior, pero en vez de leer 5 números, el usuario ha
de indicar antes cuántos números van a ser leídos, indicándolo mediante el
mensaje: Introduzca cuántos números tienen que leerse por teclado: _
"""


totalNumeros=int(input('Introduce la cantidad de números a comparar: '))
contenedor=[]

while totalNumeros > 0:
    numero=(int(input('Introduce un número: ')))
    while numero < 0:
        print ('Error, porfavor introduce un número POSITIVO')
        numero=(int(input('Introduce un número: ')))
    contenedor.append(numero)
    totalNumeros=totalNumeros-1

print ('El número mayor es',max(contenedor))
print ('El número menor es',min(contenedor))
