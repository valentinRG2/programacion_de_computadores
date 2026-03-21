#catalogo de libros

class Libro:
    def __init__(self,titulo,autor,codigo,disponible=True):
        self.titulo=titulo
        self.autor=autor
        self.codigo=codigo
        self.disponible=disponible
    
    def __str__(self):
        if self.disponible==True:
            return f'{self.titulo}, estado:disponible'
        else:
            return 'el libro no esta disponible por ahora'
#-------------------------------------------
class Biblioteca:
    def __init__(self):
        self.catalogo=[]
    def agregar_libro(self):
        num=int(input('cuantos libros desea agregar: '))
        for i in range(num):
            titulo_n_libro=input('ingrese el titulo del libro: ')
            autor_n_libro=input('ingrese el autor del libro: ')
            codigo_n_libro=input('ingrese el codigo del libro: ')
            
            n_libro=Libro(titulo_n_libro,autor_n_libro,codigo_n_libro)
            self.catalogo.append(n_libro)
#---------------------------------------------   
    def mostrar_catalogo(self):
        for i in self.catalogo:
            print(i)
#---------------------------------------------
    def prestar_libro(self):
        libro_prestar = input('Qué libro desea llevar: ')
        for libro in self.catalogo: 
            if libro.titulo.lower() == libro_prestar.lower():
                if libro.disponible:
                    libro.disponible = False
                    return f'"{libro.titulo}" está disponible, puede llevárselo.'
                else:
                    return 'Lo sentimos, ese libro ya está prestado.'
        
        return 'Ese libro no se encuentra en nuestro catálogo.'
#---------------------------------------------
    def devolver_libro(self):
        libro_a_devolver = input('¿Qué libro desea devolver?: ')
        
        for libro in self.catalogo:
            if libro.titulo.lower() == libro_a_devolver.lower():
                libro.disponible = True
                return f'Gracias por devolver "{libro.titulo}". Ahora está disponible.'
                
        return 'Ese libro no pertenece a nuestra biblioteca.'
            
libro=Libro('100 años de soledad','pepito perez','3541')
print('titulo:',libro.titulo,',autor:',libro.autor,',codigo:',libro.codigo)
print(libro)
#-------------
biblioteca=Biblioteca()
biblioteca.agregar_libro()
#-------------
print('catalogo de libros:')
biblioteca.mostrar_catalogo()
#-------------
print(biblioteca.prestar_libro())
print(biblioteca.devolver_libro())


