class Empaque:
    def __init__(self,material,tamaño,costo):
        self.material=material
        self.tamaño=tamaño
        self.__costo=costo

    def get_costo(self):
        return self.__costo

    def cant_ganancia(self):
            return self.__costo * 0.40

    def precio_venta(self):
        self.venta=self.__costo + (self.__costo * 0.40)

class Caja(Empaque):
    def __init__(self, material, tamaño, costo,fragil):
        super().__init__(material, tamaño, costo)
        self.fragil=fragil

    def detalles(self):
        costo = self.get_costo()
        venta = self.precio_venta()

        if self.fragil:
            return f'Cuidado contenido fragil,material:{self.material} ,tamaño: {self.tamaño} ,costo: {costo} , precio de venta: {self.venta}'
        else:
            return f'Material: {self.material}, tamaño: {self.tamaño}, costo: {costo}, precio de venta: {self.venta}'

class Bolsa(Empaque):
    def __init__(self, material, tamaño, costo,reutilizable):
        super().__init__(material, tamaño, costo)
        self.reutilizable=reutilizable
    def es_reutilizable(self):
        return 'La bolsa es reutilizable ♻️' if self.reutilizable else 'La bolsa no es reutilizable'

caja2 = Caja('carton', 'grande', 4000, True)
print(caja2.detalles())
bolsa = Bolsa('plástico', 'mediana', 500, True)
print(bolsa.es_reutilizable())

