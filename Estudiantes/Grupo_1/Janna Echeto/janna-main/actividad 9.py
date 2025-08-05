def mostrar_letra_cancion():
    canciones = {
        "1": {
            "titulo": "Mi Niña Bonita",
            "artista": "Chino y Nacho",
            "letra": """
Mi niña bonita, mi amor,
qué linda te ves cuando te miro, mi amor.
Tú eres mi bombón, mi sol,
la dueña de mi corazón.

Eres la estrella que ilumina mi ser,
la razón de mi existir, mi amanecer.
Contigo quiero yo envejecer,
mi niña bonita, mi gran placer.
"""
        },
        "2": {
            "titulo": "Andas En Mi Cabeza",
            "artista": "Chino y Nacho ft. Daddy Yankee",
            "letra": """
Andas en mi cabeza, nena, a todas horas.
No sé cómo te sacas la ropa,
si te la sacas en mi cama,
me muero de la emoción, nena.

Y yo te quiero, y tú me quieres,
somos perfectos en un cuento de hadas.
Tu y yo, nos juntamos, volamos,
en un universo de amores.
"""
        },
        "3": {
            "titulo": "Me Gustas",
            "artista": "Chino y Nacho",
            "letra": """
Me guta, me guta, me guta,
como lo mueve esa morena.
Me guta, me guta, me guta,
cuando baila mi nena.

Siento la adrenalina en mis venas,
cuando la veo meneando sus caderas.
Ella es la reina de la noche entera,
mi bella sirena.
"""
        }
    }

    print("¡Bienvenido al reproductor de letras de Chino y Nacho!")
    print("Por favor, selecciona una canción:")
    for key, info in canciones.items():
        print(f"{key}. {info['titulo']} - {info['artista']}")

    seleccion = input("Ingresa el número de tu elección: ")

    if seleccion in canciones:
        cancion_elegida = canciones[seleccion]
        print(f"\n--- Título: {cancion_elegida['titulo']} ---")
        print(f"--- Artista: {cancion_elegida['artista']} ---")
        print("\n" + cancion_elegida['letra'])
    else:
        print("Opción no válida. Por favor, selecciona un número de la lista.")

mostrar_letra_cancion()