class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def calcular_area(self):
        return self.base * self.altura
        
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)
        
    def imprimir(self):
        print("=== RECTÁNGULO ===")
        print(f"Base: {self.base} cm")
        print(f"Altura: {self.altura} cm")
        print(f"Área: {self.calcular_area()} cm²")
        print(f"Perímetro: {self.calcular_perimetro()} cm\n")