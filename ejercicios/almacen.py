class Dispositivo:
    def __init__(self,marca,nombre,ram,almacenamiento,color,precio_compra):
        self.marca=marca
        self.nombre=nombre
        self.ram=ram
        self.alamacenamiento=almacenamiento
        self.color=color
        self.precio_compra=precio_compra

    def precio_venta(self):
        venta=self.precio_compra*1.7
        return f'{venta}$ dolares'
    
    def informacion(self):
        return f'marca: {self.marca}, nombre: {self.nombre}, ram: {self.ram}, almacenamiento: {self.alamacenamiento}, color: {self.color}, precio de venta: {self.precio_venta()}'

class Celular(Dispositivo):
    def __init__(self, marca, nombre, ram, almacenamiento, color, precio_compra):
        super().__init__(marca, nombre, ram, almacenamiento, color, precio_compra)

class Computador(Dispositivo):
    def __init__(self, marca, nombre, ram, almacenamiento, color, precio_compra):
        super().__init__(marca, nombre, ram, almacenamiento, color, precio_compra)

class Tablet(Dispositivo):
    def __init__(self, marca, nombre, ram, almacenamiento, color, precio_compra):
        super().__init__(marca, nombre, ram, almacenamiento, color, precio_compra)

celular=Celular('iphone','iphone 17 pro','8GB','1 terabyte','rosado',600)
print(celular.informacion())