"""
15.Escribe un programa que escriba cinco veces el mensaje:
estamos estudiando metodología de la programación.
"""

def repeticion(mensaje, veces):
    contador  = 0
    while contador != veces:
        print (mensaje)
        contador += 1



mensaje = input('introduce el mensaje que quieres repetir:')
veces   = int(input('introduce cuantas veces quieres que se repita:'))

if __name__ == '__main__':
    repeticion(mensaje,veces)