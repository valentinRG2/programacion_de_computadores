
#1--------------------------------------------------
class Animal:
    edad='2 años'
    peso='2kg'
    agresivo='no'
    raza='criollo'

    def dice_miau(self):
        self.Miau=True
        return 'si dice miau'
    def le_gusta_comer(self):
        self.Comer=True
        return 'le gusta mucho'

gato=Animal()
print('el gato tiene',gato.edad)
print('al gato',gato.le_gusta_comer(),'comer')

class Vehiculo:
    marca='kawasaki'
    ruedas=2
    color='verde'
    cilindraje='250 cc'
    marca_carro='toyota'
    ruedas_carro=4
    color_carro='blanco'
    kilometraje='200000'

    def prender(self):
        self.Prender=True
        return 'prendio brrrmmm'
    def soat(self):
        self.Soat='soat al dia'
        return self.Soat

moto=Vehiculo()
print('la moto es',moto.marca)
print('el soat de la moto:',moto.soat())

carro=Vehiculo()
print('el carro es',carro.marca_carro)
print('soat del carro:',carro.soat())

class Comida:
    origen='medellin'
    ingredientes='arroz,frijoles,carne molida, chicharron,chorizo,huevo,aguacate y arepa'
    cantidad_ingredientes=8

    def rica(self):
        self.Rica=True
        return 'muy rica'
    def tiene_pollo(self):
        self.Pollo=False
        return 'no tiene pollo'

bandeja_paisa=Comida()
print('la bandeja paisa es de',bandeja_paisa.origen)
print('la bandeja paisa',bandeja_paisa.tiene_pollo())

class Arbol:
    altura='28 metros'
    edad='8 años'
    color_hojas='verde oscuro'
    fruto='Piñas/Estróbilos'

    def crecimiento(self):
        self.Crecimiento=True
        return 'esta creciendo'
    def frutos(self):
        self.Frutos=True
        return 'produce frutos'

pino=Arbol()
print('el pino mide',pino.altura)
print('el pino',pino.frutos())

class Libro:
    titulo='cincuenta años de soledad'
    paginas=300
    genero='novela'
    precio='100000'

    def recomendacion(self):
        self.Recomendado=True
        return 'te lo recomiendo'
    def regalar_novela(self):
        self.Regalar=True
        return 'regalado'
    
novela=Libro()
print('el nombre de la novela es',novela.titulo)
print('es muy bueno',novela.recomendacion())

class Pelicula:
    estudio='pixar'
    tema='comedia infantil'
    fecha_estreno='21 de diciembre de 2001'
    director='Pete Docter'

    def ver_cine(self):
        self.Cine=True
        return 'se puede ver en el cine'
    def reproduccion(self):
        self.Reproduciendo=True
        return 'se esta reprooduciendo'

monsters_inc=Pelicula()
print('se estreno el',monsters_inc.fecha_estreno)
print('monsters inc',monsters_inc.ver_cine())

class Dispositivo:
    diseño='ligero'
    pantalla='15 pulgadas'
    ram='16 GB'
    procesador='inter core i5'

    def encendido(self):
        self.Prendido=True
        return 'equipo prendido'
    def abrir_programa(self):
        self.Programa=True
        return 'programa abierto'

portatil=Dispositivo()
print('el portatil tiene',portatil.ram,'de ram')
print('abriendo...',portatil.abrir_programa())

class Servicio:
    empresa='ESSA'
    costo_kwh = 800
    voltaje = '110V'
    tipo_servicio = 'prepago'

    def cortar_servicio(self):
        self.Cortar=False
        return 'no se corta el servicio'
    def calcular_factura(self):
        self.Factura=True
        return ' su factura es de .....'

energia=Servicio()
print('su servicio es',energia.tipo_servicio)
print(energia.calcular_factura())

class Empaque:
    meterial='plastico'
    color = 'marron'
    peso = 'ligero'
    tamaño = 'mediano'

    def cerrado(self):
        self.Sellado=True
        return 'la caja esta cerrada'
    def abierto(self):
        self.Abierto=True
        return 'la caja esta abierta'

caja=Empaque()
print('el material de la caja es',caja.meterial)
print(caja.cerrado())

class Persona:
    nombre='pepito perez'
    universidad='UNAB'
    semestre='quinto semestre'
    carrera='ingenieria de sistemas'

    def pago_semestre(self):
        self.Pago=False
        return 'tiene que pagar la matricula'
    def horario(self):
        self.Horario=True
        return 'este es su horario....'

estudiante = Persona()
print(estudiante.nombre)
print(estudiante.pago_semestre())
