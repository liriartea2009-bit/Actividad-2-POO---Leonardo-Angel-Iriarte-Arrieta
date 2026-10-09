class Cuadrado:
    def __init__(self, lado: float):
        self.lado = lado
    def calcular_area(self) -> float:
        return self.lado ** 2       
        
    def calcular_perimetro(self):
        return 4 * self.lado
        
    def imprimir(self):
        print("=== CUADRADO ===")
        print(f"Lado: {self.lado} cm")
        print(f"Área: {self.calcular_area()} cm²")
        print(f"Perímetro: {self.calcular_perimetro()} cm\n")