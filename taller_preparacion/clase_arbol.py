class Arbol:
    def __init__(self,altura,edad,fruto):
        self.altura=altura
        self.__edad=edad
        self.fruto=fruto

    def dar_fruto(self):
        if self.fruto==True:
            return f'este arbol da fruto'
        else:
            return f'este arbolo no sa fruto'

    def arbol_joven(self):
        if self.__edad <=5:
            return f'es un arbol joven'
        else:
            return f'es un arbol viejo'

class Pino(Arbol):
    def __init__(self, altura, edad, fruto,tipo_hoja):
        super().__init__(altura, edad, fruto)
        self.tipo_hoja=tipo_hoja

    def clima_del_arbol(self,clima):
        if clima<=15 and clima>=10:
            return f'clima perfecto para el pino'
        else:
            return f'el clima no es el ideal para el pino'

pino=Pino(15,7,True,'acicular')

print('Pino:',pino.clima_del_arbol(20),',',pino.dar_fruto(),',',pino.arbol_joven(),', tipo de hoja:',pino.tipo_hoja)
