class Empleado:
    def __init__(self,nombre,edad,salario):
        self.nombre=nombre
        self.edad=edad
        self.salario=salario

    def incremento(self):
        if self.edad<18:
            return f'{self.nombre} usted no tiene edad para trabajar tiene solo {self.edad} años'
        elif 18<=self.edad <=50:
            return f'{self.nombre} su salario base es de: {self.salario} y tiene un aumento del 5%, queda en: {self.salario*(1+5/100)}'
        elif 51<=self.edad <=60:
            return f'{self.nombre} su salario base es de: {self.salario} y tiene un aumento del 10%, queda en: {self.salario*(1+10/100)}'
        else:
            return f'{self.nombre} su salario base es de: {self.salario} y tiene un aumento del 15%, queda en: {self.salario*(1+15/100)}'

e1=Empleado('clara',16,1000)
e2=Empleado('mercedes',45,1000)
e3=Empleado('alfredo',55,1000)
e4=Empleado('liliana',70,1000)

print(e1.incremento())
print(e2.incremento())
print(e3.incremento())
print(e4.incremento())