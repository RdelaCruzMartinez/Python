"""
18.Escribe un programa que visualice los n-primeros múltiplos de 2,
siendo n un valor leído por teclado.
"""

n=int(input("introduce el numero de multiplos de 2 a calcular: "))


fin=n
multiplicador=1
while fin >0:
    print (multiplicador * 2)
    multiplicador=multiplicador+1
    fin=fin-1

