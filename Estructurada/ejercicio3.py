"""
3.Repite el ejercicio 2 utilizando una constante que represente el valor de PI.
"""


def longitudAreaCircunferencia(radio):
    PI = 3.1416
    longitudCircun = radio * PI * 2
    areaCircun = PI * radio * radio
    print ("La longitud de la circunferencia es:", longitudCircun)
    print ("El area de la circunferencia es:", areaCircun)
    return None

radio = int(input("Por favor introduce el radio de la circunferencia: "))

longitudAreaCircunferencia(radio)
