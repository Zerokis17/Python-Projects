import sys

class Item:
    documento = ""
    nombres = ""
    apellidos = ""

    def __init__(self, doc, nom, ape):
        self.documento = doc
        self.nombres = nom
        self.apellidos = ape

    def __str__(self):
        return f"Documento: {self.documento}, Nombres: {self.nombres}, Apellidos: {self.apellidos}"

class Pila:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            print("La pila está vacía, no se puede sacar un elemento.")

    def top(self):
        if not self.isEmpty():
            return self.items[len(self.items) - 1]
        else:
            print("La pila está vacía, no hay elementos.")

    def size(self):
        return len(self.items)

    def listar(self):
        if not self.isEmpty():
            print("Elementos en la pila:")
            for i, item in enumerate(reversed(self.items), start=1):
                print(f"{i}. {item}")
        else:
            print("La pila está vacía, no hay elementos para listar.")

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            print("La cola está vacía, no se puede sacar un elemento.")

    def size(self):
        return len(self.items)

    def listar(self):
        if not self.isEmpty():
            print("Elementos en la cola:")
            for i, item in enumerate(reversed(self.items), start=1):
                print(f"{i}. {item}")
        else:
            print("La cola está vacía, no hay elementos para listar.")

def main():
    pilaEstudiantes = Pila() 
    colaEstudiantes = Queue()
    opc = ""

    while opc != "7":
        opc = input("************ Estructuras de datos (Pilas y Colas) ***************\n"
                    "1. Adicionar un estudiante a la pila\n"
                    "2. Sacar un estudiante de la pila y mostrar los datos\n"
                    "3. Listar todos los elementos de la pila sin sacarlos\n"
                    "4. Adicionar un estudiante a la cola\n"
                    "5. Sacar un estudiante de la cola y mostrar los datos\n"
                    "6. Listar todos los elementos de la cola sin sacarlos\n"
                    "7. Salir\n"
                    "Seleccione la opción que desea --> ")

        if opc == "1":
            doc = input("Ingrese el documento del estudiante: ")
            nom = input("Ingrese los nombres del estudiante: ")
            ape = input("Ingrese los apellidos del estudiante: ")
            estudiante = Item(doc, nom, ape)
            pilaEstudiantes.push(estudiante)
            print("Estudiante agregado a la pila.\n")

        elif opc == "2":
            estudiante = pilaEstudiantes.pop()
            if estudiante:
                print(f"Estudiante sacado de la pila: {estudiante}\n")

        elif opc == "3":
            pilaEstudiantes.listar()
            print()

        elif opc == "4":
            doc = input("Ingrese el documento del estudiante: ")
            nom = input("Ingrese los nombres del estudiante: ")
            ape = input("Ingrese los apellidos del estudiante: ")
            estudiante = Item(doc, nom, ape)
            colaEstudiantes.enqueue(estudiante)
            print("Estudiante agregado a la cola.\n")

        elif opc == "5":
            estudiante = colaEstudiantes.dequeue()
            if estudiante:
                print(f"Estudiante sacado de la cola: {estudiante}\n")

        elif opc == "6":
            colaEstudiantes.listar()
            print()

        elif opc == "7":
            print("Saliendo del programa...")

        else:
            print("Opción no válida. Inténtelo de nuevo.\n")

if __name__ == "__main__":
    sys.exit(main())
