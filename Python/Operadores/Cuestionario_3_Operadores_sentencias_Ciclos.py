#Cual es el valor de X?
calculo = 10 < 100
print(f"rta tarea 1: {calculo}\n")
#True con inicial mayus



#TAREA DE TRUE  rta correcta : true
calculo = (5<10) & (10<20)   #(&&= mal , AND=MAL)
calculo = (5<10) and (10<20)    #(correcto and, &)
print(f"rta tarea 2:{calculo}\n")



# VERDADERO O FALSO , SI "n" es igual a 3?  rta: verdadero
n=3
if not(n <= 100 and n >= 10):
  print("rta tarea 3: Verdadero\n")
else:
  print("rta tarea 3 : Falso\n")

#Dado que n, que vale 3, no es mayor que 10, regresa falso,
# y debido a que estamos usando el operador and, si cualquiera
# de las opciones es falsa, entonces toda la expresion regresa falso,
# pero debido a que toda la expresión está envuelta por el operador not,
# entonces invierte el valor a verdadero,
# y por lo tanto, entra a la opción de "Verdadero"