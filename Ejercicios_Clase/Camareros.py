from cierreJornada import *

class Empleado:

    def __init__(self, nombre = "test"):
        self.nombre = nombre
        self.porcentajeGanancias = 0

    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def setPorcentajeGanancias(self, porcentaje):
        self.porcentajeGanancias = porcentaje

    def getPorcentajeGanancias(self):
        return self.porcentajeGanancias

class Cocinero(Empleado):

    def __init__(self, nombre = "test"):
        Empleado.__init__(self, nombre)

    def calcularGananciasPropinas(self, cierreJornada):
        return cierreJornada.getTotalPropinas() * self.getPorcentajeGanancias()

class Camarero(Empleado):

    def __init__(self,nombre = "test"):
        Empleado.__init__(self, nombre)
        self.horasTrabajadasJornada = 0

    def setHorasTrabajadasJornada(self, horas):
        self.horasTrabajadasJornada = horas

    def getHorasTrabajadasJornada(self):
        return self.horasTrabajadasJornada

    def calcularGananciasPropinas(self, cierreJornada):
        return self.getHorasTrabajadasJornada() * cierreJornada.getTotalPropinas() * self.getPorcentajeGanancias() / cierreJornada.getTotalHorasCamareros()


class Becario(Camarero):

    def __init__(self, nombre):
        Camarero.__init__(self, nombre)
        self.propinas = 0

    def setPropinas(self, totalPropinas):
        self.propinas = totalPropinas

    def getPropinas(self):
        return self.propinas

    def calcularGananciasPropinas(self, jornada):
        return self.getPropinas()

if __name__ == '__main__':
    jornada = CierreJornada()
    jornada.setTotalPropinas(200)
    jornada.setTotalHorasCamareros(15)

    plantillaPersonal = []

    cocinero = Cocinero("Chez")
    plantillaPersonal.append(cocinero)
    cocinero.setPorcentajeGanancias(50 /100)


    camarero = Camarero("Barreiro")
    plantillaPersonal.append(camarero)
    camarero.setPorcentajeGanancias(50 /100)
    camarero.setHorasTrabajadasJornada(3)

    becario = Becario('Timmy')
    plantillaPersonal.append(becario)
    becario.setPropinas(10)



    for empleado in plantillaPersonal:
        print("Ganancias de %s son %d" %(empleado.getNombre(), empleado.calcularGananciasPropinas(jornada) ) )
