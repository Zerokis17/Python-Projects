import os
import json
import random

# Inicializar variables
tablero = [[' ' for _ in range(3)] for _ in range(3)]
jugadas = []              # Lista para almacenar las coordenadas de cada jugada en la partida actual
partidas = []             # Arreglo para almacenar todas las partidas registradas

# Cargar el archivo JSON si existe y agregar partidas
def cargar_partidas():
    archivo = "Triki/partidas_empate.json"
    if os.path.exists(archivo):
        with open(archivo, 'r') as f:
            return json.load(f)
    return []

partidas = cargar_partidas()

# Funcion para mostrar el tablero
def mostrar_tablero():
    for fila in tablero:
        print('|'.join(fila))
        print('-' * 5)

# Funcion para verificar si hay un ganador
def verificar_ganador():
    # Verificar filas, columnas y diagonales
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != ' ':
            return tablero[i][0]
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != ' ':
            return tablero[0][i]
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != ' ':
        return tablero[0][0]
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != ' ':
        return tablero[0][2]
    return None

# Funcion para verificar si hay empate
def verificar_empate():
    for fila in tablero:
        if ' ' in fila:
            return False
    return True

# Funcion para guardar todas las partidas en el archivo JSON
def guardar_partidas():
    archivo = "Triki/partidas_empate.json"
    
    with open(archivo, 'w') as f:
        json.dump(partidas, f, indent=4)
    
    print(f"Partidas guardadas en el archivo.json")

# Funcion para calcular la probabilidad de victoria de la maquina
def calcular_probabilidad_victoria():
    if not partidas:
        return 0
    
    partidas_ganadas = [partida for partida in partidas if partida['resultado'].startswith("Ganador O")]
    if not partidas_ganadas:
        return 0
    
    probabilidad = 0
    for partida in partidas_ganadas:
        jugadas_partida = partida['jugadas']
        
        # Comparar las jugadas de la maquina en la partida con el tablero actual
        coincidencias = 0
        for jugada in jugadas_partida:
            fila, col = jugada[0] - 1, jugada[1] - 1
            if tablero[fila][col] == 'O':  # Verificar si la maquina jugo en esa casilla
                coincidencias += 1
        
        probabilidad += coincidencias / len(jugadas_partida)  # Normalizamos la similitud
    
    # Promediamos la probabilidad de victoria basada en las partidas ganadas
    probabilidad = (probabilidad / len(partidas_ganadas)) * 100
    return round(probabilidad, 2)

# Funcion para que la maquina haga un movimiento basado en partidas anteriores
def movimiento_maquina():
    if partidas:
        # Tomamos una jugada aleatoria de las partidas previas
        partida = random.choice(partidas)
        jugada = random.choice(partida['jugadas'])
        fila, col = jugada[0] - 1, jugada[1] - 1  # Ajustar a indices de lista (0, 1, 2)
    else:
        # Si no hay partidas previas, la maquina elige aleatoriamente una casilla vacia
        while True:
            fila, col = random.randint(0, 2), random.randint(0, 2)
            if tablero[fila][col] == ' ':  # Verificar que la casilla este vacia
                break

    # Validar que la casilla este vacia antes de colocar la jugada
    if tablero[fila][col] != ' ':
        return movimiento_maquina()  # Volver a intentar si la casilla ya esta ocupada

    # Mostrar probabilidad de victoria
    probabilidad = calcular_probabilidad_victoria()
    print(f"Probabilidad de victoria de la maquina: {probabilidad}%")
    
    return fila, col


# Funcion principal del juego
def jugar_triki():
    global jugadas  # Asegurarse de que las jugadas de la partida actual esten en el ambito global
    global tablero
    tablero = [[' ' for _ in range(3)] for _ in range(3)]  # Reiniciar el tablero para cada partida
    jugadas = []  # Limpiar jugadas de la partida actual
    
    jugador = 'X'  # El jugador humano siempre comienza
    while True:
        mostrar_tablero()
        print(f"Turno del jugador {jugador}")
        
        if jugador == 'X':  # El jugador humano hace su jugada
            try:
                fila = int(input("Ingresa la fila (1, 2, 3): ")) - 1
                col = int(input("Ingresa la columna (1, 2, 3): ")) - 1
            except ValueError:
                print("Coordenadas no validas. Intenta nuevamente.")
                continue
            
            # Validar que la posicion este vacia
            if 0 <= fila < 3 and 0 <= col < 3 and tablero[fila][col] == ' ':
                tablero[fila][col] = jugador
                jugadas.append((fila + 1, col + 1))  # Almacenar la jugada con coordenadas del 1 al 3
            else:
                print("Esa posicion ya esta ocupada o no es valida. Intenta de nuevo.")
                continue
        else:  # La maquina hace su jugada
            fila, col = movimiento_maquina()
            tablero[fila][col] = jugador
            jugadas.append((fila + 1, col + 1))  # Almacenar la jugada con coordenadas del 1 al 3
            print(f"La maquina jugo en la posicion ({fila + 1}, {col + 1})")
        
        # Verificar si hay ganador o empate
        ganador = verificar_ganador()
        if ganador:
            mostrar_tablero()
            print(f"¡Jugador {ganador} ha ganado!")
            partidas.append({"jugadas": list(jugadas), "resultado": f"Ganador {ganador}"})
            guardar_partidas()
            break
        elif verificar_empate():
            mostrar_tablero()
            print("¡Es un empate!")
            partidas.append({"jugadas": list(jugadas), "resultado": "Empate"})
            guardar_partidas()
            break
        
        # Cambiar de jugador
        jugador = 'O' if jugador == 'X' else 'X'

# Menu de opciones
def menu():
    while True:
        print("\n--- Menu ---")
        print("1. J1 vs J2 (guardar empate o partida ganada)")
        print("2. Jugar contra la maquina")
        print("3. Salir")
        
        opcion = input("Seleccione una opcion: ")
        
        if opcion == '1':
            jugar_triki()
        elif opcion == '2':
            jugar_triki() 
        elif opcion == '3':
            print("Saliendo del juego.")
            break
        else:
            print("Opcion no valida. Intente de nuevo.")

# Iniciar el menu
menu()
