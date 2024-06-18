print('*** Operador logico or ***')
a1 = True
a2 = False
# El operador or regresa True si cualquiera de los operadores es verdadero
resultado= a1 or a2

print(f"Resultado {a1} or {a2} es: {resultado} ")

# Marcos quiere ir a ver el partido el martes pero:
print('\nHay partido el martes. (EJERCICIO)')
vacaciones = False
dia_de_descanso = True
if vacaciones or dia_de_descanso :
    print('Marcos puede ir al partido el martes')
else:
    print('Marcos tiene que trabajar el martes,no puede ir al partido.')