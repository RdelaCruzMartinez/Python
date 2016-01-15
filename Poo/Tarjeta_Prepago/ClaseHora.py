
class Hora:
    '''
Clase que permite asignar una hora especificando el tiempo en:
    horas:minutos:segundos

Propiedades de la clase:
    horas       (rango 0-24)
    minutos     (rango 0-59)
    segundos    (rango 0-59)

Metodos (aparte de los seters y geters) de la Clase:
    imprimirHora    ==> Imprime la hora en pantalla.
    '''

    def __init__(self, hora = 0, minutos = 0, segundos = 0):
##########PROPIEDADES##########
        self.hora       = hora
        self.minutos    = minutos
        self.segundos   = segundos

#########Seters y Geters###########
    def setHora(self,horas,minutos,segundos):
        self.setHoras(horas)
        self.setMinutos(minutos)
        self.setSegundos(segundos)

    def getHora(self):
        return '%s:%s:%s' %(self.hora, self.minutos, self.segundos)


    def setHoras(self, horas):
        if horas in range(25):
            self.hora = int(horas)
        else:
            self.hora = 0

    def getHoras(self):
        return self.hora

    def setMinutos(self, minutos):
        if minutos in range (60):
            self.minutos = int(minutos)
        else:
            self.minutos = 0

    def getMinutos(self):
        return self.minutos

    def setSegundos(self, segundos):
        if segundos in range (60):
            self.segundos = int(segundos)
        else:
            self.segundos = 0

    def getSegundos(self):
        return self.segundos

##########Metodos/Funciones de la Clase##########
    def imprimirHora(self):
        print (self.getHora())


#Casos Test

if __name__ == '__main__':
    tiempo = Hora()
    tiempo.setHoras(24)
    tiempo.setMinutos(30)
    tiempo.setSegundos(45)

    testEnRango = [[tiempo.getHoras(),24],
                  [tiempo.getMinutos(),30],
                  [tiempo.getSegundos(),45]]
    for caso in testEnRango:
        if caso[0] == caso[1]:
            print('Test en rango set/get',caso,'OK')
        else:
            print('Test en rango set/get',caso,'FAIL')

    tiempo.setHoras(-1)
    tiempo.setMinutos(2.2)
    tiempo.setSegundos(60)


    testNoRango = [[tiempo.getHoras(),0],
                   [tiempo.getMinutos(),0],
                   [tiempo.getSegundos(),0]]
    for caso in testNoRango:
        if caso[0] == caso[1]:
            print('Test fuera de rango set/get',caso,'OK')
        else:
            print('Test fuera de rango set/get',caso,'FAIL')

    print(Hora.__doc__)



