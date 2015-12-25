"""
4.Escribe un programa que calcule el área de una finca rectangular en metros
cuadrados,así como su perímetro exterior, también en metros.
"""


def area_rectangulo(altura, base):
    area = base * altura
    perimetro= 2 * (base + altura)
    print ("El area de la finca es:",area,"m2")
    print ("El perimetro de la finca es:",perimetro,"m")
    return None

altura= int(input("introduce la altura de la finca:"))
base= int(input("introduce la base de la finca:"))

area_rectangulo(altura, base)
