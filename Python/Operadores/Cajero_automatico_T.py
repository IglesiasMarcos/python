print('*** Cajero Automatico T ***')
saldo = 5000  # Saldo inicial
Salir= False
while not Salir:
    print(f'''Operaciones que puedes realizar:
         1.Consultar saldo
         2.Retirar
         3.Depositar
         4.Salir''')
    opcion=int(input('Elije una opcion:'))

    if opcion == 1:
        print(f"*** Tu Saldo actual es : ${saldo:.2f} ***\n")
    elif opcion == 2:
        retiro= float(input('Ingrese el monto a Retirar:'))
        #Validacion
        if retiro <= saldo:
            saldo -= retiro # saldo = saldo - retiro
            print(f'*** Tu nuevo saldo es: ${saldo:.2f} ***')
        else:
            print(f'***  Fondos insuficientes. Por favor, intente con un monto menor. ***\n')
    elif opcion == 3:
        deposito = float(input('Ingrese el monto a Depositar:' ))
        saldo += deposito # saldo = saldo + desposito
        print(f"*** Depósito exitoso. Su saldo actual es: ${saldo:.2f} ***\n")
    elif opcion == 4:
        print('Saliendo...Gracias por utilizar nuestros servicios!\n')
    else:
        print('** Operacion Invalida **\n')
