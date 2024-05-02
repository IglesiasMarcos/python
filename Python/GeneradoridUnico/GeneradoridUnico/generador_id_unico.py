from random import randint
print("***Sistema Generador De ID unico***")
nombre = input("Cual es su nombre?")
nombre_1 = nombre[0:2].upper()
apellido = input("cual es tu apellido?")
apellido_1 = apellido[0:2].upper()
anio= input("Cual es tu año de nacimiento (YYYY)?:")
anio_1 = anio[2:4]
aleatorio= randint(0,9999)
id_unico= f"{nombre_1}{apellido_1}{anio_1}{aleatorio}"
#print(id_unico)
print(f"""\nHola {nombre},su nueva identificación (ID) generada por el sistema es: 
{id_unico}   

Felicidades!
""")

