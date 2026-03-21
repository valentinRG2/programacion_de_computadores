class Vehiculo:
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo

    def info(self):
        return f'el vehiculo es marca: {self.marca}, modelo: {self.modelo}'

class Coche(Vehiculo):
    def __init__(self, marca, modelo,puertas):
        super().__init__(marca, modelo)
        self.puertas=puertas
    
    def info(self):
        return f"{super().info()} y tiene {self.puertas} puertas"
    
carro=Coche('toyota','2009','4')
print(carro.info())