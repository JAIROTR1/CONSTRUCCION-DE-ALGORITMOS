__author__ = "Jairo Andres Vallejo Burbano"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "jairo.vallejob@campusucc.edu.co"

'''----------------------------------------------------------------
# Importaciones
----------------------------------------------------------------'''
from SimuladorBancario.CuentaAhorros import CuentaAhorros
from SimuladorBancario.CuentaCorriente import CuentaCorriente
from SimuladorBancario.CDT import CDT

class SimuladorBancario:
    
    #----------------------------------------------------------------
    # Atributos
    #----------------------------------------------------------------
    
    __cedula=''
    __nombre=''
    
    __cuentaCorriente = CuentaCorriente()
    __cuentaAhorros = CuentaAhorros()
    __cdt = CDT()
    
    __mesActual = 0
    
    #----------------------------------------------------------------
    # Metodos
    #----------------------------------------------------------------
    
    __method__='ConsignarCuentaCorriente'
    __params__='Monto'
    __returns__='Nada'
    __descriptions__='Este metodo consignar un monto a la cuenta corriente'
    def ConsignarCuentaCorriente(self, monto):
        # Aqui inicia el metodo
        # self.__cuentaCorriente.saldo = self.__cuentaCorriente.saldo+monto # modo no recomendable
        self.__cuentaCorriente.ConsignarValor(monto)
        
    __method__='CalcularSaldoTotal'
    __params__='Ninguno'
    __returns__='Saldo Total'
    __descriptions__='Este metodo sumo el saldo de todas las cuentas'
    def CalcularSaldoTotal(self):
        # Aqui inicia el metodo
        # forma 1
        total = self.__cuentaCorriente.DarSaldo()+self.__cuentaAhorros.DarSaldo()
        return total
    
    __method__='PasarAhorrosACorriente'
    __params__='Ninguno'
    __returns__='Ninguno'
    __descriptions__='Este metodo transfiere el saldo de ahorros a corriente'
    def PasarAhorrosACorriente(self):
        saldoTemporal = self.   .DarSaldo()
        self.__cuentaAhorros.RetirarValor(saldoTemporal)
        self.__cuentaCorriente.ConsignarValor(saldoTemporal)
        
    __method__='Retirar todo'
    __params__='Monto'
    __returns__='nada'
    __descriptions__='Este metodo permite retirar el valor de la cuenta de ahorros y corriente'
    def retirarTodo(self):
    #Retira todo el dinero que hay en la cuenta corriente y en la cuenta de ahorros.
    
#TAREA CORREGIDA
_   _method_="Ahorrar"
    _params_="Monto"
    _returns_="Ninguno"
    _descriptions_="Este metodo permite pasar el saldo de cuenta corriente a cuenta ahorros"
    def Ahorror(self,monto):
        #Aqui inicia mi codigo
        monto = self.__cuentaCorriente.DarSaldo
        self.__cuentaCorriente.RetirarValor(monto)
        self.__CuentaAhorrosIngreso .Valornuevo (monto)
        
        
    _method_="retirarAhorro"
    _params_="Monto"
    _returns_="Ninguno"
    _descriptions_="Metodo que permite retirar un valor que dio la cuenta de ahorros"
    def retirarAhorro (self, monto):
        #Aqui inicia mi codigo
        self.__CuentaAhorrosIngreso . RetirarSaldo(monto)
        
    _method_="DarSaldoCorriente"
    _params_="Ninguno"
    _returns_="DarSaldo"
    _descriptions_="Metodo me permite retornar saldo que hay en cuenta corriente "
    def CalcularTodo(self):
        # Aqui inicia mi codigo
        return self.__cuentaCorriente.DarSaldo()
    
    _method_="RetirarTodo"
    _params_="Ninguno"
    _returns_="retirar saldo y valor"
    _descriptions_="Metodo me permite retirar todo lo que hay en la cuenta corriente y de ahorros"
    def RetirarTodo(self):
        #Aqui inicia mi codigo
        SaldoCorriente = self.__cuentaCorriente.DarSaldo()
        SaldoAhorro = self.__CuentaAhorrosIngreso.DarSaldoAhorro()
        self.__cuentaCorriente.RetirarValor(SaldoCorriente)
        self.__CuentaAhorrosIngreso.RetirarSaldo(SaldoAhorro)
    _method_="DuplicarAhorro"
    _params_="Ninguno"
    _returns_="ninguno"
    _descriptions_="metodo me permite duplicar el dinero que hay en cuenta Ahorros"
    def DuplicarAhorro(self):
        duplicar = self.__CuentaAhorrosIngreso.DarSaldoAhorro()
        self.__CuentaAhorrosIngreso.Valornuevo(duplicar)
        
        