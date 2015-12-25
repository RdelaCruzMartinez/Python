"""
Programa que solicita numeros hasta que el caracter de salida es introducido, despues compara los numeros y
muestra el menor, el mayor y la media
"""

def mayor_menor_media():
    print ('Introduce numeros para compararlos, cuando acabes pulsa "q"')
    lista_numeros = []
    numero = 0
    Flag = True
    while Flag:
        if numero != 'q':
            numero= input('Introduce un numero:')
            lista_numeros.append(numero)
        else:
            Flag = False
            lista_numeros.pop()
        
    lista_numeros= list(map(int, lista_numeros)) 
    mayor = lista_numeros[0]
    media = 0
    menor = mayor
    total = len(lista_numeros)
    for num in lista_numeros:
        if num > mayor:
            mayor = num
        elif num < menor:
            menor = num
        media = media + num
    media = media / total
    return mayor, menor, media

     
mayor, menor, media = mayor_menor_media()

print ('El num mayor es:', mayor)
print ('El num menor es:', menor)
print ('La media es:', media)


