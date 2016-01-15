
from check_dni import *
from ClaseHora import *

class TarjetaPrepago:
    '''
Clase que simula una tarjeta prepago permite al usuario efectuar acciones como ingresar saldo, enviar mensajes,
realizar llamadas... llevando un control del saldo actual.

Propiedades de la Clase:
    numeroTelefono
    saldo
    nif
    consumo

Metodos (aparte de los seters y geters) de la Clase:
    ingresarSaldo
    enviarMensaje       => descuenta 0.09€ por mensaje del saldo
    realizarLlamada     => descuenta 0.15€ por establecimiento de llamada mas 0.01€ por segundo del saldo.
    consultarTarjeta    => imprime en pantalla los datos del usuario y el estado actual de su saldo.
    '''

    def __init__(self, numeroTelefono = "", saldo = 0):
##########PROPIEDADES##########
        self.numeroTelefono = numeroTelefono
        self.saldo          = saldo
        #Has a Dni
        self.nif            = Dni()
        #Has a Hora
        self.consumo        = Hora()

#########Seters y Geters###########
    def setNumeroTelefono(self, numero):
        self.numeroTelefono = numero

    def getNumeroTelefono(self):
        return self.numeroTelefono

    def setSaldo(self, saldo):
        self.saldo = saldo

    def getSaldo(self):
        return str(self.saldo) + '€'

    def setNif(self, nif):
        self.nif = nif

    def getNif(self):
        return self.nif

    def setConsumo(self, horas, minutos, segundos):
        self.consumo.setHora(horas,minutos,segundos)

    def getConsumo(self):
        return self.consumo.getHora()

##########Metodos/Funciones de la Clase##########
    def ingresarSaldo(self, cantidad):
        self.saldo += cantidad

    def enviarMensaje(self, mensajes):
        self.saldo -= 0.09 * mensajes

    def realizarLlamada(self,segundos):
        #self.contadorConsumo(segundos)
        self.saldo -= 0.15 + segundos

    def consultarTarjeta(self):
        print('Num Tel:',self.getNumeroTelefono())
        print('NIF:',self.getNif())
        print('Consumo:',self.getConsumo())
        print('Saldo Actual:',self.getSaldo())


#Formula para actualizar el consumo en construcción.
"""
    def contadorConsumo(self,segundos):
        horas   = 0
        minutos = 0
        if segundos > 60:
            minutos += segundos /60
            segundos = 0
        if minutos > 60:
           horas  += minutos / 60
           minutos = 0
        if horas < 0:
            horas = 0

        self.setConsumo(self.consumo.getHoras()+ horas,
                        self.consumo.getMinutos() + minutos,
                        self.consumo.getSegundos() + segundos)

"""



if __name__ == '__main__':
    tarjeta = TarjetaPrepago()
    tarjeta.setNif('41782549Z')
    tarjeta.setNumeroTelefono(666242197)
    tarjeta.setConsumo(1,30,49)
    tarjeta.setSaldo(10.52)
