
class Fecha:
    """
    Clase Fecha, simula una fecha con rangos del 1-1-1900 al 31-12-3000,
    permite incrementar/reducir dias, meses y años siempre que se respete el formato.
    ATENCION para esta clase se parte de la premisa erronea que todos los meses tienen 31 dias.

    Propiedades de la clase:
        dia (1-31)
        mes (1-12)
        año (1900-3000)

    Metodos (aparte de los seters y geters) de la Clase:
        incrementarFecha => incrementa la fecha en el numero de dias que se indique.
        imprimirFecha    => Devuelve la fecha en formato "dia-mes-año" aportando el nombre del mes no su valor numerico.
    """

    def __init__(self, dia = 1, mes = 1, año = 1900):
##########PROPIEDADES##########
        self.dia    = dia
        self.mes    = mes
        self.año    = año

#########Seters y Geters###########
    def setDia(self,dia):
        if dia in range(1,32):
            self.dia = dia
        else:
            self.dia = 1

    def getDia(self):
        return self.dia

    def setMes(self,mes):
        if mes in range(1,13):
            self.mes = mes
        else:
            self.mes = 1

    def getMes(self):
        return self.mes

    def setAño(self,año):
        if año in range(1900,3001):
            self.año = año
        else:
            self.año = 1900

    def getAño(self):
        return self.año

##########Metodos/Funciones de la Clase##########
    def setFecha(self, dia, mes, año):
        self.setDia(dia)
        self.setMes(mes)
        self.setAño(año)

    def incrementarFecha(self,dias):
        self.contadorDias(dias)

    def imprimirFecha(self):
        mes = self.calcMes()
        return "%s-%s-%s" % (self.getDia(),mes,self.getAño())

    def contadorDias(self, diasAñadidos):
        año     = self.getAño()
        mes     = self.getMes()
        dias    = self.getDia()

        while diasAñadidos > 0:
            dias            += 1
            diasAñadidos    -= 1

            if dias > 31:
                mes += 1
                dias = 0
            if mes  > 12:
                año += 1
                mes  = 0

        self.setFecha(dias,mes,año)

    def calcMes(self):
        meses = ('Enero','Febrero','Marzo','Abril','Mayo','Junio',
                 'Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre')

        mes = meses[self.getMes() -1 ]

        return mes



if __name__ == '__main__':
    fecha = Fecha()
    fecha.setAño(1993)
    fecha.setMes(11)
    fecha.setDia(25)
    print(fecha.getDia(),fecha.getMes(),fecha.getAño())
    fecha.incrementarFecha(5)
    print(fecha.getDia(),fecha.getMes(),fecha.getAño())
    fecha.incrementarFecha(5)
    print(fecha.getDia(),fecha.getMes(),fecha.getAño())
    fecha.incrementarFecha(31)
    print(fecha.getDia(),fecha.getMes(),fecha.getAño())
    print(fecha.imprimirFecha())