
"""
5.Escribe un programa que calcule lo que tiene que cobrar un empleado
#sabiendo que se le tiene que aplicar al sueldo una retención del 20%.
"""


def retencion_sueldo(sueldo, retencion):
    descuento = sueldo * (retencion / 100)
    sueldo = sueldo - descuento
    print ("Tras aplicarse una retencion del %s porciento" %
           (retencion), 'tu sueldo es:', int(sueldo), '€')
    return None

sueldo = int(input("Por favor introduce tu sueldo:"))
retencion = int(input('intoduce el porcentaje de retencion sin el simbolo %:'))


retencion_sueldo(sueldo, retencion)
