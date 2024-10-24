piedra = "piedra"
papel = "papel"
tijera = "tijera"

jugador1 = input("Elección jugador 1: ")
jugador2 = input("Elección jugador 2: ")

if jugador1 == piedra:
    if jugador2 == papel:
        print("Jugador 2 gana")
    elif jugador2 == tijera:
        print("Jugador 1 gana")
    elif jugador2 == piedra:
        print("Empate")
elif jugador1 == papel:
    if jugador2 == papel:
        print("Empate")
    elif jugador2 == tijera:
        print("Jugador 2 gana")
    elif jugador2 == piedra:
        print("Jugador 1 gana")
elif jugador1 == tijera:
    if jugador2 == papel:
        print("Jugador 1 gana")
    elif jugador2 == tijera:
        print("Empate")
    elif jugador2 == piedra:
        print("Jugador 2 gana")
