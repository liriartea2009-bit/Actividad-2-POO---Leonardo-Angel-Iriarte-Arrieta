from enum import Enum

class TipoCuenta(Enum):
    AHORROS = ("Ahorros", 0.02)     # Interés
    CORRIENTE = ("Corriente", 0.0)  # Sin interés

    def __init__(self, descripcion, tasa_interes):
        self.descripcion = descripcion
        self.tasa_interes = tasa_interes

    # Método para calcular el rendimiento mensual del saldo
    def calcular_interes_mensual(self, saldo):
        return (saldo * self.tasa_interes) / 12

    # Formato al imprimir el enum
    def __str__(self):
        return self.descripcion


# 2. Clase principal CuentaBancaria
class CuentaBancaria:
    # Constructor
    def __init__(self, nombres_titular, apellidos_titular, numero_cuenta, tipo_cuenta):
        self.nombres_titular = nombres_titular
        self.apellidos_titular = apellidos_titular
        self.numero_cuenta = numero_cuenta
        self.tipo_cuenta = tipo_cuenta  # Espera una instancia de TipoCuenta
        self.saldo = 0.0
        
    # Método para consignar dinero (sin valor de retorno)
    def consignar(self, valor):
        self.saldo += valor
        print(f"Consignación exitosa: ${valor:.2f}")
        
    # Método para retirar dinero (retorna boolean)
    def retirar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente para realizar el retiro")
            return False
        
        self.saldo -= valor
        print(f"Retiro exitoso: ${valor:.2f}")
        return True
        
    # Método para aplicar el interés según el tipo de cuenta
    def aplicar_interes_mensual(self):
        interes = self.tipo_cuenta.calcular_interes_mensual(self.saldo)
        self.saldo += interes
        print(f"Interés mensual aplicado ({self.tipo_cuenta}): ${interes:.2f}")

    # Método para consultar el saldo (sin valor de retorno)
    def consultar_saldo(self):
        print(f"Saldo actual: ${self.saldo:.2f}")
        
    # Representación en texto del objeto
    def __str__(self):
        return (f"=== DATOS DE LA CUENTA ===\n"
                f"Titular: {self.nombres_titular} {self.apellidos_titular}\n"
                f"Número de Cuenta: {self.numero_cuenta}\n"
                f"Tipo de Cuenta: {self.tipo_cuenta}\n"
                f"Saldo: ${self.saldo:.2f}\n"
                f"==========================")

# Método main
if __name__ == "__main__":
    print("Ejercicio 2.4 - Métodos con y sin Valores de Retorno (Con Enum)\n")
    
    # Se crea la cuenta pasando la constante del Enum
    cuenta1 = CuentaBancaria("Juan", "Pérez", 1001, TipoCuenta.AHORROS)
    
    print(cuenta1)
    print() 
    
    # Pruebas de los métodos
    cuenta1.consignar(5000)
    cuenta1.aplicar_interes_mensual()
    cuenta1.consultar_saldo()
    
    print() # Salto de línea
    
    cuenta1.retirar(2000)
    cuenta1.consultar_saldo()
    
    cuenta1.retirar(5000)
    cuenta1.consultar_saldo()