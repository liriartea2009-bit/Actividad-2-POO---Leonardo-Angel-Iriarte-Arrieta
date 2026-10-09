from enum import Enum

# 1. Definición del enumerado para el tipo de planeta
class TipoPlaneta(Enum):
    GASEOSO = 1
    TERRESTRE = 2
    ENANO = 3

class Planeta:
    # Constructor de la clase
    def __init__(self, nombre: str, cantidad_satelites: int, masa: float, volumen: float, 
                 diametro: int, distancia_sol: int, tipo: TipoPlaneta, es_observable: bool):
        self.nombre = nombre
        self.cantidad_satelites = cantidad_satelites
        self.masa = masa
        self.volumen = volumen
        self.diametro = diametro
        self.distancia_sol = distancia_sol
        self.tipo = tipo
        self.es_observable = es_observable

    # 4. Método especial __str__ en lugar de imprimir()
    def __str__(self):
        # Retornamos un string formateado (f-string) con múltiples líneas
        return (f"Nombre del planeta = {self.nombre}\n"
                f"Cantidad de satélites = {self.cantidad_satelites}\n"
                f"Masa del planeta = {self.masa}\n"
                f"Volumen del planeta = {self.volumen}\n"
                f"Diámetro del planeta = {self.diametro}\n"
                f"Distancia al sol = {self.distancia_sol}\n"
                f"Tipo de planeta = {self.tipo.name}\n"
                f"Es observable = {self.es_observable}")

    # 5. Método para calcular la densidad
    def calcular_densidad(self):
        return self.masa / self.volumen

    # 6. Método para determinar si es un planeta exterior
    def es_planeta_exterior(self):
        limite = 3.4 * 149597870
        return self.distancia_sol > limite

# 7. Bloque principal
if __name__ == "__main__":
    planeta1 = Planeta("Tierra", 1, 5.9736e24, 1.08321e12, 12742, 150000000, TipoPlaneta.TERRESTRE, True)
    
    print(planeta1)
    
    print(f"Densidad del planeta = {planeta1.calcular_densidad()}")
    print(f"Es planeta exterior = {planeta1.es_planeta_exterior()}")
    
    print("\n---") # Separador
    
    planeta2 = Planeta("Júpiter", 79, 1.899e27, 1.4313e15, 139820, 750000000, TipoPlaneta.GASEOSO, True)
    
    print(planeta2)
    print(f"Densidad del planeta = {planeta2.calcular_densidad()}")
    print(f"Es planeta exterior = {planeta2.es_planeta_exterior()}")