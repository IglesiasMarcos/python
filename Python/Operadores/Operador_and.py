print("*** Operador Logico and ***")
a1 = True
a2 = False
# Aplicamos el operador and
resultado = a1 and a2
#El operado and si cualquiera de sus operandos es falso, toda la expresión sera falsa.
print(f"resultado {a1} and {a2}: {resultado}")

# Ejemplo if else con operador AND
llueve = False
nublado = False
print(f"\n*** Revision del clima")
if llueve and nublado:
    print('LLevar campera e paraguas, llueve y esta nublado')
elif llueve:
    print('llevar paraguas,esta lloviendo')
elif nublado:
    print("llevar campera,esta nublado")
else:
    print('puedes salir tranquilamente, esta lindo el dia. disfruta tu dia!')









