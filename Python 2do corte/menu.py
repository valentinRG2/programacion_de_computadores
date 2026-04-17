def mostrar_menu():
    print('===== MENÚ =====')
    opcion=int(input('1.ingresar datos \n2.mostrar datos\n3.salir\ningrese el numero de su opcion: '))
    if opcion < 1 or opcion > 3:
        return 'opcion no valida'
    else:
        return opcion

print(mostrar_menu())