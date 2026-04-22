def mostrarMenu():
    print('===== MENÚ PRINCIPAL =====')
    print('1. Mostrar números\n2. Sumar números\n3. Validar contraseña\n4.Salir')
    op=int(input('ingrese el numero de su opcion: '))
    return op

op=mostrarMenu()
if op==4:
    print('saliendo del programa...')

while op != 4:
    if op==1:
        num1=int(input('ingrese su numero: '))
        for i in range (1,num1+1):
            print(i)
    
    elif op==2:
        resultado=0
        bucle=1
        while bucle!=0:
            nums=int(input('ingrese el numero a sumar: '))
            if nums==0:
                bucle=0
            else:
                resultado+=nums

        print('el resultado de su suma es: ',resultado)
    
    elif op==3:
        contra_correcta=input('ingrese su contraseña: ')
        contraseña=''
        while contraseña!=contra_correcta:
            contraseña=input('verifique su contraseña: ')
        if contraseña==contra_correcta:
            print('acceso concedido...')


    
    print('\n===== MENÚ PRINCIPAL =====')
    print('1. Mostrar números\n2. Sumar números\n3. Validar contraseña\n4. Salir')
    op = int(input('ingrese el numero de su opcion: ')) 

#REFLEXION 
#1.ENCONTRE QUE SE USAN DEPENDIENDO DE QUE NECESITAMOS HACER
#2.SE USAN EN CASOS DISTINTOS POR QUE EL FOR ES PARA CUANDO SABEMOS EXACTAMENTE CUANTAS VECES VAMOS A EJECUTAR EL PROGRAMA, EL WHILE CUANDO DEPENDE SE UNA CONDICION Y DO-WHILE CUANDO SE DEBE EJCUTAR ALMENOS UNA VEZ
#3.PARA TENER MAS ORGANIZADO EL CODIGO#

