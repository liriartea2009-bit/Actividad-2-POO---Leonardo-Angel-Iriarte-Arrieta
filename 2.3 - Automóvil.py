class Automovil:
    def __init__(self, marca, modelo, motor, tipo_combustible, tipo_automovil, 
                 numero_puertas, cantidad_asientos, velocidad_maxima, color):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.tipo_combustible = tipo_combustible
        self.tipo_automovil = tipo_automovil
        self.numero_puertas = numero_puertas
        self.cantidad_asientos = cantidad_asientos
        self.velocidad_maxima = velocidad_maxima
        self.color = color
        
        # 1. Renombramos el atributo interno con un guion bajo (convención de "privado")
        self._velocidad_actual = 0  
        
    @property
    def velocidad_actual(self):
        """Obtiene la velocidad actual del automóvil."""
        return self._velocidad_actual

    @velocidad_actual.setter
    def velocidad_actual(self, nuevo_valor):
        """Valida y establece la nueva velocidad."""
        if nuevo_valor < 0:
            print("Error: La velocidad no puede ser negativa. Se mantendrá la velocidad actual.")
        elif nuevo_valor > self.velocidad_maxima:
            print(f"Error: La velocidad no puede exceder la máxima ({self.velocidad_maxima} km/h).")
            self._velocidad_actual = self.velocidad_maxima
        else:
            self._velocidad_actual = nuevo_valor


    def acelerar(self, incremento):
        # Al sumar a self.velocidad_actual, Python llamará automáticamente al setter
        self.velocidad_actual += incremento

    def desacelerar(self, decremento):
        self.velocidad_actual -= decremento

    def frenar(self):
        self.velocidad_actual = 0

    def calcular_tiempo_llegada(self, distancia):
        if self.velocidad_actual == 0:
            print("El automóvil debe estar en movimiento")
            return 0
        return distancia / self.velocidad_actual


if __name__ == "__main__":
    auto1 = Automovil("Ferrari", 2023, 2.0, "Gasolina", 
                      "Compacto", 4, 5, 200, "Rojo")
    
    # 1. Asignación normal 
    auto1.velocidad_actual = 50
    print(f"Velocidad tras asignación correcta: {auto1.velocidad_actual} km/h")
    
    # 2. Intento de asignar un valor negativo (dispara la validación del setter)
    print("\nIntentando asignar velocidad negativa (-20):")
    auto1.velocidad_actual = -20
    print(f"Velocidad actual: {auto1.velocidad_actual} km/h")
    
    # 3. Intento de superar la velocidad máxima (dispara la validación del setter)
    print("\nIntentando asignar velocidad excesiva (250):")
    auto1.velocidad_actual = 250
    print(f"Velocidad actual: {auto1.velocidad_actual} km/h")
    tiempo = auto1.calcular_tiempo_llegada(120)
    print(f"El tiempo de llegada estimado para recorrer 120km es de {tiempo} horas")