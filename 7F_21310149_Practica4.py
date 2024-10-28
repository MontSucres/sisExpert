import random

# Listas de elementos del juego
personajes = ["pinguinoestrella", "pinguinoarcoiris", "pinguinodulce", "pinguinonieve", "pinguinobrillante"]
habitaciones = ["plaza", "cuevadenieve", "tiendaderegalos", "Biblioteca", "saladejuegos"]
armas = ["boladenieve", "pala", "Canondenieve", "sombrerodefiesta", "copadechocolatecaliente"]

# Escoger una escena del crimen aleatoria
escena_crimen = (
    random.choice(personajes),
    random.choice(habitaciones),
    random.choice(armas)
)

# Crear grupos de 3 elementos
grupos = {}
elementos = list(zip(personajes, habitaciones, armas))
random.shuffle(elementos)

for personaje, habitacion, arma in elementos:
    grupos[personaje] = (habitacion, arma)
    grupos[habitacion] = (personaje, arma)
    grupos[arma] = (personaje, habitacion)

# Mostrar la escena del crimen para fines de depuracion
print("Escena del crimen:", escena_crimen)  # Para propositos de depuracion (puedes comentarlo para no mostrarlo al jugador)

# Funcion para responder una consulta del usuario y verificar la veracidad
def responder_consulta(elemento):
    if elemento not in grupos:
        print("Elemento no encontrado en el juego.")
        return
    
    relacionado1, relacionado2 = grupos[elemento]
    print(f"\nInformacion sobre {elemento}:")
    print(f"- {elemento} se encuentra en {relacionado1} y lo tiene {relacionado2}.")
    
    # Verificar la veracidad de cada elemento en relacion a la escena del crimen
    veracidad_relacionado1 = (
        (relacionado1 == escena_crimen[0]) or
        (relacionado1 == escena_crimen[1]) or
        (relacionado1 == escena_crimen[2])
    )
    veracidad_relacionado2 = (
        (relacionado2 == escena_crimen[0]) or
        (relacionado2 == escena_crimen[1]) or
        (relacionado2 == escena_crimen[2])
    )
    if (elemento == escena_crimen[0] or
        elemento == escena_crimen[1] or
        elemento == escena_crimen[2]):
        print(f"- Veracidad:")
        print(f"   - {relacionado1} es {'verdadero' if veracidad_relacionado1 else 'falso'}")
        print(f"   - {relacionado2} es {'verdadero' if veracidad_relacionado2 else 'falso'}")
    else:
        print(f"- Veracidad:")
        print(f"   - {relacionado1} es {'falso' if veracidad_relacionado1 else 'verdadero'}")
        print(f"   - {relacionado2} es {'falso' if veracidad_relacionado2 else 'verdadero'}")

# Contador de inspecciones permitidas
inspecciones_restantes = 5

# Simulacion del juego
print("\n--- Bienvenido al juego de Club Penguin ---")
print("Puedes inspeccionar hasta 5 elementos para averiguar detalles sobre el crimen.")
print("Despues de 5 inspecciones, deberas adivinar al pinguino asesino.")

while inspecciones_restantes > 0:
    consulta = input("\n¿Qué elemento deseas inspeccionar? (escribe 'salir' para terminar): ").strip()
    
    if consulta.lower() == "salir":
        print("Gracias por jugar. ¡Hasta la próxima!")
        break
    
    responder_consulta(consulta.capitalize())
    inspecciones_restantes -= 1
    print(f"Inspecciones restantes: {inspecciones_restantes}")
    
    if inspecciones_restantes == 0:
        print("\nSe han agotado tus inspecciones.")
        
        # Solicitar al usuario que adivine la escena del crimen
        sospechoso = input("\n¿Quién crees que es el culpable?: ").strip()
        lugar = input("¿En qué habitación ocurrió el crimen?: ").strip()
        arma = input("¿Con qué arma se cometió el crimen?: ").strip()
        
        # Comprobar si el usuario adivinó correctamente
        if (sospechoso, lugar, arma) == escena_crimen:
            print("\n¡Felicidades! Has acertado en todos los elementos de la escena del crimen.")
        else:
            print("\nBuen intento, pero no acertaste en todos los elementos")
