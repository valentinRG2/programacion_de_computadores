#NIVEL 1- funciones sin parametros ni retorno
def edad():
    años=input('ingrese su edad: ')
    print('Tu tienes',años,'años')

edad()
#-------------------------------------------
def suma():
    total=0
    for i in range(2):
        num=int(input('ingrese un numero: '))
        total=total+num
    print('la suma de los numeros da:',total)

suma()
#-------------------------------------------
import random
num_corecto=random.randint(1,100)
def num_aleatorio():
    num=0
    while num !=num_corecto:
        num=int(input('ingrese un numero de 1 a 100: '))
        if num==num_corecto:
            print('!felicitaciones¡',num_corecto,'era el numero')

num_aleatorio()
#-------------------------------------------
def cont_vocales():
    frase=input('ingrese su frase: ').lower()
    contador=0
    for i in frase:
        if i in 'aeiou':
            contador=contador+1
    print('la frase: ', frase,'tiene',contador,'vocales')

cont_vocales()
#-------------------------------------------
#NIVEL 2-funciones con parametros pero sin retorno
def palindromo(palabra):
    palabra=palabra.lower()
    if palabra==palabra[::-1]:
        return True
    else:
        return False
    
print(palindromo('ana'))
print(palindromo('banana'))
#-------------------------------------------
def calcular_potencia(a,b):
    potencia=a**b
    print('el resulado es:',potencia)

calcular_potencia(2,13)
#-------------------------------------------
def calcular_media(lista):
    suma=0
    for i in lista:
        suma=suma+i
    cantidad=len(lista)
    media=suma/cantidad
    print('la media es:',media)

calcular_media([2,5,6,7,8])
#-------------------------------------------
#NIVEL 3-funciones con parametros y retorno
def invertir_cadena(cadena):
    invertida=cadena[::-1]
    return invertida
cadena_invertida=invertir_cadena('cadena invertida')
print(cadena_invertida)
#-------------------------------------------
def calcular_area(radio,altura):
    a_cilindro=(2*3.1416*radio**2+2*3.1416*radio*altura)
    return a_cilindro

area=calcular_area(3,5)
print('el area es:',area)
#-------------------------------------------
def buscar_palabra(cadena,palabra):
    return palabra.lower() in cadena.lower()

buscador=buscar_palabra('bienvenidos amigos de poco pelo de pelo pobre y pelo casi inexistente','Pobre' )
print(buscador)
#-------------------------------------------
#NIVEL 4-funciones con multiples parametros y retornos
def promedio(notas):
    suma=0
    for i in notas:
        suma=suma+i
    cantidad=len(notas)
    return suma/cantidad

promedio_notas=promedio([4,5,3.7,4.3,2.7,4.4])
print(promedio_notas)
#-------------------------------------------
def multiplicar_lista(lista,num):
    n_lista=[]
    for i in lista:
        n_num=num*i
        n_lista.append(n_num)
    return n_lista

lista_multi=multiplicar_lista([2,4,7,5,9,0],3)
print(lista_multi)
#-------------------------------------------
def mayor_de_varios(nums):
    num_mayor=0
    for i in nums:
        if i >num_mayor:
            num_mayor=i
    return num_mayor

mayor=mayor_de_varios([2,3,4,5,6,8,10,9])
print(mayor)
#-------------------------------------------
def calcular_mediana(lista):
    nueva_lista=lista.sort()
    n=len(lista)
    medio=n//2
    if n%2==1:
        return lista[medio]
    else:
        return (lista[medio-1]+lista[medio]/2)

mediana=calcular_mediana([5, 2, 9, 1, 7])
print(mediana)
#-------------------------------------------
def contar_ocurrencias(cadena, palabra):
    cantidad=cadena.count(palabra)
    return cantidad

contar=contar_ocurrencias('buenos dias, buenas tardes y buenas noches','buenas')
print(contar)