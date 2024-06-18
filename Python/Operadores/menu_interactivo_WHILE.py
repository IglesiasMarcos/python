print('*** Sistema de administración de cuentas ***')

salir = False
while not salir:
    print(f'''Menu:
        1.Crear Cuenta
        2.Eliminar Cuenta
        3.Salir''')
    opcion= int(input('Elije una opcíon:'))
    if opcion ==1:
        print('Creando tu cuenta...\n')

    elif opcion ==2:
        print('Estamos Eliminando Tu Cuenta..\n')

    elif opcion ==3:
        print('Saliendo, hasta Luego...\n')
    else:
        print('Opcion Invalida, Seleccione otra opcion..\n')