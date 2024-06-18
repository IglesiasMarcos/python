#proyecto calculadora
print("*** CALCULADORA en python ***")
Salir= False
while not Salir:
    print(f'''Operaciones que puedes realizar:
         1.Suma
         2.Resta
         3.Multipliclación
         4.Division 
         5.Salir''')
    opcion=int(input('Elije una opcion:'))
    #if 1 <= opcion <=4:     menor que o mayor que .
    if opcion == 1:  #SUMA
       suma1 = int(input(f"Que numero quieres Sumar? "))
       suma2 = int(input(f"{suma1} +  "))
       respuesta1= suma1 + suma2
       print(f"la suma de {suma1} + {suma2} es : {respuesta1} \n")
    elif opcion == 2:   #RESTA
        resta1 = int(input(f"Que numero quieres Restar? "))
        resta2 = int(input(f"{resta1} -  "))
        respuesta2 = resta1 - resta2
        print(f"la resta de {resta1} - {resta2} es : {respuesta2} \n")
    elif opcion == 3:      #MULTIPLICAR
        mult1 = int(input(f"Que numero quieres Multiplicar? "))
        mult2 = int(input(f"{mult1} X  "))
        respuesta3 = mult1 * mult2
        print(f"la multiplicación de {mult1} X {mult2} es : {respuesta3} \n")
    elif opcion == 4:      #DIVISION
        divi1 = float(input(f"Que numero quieres dividir? "))
        divi2 = float(input(f"{divi1} %  "))
        respuesta4 = divi1 / divi2
        print(f"la division de {divi1} % {divi2} es : {respuesta4:.2f} \n")
    elif opcion == 5:   #SALIR
        print('Saliendo de nuestra Calculadora, Hasta Pronto!\n')
    else:
        print('** Operacion Invalida **\n')