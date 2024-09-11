__author__ = "Jairo Andres Vallejo Burbano"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "jairo.vallejob@campusucc.edu.co"

class CuentaAhorros:
    #----------------------------------------------------------------
    # Atributos
    #----------------------------------------------------------------
    
    __saldo = 0
    
    #----------------------------------------------------------------
    # Metodos
    #----------------------------------------------------------------
    
    __method__='ConsignarValor'
    __params__='Monto'
    __returns__='Nada'
    __descriptions__='Este metodo consignar un monto a la cuenta'
    def ConsignarValor(self, monto):
        self.__saldo=self.__saldo+monto
        
    __method__='DarSaldo'
    __params__='Ninguno'
    __returns__='Saldo'
    __descriptions__='Este metodo retorna el saldo'
    def DarSaldo(self):
        return self.__saldo
    
    __method__='RetirarValor'
    __params__='Monto'
    __returns__='Nada'
    __descriptions__='Este metodo retira un monto a la cuenta'
    def RetirarValor(self, monto):
        self.__saldo=self.__saldo-monto
   
    #TAREA 3   
    __method__='Ahorrar'
    __params__='Monto'
    __returns__='nada'
    __descriptions__='Este metodo ahorra un saldo a la cuenta'
    def Ahorrar(self, monto):
    #Pasa de la cuenta corriente a la cuenta de ahorros el valor que se entrega como parámetro (suponiendo que hay suficientes fondos).
    
    __method__='Retirar ahorro'
    __params__='Monto'
    __returns__='nada'
    __descriptions__='Este metodo permite retirar el valor de la cuenta de ahorros'
    def retirarAhorro(self, monto):
    #Retira un valor dado de la cuenta de ahorros (suponiendo que hay suficientes fondos).
    
    __method__='Duplicar Ahorro'
    __params__='Monto'
    __returns__='nada'
    __descriptions__='este metodo permite duplicar el saldo de la cuenta de ahorros'
    def duplicarAhorro(self):
    #Duplica la cantidad de dinero que hay en la cuenta de ahorros.