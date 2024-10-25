import time

class Proceso:
    def __init__(self, nombreProceso, tiempoDuracion):
        self.nombreProceso = nombreProceso
        self.tiempoDuracion = tiempoDuracion

class Cola:
    def __init__(self):
        self.cola = []

    def adicionarProceso(self, proceso):
        self.cola.append(proceso)
        print(f"{proceso.nombreProceso} ha sido añadido a la cola.")

    def obtenerSiguienteProceso(self):
        if self.cola:
            return self.cola.pop(0)
        else:
            return None

    def mostrarCola(self):
        if self.cola:
            print("Cola actual de procesos:")
            for vc in self.cola:
                print(f" - {vc.nombreProceso} (Duración: {vc.tiempoDuracion} ms)")
        else:
            print("La cola está vacía.")

col = Cola()
opc = ""
procesosEjecutados = 0

while opc != "3":
    print("\nMENU")
    print("1. Adicionar un proceso")
    print("2. Simular procesos")
    print("3. Salir")
    opc = input("Seleccione la opción que desea --> ")

    if opc == "1":
        nombreProceso = input("Ingrese el nombre del proceso: ")
        tiempoDuracion = int(input("Ingrese el tiempo de duración del proceso (ms): "))
        proceso = Proceso(nombreProceso, tiempoDuracion)
        col.adicionarProceso(proceso)

    elif opc == "2":
        tiempoSimulacion = int(input("Ingrese el tiempo de simulación en segundos: "))

        while tiempoSimulacion > 0:
            print(f"\nSimulando... Tiempo restante: {tiempoSimulacion} segundos")
            procesoActual = col.obtenerSiguienteProceso()
            if procesoActual is None:
                break
            
            tiempoPorEjecutar = min(1000, procesoActual.tiempoDuracion)
            print(f"Ejecutando el proceso: {procesoActual.nombreProceso} durante {tiempoPorEjecutar / 1000:.1f} segundos.")
            time.sleep(1)
            procesoActual.tiempoDuracion -= tiempoPorEjecutar
            
            if procesoActual.tiempoDuracion > 0:
                col.adicionarProceso(procesoActual)
            else:
                procesosEjecutados += 1
            
            tiempoSimulacion -= 1

        print(f"\nSimulación finalizada. Se ejecutaron {procesosEjecutados} procesos.")
        col.mostrarCola()

    elif opc == "3":
        print("Saliendo del programa...")
    else:
        print("Opción no válida. Intente nuevamente.")
