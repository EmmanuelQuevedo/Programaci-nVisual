#CLASE
class Directorio:

    #ATRIBUTOS
    def __init__(self, nombre, apellidos, edad):
       self.nombre = nombre
       self.apellidos = apellidos
       self.edad = edad 
       
    #METODOS
    
    def presentar(self):
        print(f'Mi nombre es {self.nombre} {self.apellidos}, tengo {self.edad} años')
        print("\n")
        print("Estos son los servicios disponibles:")
    
    def Solicitar(self):
        print("\n")
        print("¿Que servicio desea solicitar?")
        print("\n")
        print('''Servicio Medico: 1           Policia: 2                   Salir: 3''')
        print("\n")

        Solicitud = int(input())

        if Solicitud == 1:
            persona2.Ambulancia()
        
        elif Solicitud == 2:
            persona3.Patrulla()

        else:
            pass

#CLASE HIJA
class Doctor(Directorio):

    #ATRIBUTOS
    def __init__(self, nombre, apellidos, edad, cedulapro, especialidad):
        super().__init__(nombre, apellidos, edad)
        self.__cedulapro = cedulapro
        self.especialidad = especialidad

    #Setter
    def setCedula(self,cedulapro):
        self.__cedulapro = cedulapro
    
    #Getter
    def getCedula(self):
        return self.__cedulapro

    #METODOS
    def presentar(self):
        print(f'Doctor: {self.nombre} {self.apellidos}\n Edad: {self.edad}\n Cedula: {self.__cedulapro}\n Especialidad: {self.especialidad}\n')

    def Ambulancia(self):
        print("La ambulancia está en camino")

            
#CLASE HIJA 2
class Policia(Directorio):

    #ATRIBUTOS
    def __init__(self, nombre, apellidos, edad, cargo, Numplaca):
        super().__init__(nombre, apellidos, edad)
        self.cargo = cargo
        self.__Numplaca = Numplaca
    
    #Setter
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setApellido(self, apellidos):
        self.apellidos = apellidos

    
    def setNumPlaca(self,Numplaca):
        self.__Numplaca = Numplaca
    
    #Getter
    def getNombre(self):
        return self.nombre 
    
    def getApellido(self):
        return self.apellidos 
    
    def getNumPlaca(self):
        return self.__Numplaca
        
    #METODOS
    def presentar(self):
        print(f'Nombre: {self.nombre} {self.apellidos}\n Edad: {self.edad}\n Cargo: {self.cargo}\n Numero de Placa: {self.__Numplaca}\n')


    def Patrulla(self):
        print("Se ha enviado una unidad a su localizacion")

#INICIO    
print("\n")
persona1 = Directorio("Don Eurelio", "Sanchez Mondragon", 60)
persona1.presentar()
print('-------------------------------------------------------------')
print("\n")
print("SERVICIO MEDICO:")
print("\n")

#DATOS DEL SERVICIO MEDICO
persona2 = Doctor("Valdemar", "Perez Orozco", 65, "PCE273", "Medico Cirujano") #Instanciar
persona2.presentar()
print('.........................................................')
print("\n")

#DATOS DE LA POLICIA
print("POLICIA:")
print("\n")
persona3 = Policia("Emmanuel", "Quevedo Cuevas", 19, "Comisario", "640914")#Instanciar
persona3.presentar()
print("\n")
persona3.getNombre()
persona3.setNombre("Monserrat")
persona3.getNumPlaca()
persona3.setNumPlaca("789900")
persona3.getApellido()
persona3.setApellido("Flores Salado")
persona3.presentar()
print('.........................................................')
persona1.Solicitar()
