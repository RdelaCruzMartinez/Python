import math



def raizCuadrada(x, eps = 10e-7):
    try:
        #Precondiciones 1/3, un número dentro de un rango procesable sin problemas.
        if len(x) >= 10:
            raise Exception("Por favor introduce un número mas corto")
        # 2/3 número real
        else:
            x = float(x)
        # 3/3 número positivo.
            if x < 0:
                raise Exception("El valor introducido debe ser superior a 0")
            else:

                b = x

                if b == 0:
                    return b
                else:
                    fin = False
                    while not fin:
                        #Postcondición: establecemos un epsilon para controlar el margen de error
                        if abs(b * b - x) < eps:
                            return b
                        else:
                            b  = (1/2)*(x/b + b)
    except ValueError:
        print("Debes intruducir un numero real y positivo")

def test():

    print("Introduce x")
    x = input('x = ')
    # raw_input devuelve un string

    print(raizCuadrada(x))

test()


"""
Pasos que he seguido durante el Debugging

1. Escribirme un log con lo que voy haciendo (Debugging Explícito)

2. Testear la aplicación y comprobar el primer error: TypeError: unsupported operand type(s) for /: 'str' and 'str'

3. Mediante dependencia de datos identifico el problema de manera sencilla y lo
    soluciono  estableciendo una precondición que checkee que los valores  introducidos sean números reales.

4. Establezco una barricada con un Try/except para controlar que solo me entren números.

5. Introduzco otra precondición (sin assert ya que es importante que se mantenga para la logica del programa)
    para que compruebe que los números son positivos.

6. Refactorizo código de manera que me parezca más eficiente.

7. Por último establezco una precondición junto a un epsilon para que los resultados que contengan bastantes decimales
    y no sean exactos al 100% no dejen la aplicación en un bucle infinito.

8. Testeo otra vez el programa con numeros positivos, me doy cuenta que con números de gran longitud el programa no
    los procesa bien, refactorizo e introduzco una nueva precondición.

9. Testeo otra vez el programa con números que no tengan raíz entera.

10. Finalmente testeo el programa otra vez con números decimales.
"""