import math

class TrianguloRectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def calcular_hipotenusa(self):
        return math.sqrt((self.base ** 2) + (self.altura ** 2))
        
    def calcular_area(self):
        return (self.base * self.altura) / 2
        
    def calcular_perimetro(self):
        return self.base + self.altura + self.calcular_hipotenusa()
        
    def determinar_tipo(self):
        hip = self.calcular_hipotenusa()
        if self.base == self.altura and self.altura == hip:
            return "Equilátero"
        elif self.base == self.altura or self.altura == hip or self.base == hip:
            return "Isósceles"
        else:
            return "Escaleno"
            
    def imprimir(self):
        print("=== TRIÁNGULO RECTÁNGULO ===")
        print(f"Base: {self.base} cm")
        print(f"Altura: {self.altura} cm")
        print(f"Hipotenusa: {self.calcular_hipotenusa()} cm")
        print(f"Área: {self.calcular_area()} cm²")
        print(f"Perímetro: {self.calcular_perimetro()} cm")
        print(f"Tipo: {self.determinar_tipo()}\n")