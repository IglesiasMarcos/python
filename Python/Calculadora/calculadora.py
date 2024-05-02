import inflect

def obtener_nombre_numero(numero):
    p = inflect.engine()
    return p.number_to_words(numero)

def suma(a, b):
    resultado = a + b
    resultado_textual = obtener_nombre_numero(resultado)
    return f"{obtener_nombre_numero(a)} más {obtener_nombre_numero(b)} es {resultado} ({resultado_textual})"

def resta(a, b):
    resultado = a - b
    resultado_textual = obtener_nombre_numero(resultado)
    return f"{obtener_nombre_numero(a)} menos {obtener_nombre_numero(b)} es {resultado} ({resultado_textual})"

def multiplicacion(a, b):
    resultado = a * b
    resultado_textual = obtener_nombre_numero(resultado)
    return f"{obtener_nombre_numero(a)} por {obtener_nombre_numero(b)} es {resultado} ({resultado_textual})"

def division(a, b):
    if b != 0:
        resultado = a / b
        resultado_textual = obtener_nombre_numero(resultado)
        return f"{obtener_nombre_numero(a)} dividido por {obtener_nombre_numero(b)} es {resultado} ({resultado_textual})"
    else:
        return "Error: No se puede dividir por cero."

def calculadora():
    print("Bienvenido a la calculadora")
    while True:
        print("Seleccione la operación:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")

        opcion = input("Ingrese el número de la operación deseada (1/2/3/4/5): ")

        if opcion == '5':
            print("Gracias por usar la calculadora. ¡Hasta luego!")
            break

        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
        except ValueError:
            print("Error: Ingrese números válidos.")
            continue

        if opcion == '1':
            print(suma(num1, num2))
        elif opcion == '2':
            print(resta(num1, num2))
        elif opcion == '3':
            print(multiplicacion(num1, num2))
        elif opcion == '4':
            print(division(num1, num2))
        else:
            print("Opción no válida. Por favor, seleccione una operación válida.")

# Ejecutar la calculadora
calculadora()
