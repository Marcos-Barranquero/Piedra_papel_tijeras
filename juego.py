""" Juego de piedra, papel, o tijeras. """


from random import choice
import pickle
import os

def elegir_jugada_jugador():
    """ Devuelve la jugada que elige el jugador """
    eleccion_jugador = "" # Guardará piedra, papel o tijeras.
    while(not eleccion_jugador):
        eleccion_jugador = (input("Elige piedra, papel o tijera: "))
        eleccion_jugador.lower()  # lo pongo en minus. para comparar.
        if eleccion_jugador not in ("piedra", "papel", "tijera"):
            print("Debes escribir \'piedra\', \'papel\' o \'tijera\'.")
            eleccion_jugador = ""
    return eleccion_jugador

def elegir_jugada_ordenador():
    """ Devuelve la jugada que elige el ordenador. """
    return choice(("piedra", "papel", "tijera"))

def cargar_partida():
    """ Carga tus estadísticas globales del juego. """
    try:
        archivo = open("marcador.pickle", "rb")
        puntos = pickle.load(archivo)
        archivo.close()
    except FileNotFoundError: # Si no existe el archivo con
        generar_partida()     # La partida, genero uno
        puntos = cargar_partida()  # Y lo cargo.
    return puntos

def guardar_partida(puntos):
    """ Guarda la puntuación de la partida. """
    archivo = open("marcador.pickle", "wb")
    pickle.dump(puntos, archivo) # Guardo la punt. actualizada
    archivo.close() # Cierro el archivo


def generar_partida():
    """ Genera un nuevo marcador con estadísticas a 0 """
    archivo = open("marcador.pickle", "wb")
    puntos = {
        "p_jugadas": 0,
        "p_ganadas": 0,
        "p_perdidas": 0,
        "p_empatadas": 0
    }
    # Guardo la partida en el marcador:
    pickle.dump(puntos, archivo)
    archivo.close()

def comprobar_jugada(jugada_jugador, jugada_ordenador):
    """ Devuelve quién gana la partida. """
    if((jugada_jugador == "papel" and jugada_ordenador == "tijera")
       or (jugada_jugador == "piedra" and jugada_ordenador == "papel")
       or (jugada_jugador == "tijera" and jugada_ordenador == "piedra")):
        return "ordenador"
    elif((jugada_jugador == "papel" and jugada_ordenador == "piedra")
         or (jugada_jugador == "tijera" and jugada_ordenador == "papel")
         or (jugada_jugador == "piedra" and jugada_ordenador == "tijera")):
        return "jugador"
    else:
        return "empate"

def actualizar_puntos(ganador):
    """ Actualiza el marcador tras jugar una partida. """
    puntos = cargar_partida() # Recupero el marcador.
    if ganador == "jugador":
        puntos["p_ganadas"] += 1
    elif ganador == "ordenador":
        puntos["p_perdidas"] += 1
    else:
        puntos["p_empatadas"] += 1
    puntos["p_jugadas"] += 1
    guardar_partida(puntos) # Guardo el marcador actualizado.

def mostrar_puntuacion():
    """ Muestra por pantalla la puntuación actual. """
    puntos = cargar_partida()
    jugadas = puntos["p_jugadas"]
    ganadas = puntos["p_ganadas"]
    perdidas = puntos["p_perdidas"]
    empates = puntos["p_empatadas"]
    print("Mostrando puntuación: ")
    print(f"Partidas jugadas: {jugadas}")
    print(f"Partidas ganadas: {ganadas}")
    print(f"Partidas perdidas: {perdidas}")
    print(f"Partidas empatadas: {empates}")


def elige_mostrar_puntuacion():
    """ Permite elegir al jugador si quiere ver su puntuación. """
    mostrar = ""
    while(not mostrar):
        mostrar = input("¿Quieres ver la puntuación? S/N: ")
        mostrar.lower()
        if(mostrar == "s"):
            mostrar_puntuacion()
        elif(mostrar not in ("s", "n")):
            print("Debes escribir \'s\' ó \'n\'")
            mostrar = ""



# Programa principal:

continuar = "s"

while continuar.lower() == "s":
    os.system('cls')
    print("JUGANDO A PIEDRA, PAPEL O TIJERA")
    ordenador = elegir_jugada_ordenador()
    jugador = elegir_jugada_jugador()

    el_ganador = comprobar_jugada(jugador, ordenador)

    # Enseño la jugada por pantalla:
    print(f"Eliges {jugador} y el ordeandor elige {ordenador}")
    print(f"¡Ha ganado el {el_ganador}!")

    actualizar_puntos(el_ganador)
    elige_mostrar_puntuacion()

    continuar = ""
    while not continuar:
        continuar = input("¿Quieres continuar? S/N: ")
        continuar.lower()
        if continuar not in ("s", "n"):
            continuar = ""
            print("Debes escribir \'s\' ó \'n\'")
