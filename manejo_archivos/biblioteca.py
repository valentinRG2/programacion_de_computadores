class Libro:
    def __init__(self,titulo,autor):
        self.titulo=titulo
        self.autor=autor

    def __str__(self):
        return f'Titulo: {self.titulo}. Autor: {self.autor}.'

class Biblioteca:
    def __init__(self,nombre):
        self.nombre=nombre
        self.libros=[]

    def agregar(self,libro_nuevo):
        self.libros.append(libro_nuevo)

    def listar(self):
        for libro in self.libros:
            print(libro)

    def guardar(self):
        with open('libros.txt','w') as archivo:
            for libro in self.libros:
                archivo.write(f'{libro.titulo},{libro.autor}\n')

    def leer(self):
        with open('libros.txt','r') as archivo:
            for linea in archivo:
                datos=linea.strip().split(',')

                if len(datos)==2:
                    nuevo=Libro(datos[0],datos[1])
                    self.agregar(nuevo)
        print("¡Datos cargados desde el archivo!")



biblioteca= Biblioteca('biblioteca')

l1 = Libro("Cien años de soledad", "Gabriel García Márquez")
l2 = Libro("Rayuela", "Julio Cortázar")
print('----------Biblioteca de libros----------')
biblioteca.leer()
biblioteca.listar()
print('----------------------------------------')

