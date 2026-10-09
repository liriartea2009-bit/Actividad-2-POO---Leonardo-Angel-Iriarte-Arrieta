from circulo import Circulo
from rectangulo import Rectangulo
from cuadrado import Cuadrado
from triangulo_rectangulo import TrianguloRectangulo

#En esta sección 2.4 aun no sabía usar el método ___str__

def main():
    print("Ejercicio 2.4 - Estado de un Objeto\n")
    
    c = Circulo(5)
    c.imprimir()
    
    r = Rectangulo(4, 6)
    r.imprimir()
    
    cu = Cuadrado(5)
    cu.imprimir()
    
    t = TrianguloRectangulo(3, 4)
    t.imprimir()

if __name__ == "__main__":
    main()