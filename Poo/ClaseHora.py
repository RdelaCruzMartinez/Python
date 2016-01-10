
class Hora:

    def __init__(self, hora = 0, minutos = 0, segundos = 0):
        self.hora       = hora
        self.minutos    = minutos
        self.segundos   = segundos

    def setHora(self,horas,minutos,segundos):
        self.setHoras(horas)
        self.setMinutos(minutos)
        self.setSegundos(segundos)

    def getHora(self):
        return '%s:%s:%s' %(self.hora, self.minutos, self.segundos)

    def imprimirHora(self):
        print (self.getHora())


    def setHoras(self, horas):
        if horas in range(25):
            self.hora = int(horas)
        else:
            pass

    def getHoras(self):
        return self.hora

    def setMinutos(self, minutos):
        if minutos in range (60):
            self.minutos = int(minutos)
        else:
            pass

    def getMinutos(self):
        return self.minutos

    def setSegundos(self, segundos):
        if segundos in range (60):
            self.segundos = int(segundos)
        else:
            pass

    def getSegundos(self):
        return self.segundos

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
        if testEnRango[0][0] == testEnRango[0][1]:
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
        if testEnRango[0][0] == testEnRango[0][1]:
            print('Test fuera de rango set/get',caso,'OK')
        else:
            print('Test fuera de rango set/get',caso,'FAIL')



