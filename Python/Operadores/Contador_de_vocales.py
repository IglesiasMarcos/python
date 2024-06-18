#declarar la variable
# Agregar el ciclo for
# Imprimir la cantidad de vocales encontradas en la cadena


cadena = "Hola Mundo"
contador_vocales = 0
for caracter in cadena:
    if caracter.lower() in "aeiou":
        contador_vocales += 1
print(contador_vocales)



#Explicación
# Declarar la variable llamada cadena con el valor de "Hola Mundo"
cadena = "Hola Mundo"
# Inicializar un contador para las vocales

contador_vocales = 0
# Ciclo for para recorrer cada caracter de la cadena
for caracter in cadena:

#Este ciclo for recorre cada carácter de la cadena cadena.
# En cada iteración, la variable caracter
# contendrá uno de los caracteres de la cadena.

#Para cada carácter de la cadena, se convierte a minúsculas
# usando caracter.lower() y se verifica si está en la cadena "aeiou",
# que contiene todas las vocales en minúscula
    # Verificar si el caracter es una vocal
    if caracter.lower() in "a,e,i,o,u":

        # Incrementar el contador de vocales
        contador_vocales += 1

# Imprimir la cantidad de vocales encontradas

print(contador_vocales)


