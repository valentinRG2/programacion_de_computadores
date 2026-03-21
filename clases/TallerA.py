class Persona:
    def __init__(self, nombre, edad):
        self.__edad=edad
        self.__nombre=nombre
        # debe devolver "Hola, soy <nombre> y tengo <edad> años  
    def saludar(self):
        return f'Hola,soy {self.__nombre} y tengo {self.__edad} años'

persona1=Persona('carlos',30)
print(persona1.saludar())