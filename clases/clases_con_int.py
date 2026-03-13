class Persona:
    def __init__(self,nombre):
        self.nombre=nombre
    
class Estudiante(Persona):
    def __init__(self, nombre,carrera):
        super().__init__(nombre)
        self.carrera=carrera

alumno=Estudiante('pepito','derecho')
print(alumno.nombre)
print(alumno.carrera)


#-------------------------------------------------


class Estudiante:
    def __init__(self,nombre,nota):
        self.__nombre=nombre
        self.__nota=4.4
    def get_nota(self):
        return self.__nota
    def set_nota(self,nueva_nota):
        if 0<=nueva_nota<=5:
            self.__nota=nueva_nota
        else:
            print('nota invalida')

estudiante=Estudiante('pepito',4.4)
print(estudiante.get_nota())
estudiante.set_nota(3.3)
print(estudiante.get_nota())

#-----------------------------------



class Personaje:
    def __init__(self, nombre, nivel=1, energia=100):
        self.nombre = nombre
        self.nivel = nivel
        self.energia = energia
    def atacar(self):
        self.energia -= 10
        print('ataque')
    def descansar(self):
        self.energia = 100
        print('energia al 100')
    def mostrar_estado(self):
        print(f"Nivel: {self.nivel}")
        print(f"Energía: {self.energia}")
    def subir_nivel(self):
        self.nivel += 1
        print("subio de nivel a",self.nivel)

jugador = Personaje('steve')
jugador.mostrar_estado()
jugador.atacar()
jugador.subir_nivel()
jugador.mostrar_estado()