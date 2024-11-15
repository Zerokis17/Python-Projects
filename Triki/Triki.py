import os
import json

# Inicializar variables
tablero = [[' ' for _ in range(3)] for _ in range(3)]
jugadas = []              # Lista para almacenar las coordenadas de cada jugada en la partida actual
partidas = []             # Arreglo para almacenar todas las partidas registradas

# Cargar el archivo JSON si existe y agregar partidas
def cargar_partidas():
    archivo = "partidas_empate.json"
    if os.path.exists(archivo):
        with open(archivo, 'r') as f:
            return json.load(f)
    return []

partidas = cargar_partidas()

# Función para mostrar el tablero
def mostrar_tablero():
    for fila in tablero:
        print('|'.join(fila))
        print('-' * 5)

# Función para verificar si hay un ganador
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

# Función para verificar si hay empate
def verificar_empate():
    for fila in tablero:
        if ' ' in fila:
            return False
    return True

# Función para guardar todas las partidas en el archivo JSON
def guardar_partidas():
    archivo = "partidas_empate.json"
    
    with open(archivo, 'w') as f:
        json.dump(partidas, f, indent=4)
    
    print(f"Partidas guardadas en {archivo}")

# Función principal del juego
def jugar_triki():
    global jugadas  # Asegurarse de que las jugadas de la partida actual estén en el ámbito global
    global tablero
    tablero = [[' ' for _ in range(3)] for _ in range(3)]  # Reiniciar el tablero para cada partida
    jugadas = []  # Limpiar jugadas de la partida actual
    
    jugador = 'X'
    while True:
        mostrar_tablero()
        print(f"Turno del jugador {jugador}")
        
        # Solicitar coordenadas de jugada
        try:
            fila = int(input("Ingresa la fila (1, 2, 3): ")) - 1
            col = int(input("Ingresa la columna (1, 2, 3): ")) - 1
        except ValueError:
            print("Coordenadas no válidas. Intenta nuevamente.")
            continue
        
        # Validar que la posición esté vacía
        if 0 <= fila < 3 and 0 <= col < 3 and tablero[fila][col] == ' ':
            tablero[fila][col] = jugador
            jugadas.append((fila + 1, col + 1))  # Almacenar la jugada con coordenadas del 1 al 3
            
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
        else:
            print("Esa posición ya está ocupada o no es válida. Intenta de nuevo.")

# Menú de opciones
def menu():
    while True:
        print("\n--- Menú ---")
        print("1. J1 vs J2 (guardar empate o partida ganada)")
        print("2. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            jugar_triki()
        elif opcion == '2':
            print("Saliendo del juego.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Iniciar el menú
menu()