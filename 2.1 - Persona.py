class Persona:
    """
    Modelar el concepto de una persona con nombre, apellido, 
    número de documento y año de nacimiento.
    """
    
    # Constructor 
    def __init__(self, nombre: str, apellido: str, numero_documento: str, año_nacimiento: int):
        self.nombre = nombre
        self.apellido = apellido
        self.numero_documento = numero_documento
        self.año_nacimiento = año_nacimiento
        
    def __str__(self):
        return (f"=== DATOS DE LA PERSONA ===\n"
                f"Nombre: {self.nombre}\n"
                f"Apellido: {self.apellido}\n"
                f"Número de Documento: {self.numero_documento}\n"
                f"Año de Nacimiento: {self.año_nacimiento}\n"
                f"===========================\n")

# Bloque principal que crea dos personas y muestra sus valores
if __name__ == "__main__":
    print("Ejercicio 2.1 - Definición de Clases\n")
    
    # Crear primera persona
    persona1 = Persona("Carlos", "Medrano", "1234567890", 1990)
    print(persona1)
    
    # Crear segunda persona
    persona2 = Persona("Luis", "Salgado", "0987654321", 1995)
    print(persona2)
