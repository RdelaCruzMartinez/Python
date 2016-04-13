import math


def raizcuadrada(x):
    #Precondiciones, número real
    x = float(x)
    # Número positivo
    if x < 0:
        raise Exception("El valor introducido debe ser superior a 0")
    else:
        b = x

        if b == 0:
            return b
        else:
            fin = False
            while not fin:
                if b == x/b:
                    return b
                else:
                    b  = (1/2)*(x/b + b)
        #Postcondición: el resultado al cuadrado debe ser igual al número inicial.
        assert x == b * b

def test():

    print("Introduce x")
    x = input('x = ')
    # raw_input devuelve un string

    print(raizcuadrada(x))

test()