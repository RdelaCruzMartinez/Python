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
