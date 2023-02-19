class Persona:

    #Definimos los setters

    def setNombre(self,nombre):
        self.__nombre = nombre
    
    def setEdad(self,edad):
        self.__edad = edad
    
    #Definimos los getters
    
    def getNombre(self):
        return self.__nombre
    
    def getEdad(self):
        return self.__edad
    
    #CONSTRUCTOR
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    #METODOS
    def MostrarPersona(self):
        print(f'Nombre: {self.__nombre}\n Edad: {self.__edad} años\n ') #Instanciar
    
    def EsMayorDeEdad(self):
        print("¿LA PERSONA ES MAYOR DE EDAD?")
        if self.__edad >= 18:
            return True
        
        else:
            return False
    
    def EsMayorQue(self):
        print("¿QUIEN ES MAYOR?")
        if  persona1.__edad > persona2.__edad:
           return print(f'{persona1.__nombre} ES MAYOR QUE {persona2.__nombre} ')
        
        elif persona1.__edad == persona2.__edad:
            return print(f'{persona1.__nombre}  Y  {persona2.__nombre}  SON DE LA MISMA EDAD')
        
        else:
            return print(f'{persona2.__nombre} ES MAYOR QUE {persona1.__nombre} ')
        
            

print("----------------------------------------------------------------------------------")

persona1 = Persona("Monserrat Flores Salado", 20)
persona1.MostrarPersona()
print(persona1.EsMayorDeEdad())

print("----------------------------------------------------------------------------------")


persona2 = Persona("Emmanuel Quevedo Cuevas", 19)
persona2.MostrarPersona()
print(persona2.EsMayorDeEdad())

print("-----------------------------------------------------------------------------------")

print(persona2.EsMayorQue())
print("-----------------------------------------------------------------------------------")

persona1.getNombre()
persona1.getEdad()
persona1.setNombre("Camila Estefania Quevedo Cuevas")
persona1.setEdad(2)
persona1.MostrarPersona()
print(persona1.EsMayorDeEdad())

print("----------------------------------------------------------------------------------")

persona2.getNombre()
persona2.getEdad()
persona2.setNombre("Yapitas Quevedo Flores")
persona2.setEdad(18)
persona2.MostrarPersona()

print(persona2.EsMayorDeEdad())

print("-----------------------------------------------------------------------------------")

print(persona2.EsMayorQue())

print("-----------------------------------------------------------------------------------")





