"""
14.Escribe un programa que pida por teclado una cantidad de dinero y que a
continuación muestre la descomposición de dicho importe en el menor número
de billetes y monedas de 100, 50, 20, 10, 5, 2 y 1 euro.
En el caso de que alguna moneda no intervenga en la descomposición no se
tiene que visualizar nada en la pantalla.
Para una cantidad de 2236 euros la salida que generaría el programa sería:
22 billetes de 100 euros
1 billete de 20 euros
1 billete de 10 euros
1 billete de 5 euros
1 moneda de 1 euro
"""

def recuento(a):
    billete100=a//100
    a=a-billete100*100
    billete50=a//50
    a=a-billete50*50
    billete20=a//20
    a=a-billete20*20
    billete10=a//10
    a=a-billete10*10
    billete5=a//5
    a=a-billete5*5
    moneda2=a//2
    a=a-moneda2*2
    moneda1=a//1
    return billete100,'billetes de 100€',billete50,'billetes de 50€',billete20,'billetes de 20€',billete10,'billetes de 10€',billete5,'billetes de 5€',moneda2,'monedas de 2€',moneda1,'monedas de 1€'

dinero= int(input('Introduce el dinero a desglosar: '))

print (recuento(dinero))
