# FORMATO DE CADENAS EN PYTHON

var_hola = "Hola"
var_mundo= "Mundo"

# Imprimir los valores ( , )
#print(var_hola,var_mundo)

#CONCACATENACION DE CADENAS (unir dos omas cadenas ,  +" "+
var_hola_mundo = var_hola + " " + var_mundo

#print(var_hola_mundo)

#interpolacion de cadenas, usando la letra f , f""

var_hola_mundo= f"Mi cadena:{var_hola} {var_mundo} "

print(var_hola_mundo)

#interpolacion con multilineas, f''' '''

#print(f'''Mi cadena:
#      {var_hola}
#          {var_mundo}''')