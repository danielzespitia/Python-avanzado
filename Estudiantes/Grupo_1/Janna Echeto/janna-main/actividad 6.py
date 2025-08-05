respuesta = input("¿Tienes una mascota? (sí/no): ").lower() # .lower() convierte la respuesta a minúsculas

if respuesta == "si":

    nombre_mascota = input("¡Qué bien! ¿Cómo se llama tu mascota? ")
    print(f"¡Tu mascota se llama {nombre_mascota}!")
elif respuesta == "no":

    nombre_futura_mascota = input("¡Oh, vaya! ¿Cómo te gustaría que se llamara tu futura mascota? ")
    print(f"¡Tu futura mascota se llamará {nombre_futura_mascota}!")
else:

    print("No entendí tu respuesta. Por favor, responde 'sí' o 'no'.")