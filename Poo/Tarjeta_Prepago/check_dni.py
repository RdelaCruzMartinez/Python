class TablaLetrasDni:
    def __init__(self):
        self.tabla_letras_Dni = ['T', 'R', 'W', 'A', 'G', 'M',
                                 'Y', 'F', 'P', 'D', 'X', 'B',
                                 'N', 'J', 'Z', 'S', 'Q', 'V',
                                 'H', 'L', 'C', 'K', 'E']

    # /////  INTERFAZ PUBLICA  /////#
    def get_letra(self, dni):
        return self.get_modulo(dni)

    def letra_posicion(self, letra):
        return letra in self.tabla_letras_Dni

    def mostrar_tabla(self):
        print(self.tabla_letras_Dni)

    # /////  INTERFAZ PRIVADA (METODOS)  ///// #
    def get_modulo(self, dni):
        posicion = int(dni[0:8]) % len(self.tabla_letras_Dni)
        return self.tabla_letras_Dni[posicion]


class Dni:
    def __init__(self, dni=""):
        self.dni = dni
        self.sano = False
        # Has - a
        self.tabla = TablaLetrasDni()

    # /////  INTERFAZ PUBLICA  /////#
    def set_sano(self, boolean):
        self.sano = boolean

    def get_sano(self):
        return self.sano

    def set_dni(self, dni):
        self.dni = dni

    def get_dni(self):
        return self.dni

      # /////  INTERFAZ PRIVADA (METODOS)  ///// #

    def check_dni(self):
        if self.check_longitud() and self.check_letra and self.check_numero:
            self.set_sano(True)
        else:
            self.set_sano(False)


    def check_longitud(self, dni):
        return len(dni) == 9

    def checkNumero(self):
        return self.dni[:-1].isdigit()


if __name__ == '__main__':
    tabla = TablaLetrasDni()
    dni = Dni()
    if tabla.letra_posicion('Z') == True:
        print("Test letra_posicion OK")
    else:
        print("Test letra_posicion FAIL")
    if tabla.get_letra('51428752') == 'Q':
        print("Test tabla.get_letra OK")
    else:
        print("Test tabla.get_letra FAIL")

    dni.set_sano(True)
    if dni.get_sano() == True:
        print("Test set/get_sano OK")
    else:
        print("Test set/get_sano FAIL")

    if dni.check_longitud("51428752Q") == True:
        print("Test dni.check_longitud OK")
    else:
        print("Test dni.check_longitud FAIL")
