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

def calc_resto(importe, dinero):
    return importe % dinero

def calc_cantidad(importe, dinero):
    return importe // dinero


def calc_total_moneda(importe):
    moneda = [100, 50, 20, 10, 5, 2, 1]
    for elemento in moneda:
        if elemento > 2:
            print ('%s billetes de %s' % (calc_cantidad(importe,elemento), elemento))
        else:
            print ('%s monedas de %s' % (calc_cantidad(importe, elemento), elemento))
        importe = calc_resto(importe, elemento)


if __name__ == '__main__':
    calc_total_moneda(1238)