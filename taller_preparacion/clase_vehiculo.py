class Vehiculo:
    def __init__(self,marca,modelo,placa):
        self.marca=marca
        self.modelo=modelo
        self.__placa=placa

    def informacion(self):
        return f'vehiculo Marca: {self.marca}, Modelo: {self.modelo}, Placa: {self.__placa}'

    def soat(self,soat_al_dia):
        if soat_al_dia==True:
            return f'Soat al dia 👍'
        else:
            return f'Soat vencido👎'

class Moto(Vehiculo):
    def __init__(self, marca, modelo, placa,cilindraje):
        super().__init__(marca, modelo, placa)
        self.cilindraje=cilindraje

    def es_alto_cilindraje(self):
        if self.cilindraje >=500:
            return f'es alto cilindraje'
        else:
            return f'no es alto cilindraje'

class Carro(Vehiculo):
    def __init__(self, marca, modelo, placa,kilometraje):
        super().__init__(marca, modelo, placa)
        self.kilometraje=kilometraje

    def alto_kilometraje(self):
        if self.kilometraje >150000:
            return f'alto kilometraje'
        else:
            return f'bajo kilometraje'

moto=Moto('kawasaki','Ninja 500/ZX-10R','HTF973',200)
print(moto.informacion(),',',moto.es_alto_cilindraje(),',',moto.soat(False))

carro=Carro('toyota','Corolla Cross','BOF347',200000)
print(carro.informacion(),',',carro.alto_kilometraje())