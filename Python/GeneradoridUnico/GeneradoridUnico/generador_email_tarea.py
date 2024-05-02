print("***Bienvenido al sistema de generación de email de ciudad gotica***")
nombre=input("Cual es tu nombre?")
nombre_1=nombre.lower()
apellido=input("Cual es tu apellido?")
apellido_1=apellido.lower()
email=("@ciudadgotica.com")
email_generado=nombre_1+"."+apellido_1+str(email)
#email_generado=f"{nombre.lower()}.{apellido.lower()}@ciudadgotica.com"
print(f"""\n{nombre} tu nuevo email generado por el sistema es:
    {email_generado}
    ***Felicidades*** 
    """)