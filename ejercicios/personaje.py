class Personaje:
    def __init__(self,nombre,nivel=1,energia=100):
        self.nombre=nombre
        self.nivel=nivel
        self.energia=energia

    def atacar(self):
        self.energia -=10
        return f'!ATAQUE¡, tu energia a bajado a {self.energia}'

    def descansar(self):
        self.energia=100
        return f'!Energia restaurada al {self.energia}¡'

    def subir_nivel(self):
        self.nivel +=1
        return f'felicidades subes de nivel, nuevo nivel: {self.nivel}'

    def estado(self):
        return f'Tu estado actual, nombre: {self.nombre},nivel: {self.nivel},energia: {self.energia}'

avatar=Personaje('steve')
print(avatar.atacar())
print(avatar.atacar(),avatar.subir_nivel())

print(avatar.estado())
