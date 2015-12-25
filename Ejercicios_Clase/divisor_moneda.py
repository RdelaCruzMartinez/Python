"""
Programa que dada una cifra inicial de dinero, la divide entre diversas cantidades de billetes y monedas.
"""

def calcularBilletes(importe, billete):
    numBilletes = importe // billete
    return numBilletes

def calcularResto(importe, billete):
    resto = importe % billete
    return resto

def divisor_moneda(cifra):
    listaMoneda = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    for billete in listaMoneda:
        if billete > 2:
            print ('%s billetes de %s' % (calcularBilletes(cifra, billete), billete))
        else:
            print ('%s monedas de %s' % (calcularBilletes(cifra, billete), billete))
        cifra = calcularResto(cifra,billete)




