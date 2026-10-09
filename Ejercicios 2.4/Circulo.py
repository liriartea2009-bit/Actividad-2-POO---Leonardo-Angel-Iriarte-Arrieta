import math

class Circulo:
    def __init__(self, radio: float):
        self.radio = radio
        
    def calcular_area(self):
        return math.pi * (self.radio ** 2)
        
    def calcular_perimetro(self):
        return 2 * math.pi * self.radio
        
    def imprimir(self):
        print("=== CÍRCULO ===")
        print(f"Radio: {self.radio} cm")
        print(f"Área: {self.calcular_area()} cm²")
        print(f"Perímetro: {self.calcular_perimetro()} cm\n")