"""
Crea un clase persona con los siguientes atributos: nombre,edad,genero y nacionalidad,
agrega un metodo par imprimir los datos de la persona y otro metodo para calcular el año
de nacimiento  de la persona.
Crea un objeto de la clase Persona y utiliza los metodos  para mostrar su informacion y
calcular su año de nacimiento
"""
import datetime

class Persona:
    
    def __init__(self, nombre,edad,genero,nacionalidad = "Mexico"):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.nacionalidad = nacionalidad
        
    def informacion(self):
        print("------Información------")
        print(f"{self.nombre} ({self.genero})")
        print(f"Edad: {self.edad} años")
        print(f"Nacionalidad: {self.nacionalidad}")
        
    def calcularNacimiento(self):
        year =datetime.date.today().year
        return year - self.edad
    
def main():
    objPersona = Persona("Julian Antonio",16,"Masculino")
    objPersona.informacion()
    print(f"Año de nacimiento: {objPersona.calcularNacimiento()}")
    
if __name__ == "__main__":
    main()