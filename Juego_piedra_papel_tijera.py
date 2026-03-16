import random

def jugar():
    opciones = ["piedra", "papel", "tijera"]

    jugador = input("Elige: piedra, papel o tijera: ").lower()

    if jugador not in opciones:
        print("Opción no válida, elige piedra, papel o tijera")
        return

    computadora = random.choice(opciones)

    print(f"\nTu elegiste: {jugador}")
    print(f"La computadora eligió: {computadora}")

    if jugador == computadora:
        print("Empate")
    elif (
        (jugador == "piedra" and computadora == "tijera") or
        (jugador == "papel" and computadora == "piedra") or
        (jugador == "tijera" and computadora == "papel")
    ):
        print("¡Ganaste!")
    else:
        print("Perdiste")

def juego():
    print("=== Piedra, Papel o Tijera ===")

    while True:
        jugar()

        otra = input("\n¿Quieres jugar otra vez? (si/no): ").lower()

        if otra != "si":
            print("Gracias por jugar")
            break


juego()