class Perro:
    # Atributos de la clase Perro
    especie = "canis lupus familiaris"
    # Constructor de la clase Perro
    def __init__ (self,nombre,raza = "Caramelo",edad = 0):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        
    #Metodo para imprimir los datos del Perro
    def imprimirDatos(self):
        print("nombre: ", self.nombre)
        print("raza: ", self.raza)
        print("edad: ", self.edad)
        print ("Especie",self.especie)
        
def main():
    # CRear un objeto de la clase Perro
    perro1 = Perro("firulais", "labrador",5)
    perro1.imprimirDatos()
    perro2 = Perro("rex","pastor Aleman",3)
    perro2.imprimirDatos()
    print("informacion de perro 2: ",perro2.nombre,perro2.raza,perro2.edad)
    perro3 = Perro("Max","Bulldog",2)
    perro3.imprimirDatos()
    perro4 = Perro("Dante")
    perro4.edad = 4
    perro4.imprimirDatos()
    perro2.raza = "pastor belga"
    perro2.imprimirDatos()
    perro5 = Perro("raya","Siames",1)
    perro5.especie = "Felis catus"
    perro5.imprimirDatos()
        
if __name__ == "__main__":
    main()