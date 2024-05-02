print("***Revision valor positivo***")
numero = int(input('Que numero quieres ingresar?'))
if numero > 0:
    print(f'es positivo: +{numero}')
elif numero < 0:
    print(f'es negativo: {numero}')
else:
    print(f"es cero = {numero}")
