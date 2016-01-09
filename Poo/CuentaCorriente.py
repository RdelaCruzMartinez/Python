from check_dni import *

class CuentaCorriente:

    def __init__(self):
        self.nombre    = ""
        self.apellidos = ""
        self.direccion = ""
        self.telefono  = ""
        self.saldo     = 0
        # Has - a
        self.nif       = Dni()

    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def setApellidos(self, apellidos):
        self.apellidos = apellidos

    def getApellidos(self):
        return self.apellidos

    def setDireccion(self, direccion):
        self.direccion = direccion

    def getDireccion(self):
        return self.direccion

    def setTelefono(self, telefono):
        self.telefono = telefono

    def getTelefono(self):
        return self.telefono

    def setSaldo(self, saldo):
        self.saldo = saldo

    def getSaldo(self):
        return self.saldo

    def setNif(self, nif):
        self.nif = nif

    def getNif(self):
        return self.nif

    def retirarDinero(self, cantidad):
        self.setSaldo(self.getSaldo() - cantidad)

    def ingresardinero(self, cantidad):
        self.setSaldo(self.getSaldo() + cantidad)

    def consultarCuenta(self):
        print('Usuario:',self.nombre, self.apellidos)
        print ('NIF:', self.nif)
        print('Direccion:',self.direccion)
        print('Tel:',self.telefono)
        print('Su saldo actual es:', self.saldo)

    def saldoNegativo(self):
        if self.getSaldo() < 0:
            return True
        else:
            return False


if __name__ == '__main__':
#Test Informacion Personal
    cuenta = CuentaCorriente()
    cuenta.setNombre('Ramon')
    cuenta.setApellidos('De la Cruz Martinez')
    cuenta.setDireccion('Calle random')
    cuenta.setNif('41782596Z')
    cuenta.setTelefono('112')

    testInfoPersonal = [[cuenta.getNombre(),'Ramon'],
                        [cuenta.getApellidos(),'De la Cruz Martinez'],
                        [cuenta.getDireccion(),'Calle random'],
                        [cuenta.getNif(),'41782596Z'],
                        [cuenta.getTelefono(),'112']]

    for caso in testInfoPersonal:
        if testInfoPersonal[0][0] == testInfoPersonal[0][1]:
            print(caso, 'OK')
        else:
            print(caso, 'FAIL')

 #Test Saldo
    cuenta.setSaldo(510.50)
    cuenta.ingresardinero(110.25)
    cuenta.retirarDinero(120.75)
    if cuenta.getSaldo() == 500:
        print('Test Saldo OK')
    else:
        print('Test Saldo FAIL')

    cuenta.retirarDinero(600)
    if cuenta.saldoNegativo() == True:
        print('Test Saldo negativo OK')
    else:
        print('Test Saldo negativo FAIL')




