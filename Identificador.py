
class Persona:
    #Propiedades/Atributos
    #constructor: es el bloque para signar las propiedades del objeto
    #init permite inicializar los valores del constructor
    def __init__(self, nombre, edad, DNI):
        self.nombre = nombre
        self.edad = edad
        self.DNI = DNI

    
    #Metodos
    def mostrar(self):
        print(f' Nombre: {self.nombre}\n Edad: {self.edad}\n DNI: {self.DNI}\n ') #Instanciar

    def EsMayorDeEdad(self):
        print("¿LA PERSONA ES MAYOR DE EDAD?")
        if self.edad >= 18:
            return True
        
        else:
            return False

print("\n")
persona1 = Persona ("Monserrat Flores Salado", 19, 21560028)
persona1.mostrar()

print(persona1.EsMayorDeEdad())