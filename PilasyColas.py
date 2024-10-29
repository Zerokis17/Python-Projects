import sys

class Curso:
    def __init__(self, codigoCurso, nombreCurso):
        self.codigoCurso = codigoCurso
        self.nombreCurso = nombreCurso
        self.estudiantes = []
    
    def adicionarEstudiante(self,estudiante):
        self.estudiantes.append(estudiante)

class Estudiante:
    def __init__(self, documentoIdentidad, nombre, curso):
        self.documentoIdentidad = documentoIdentidad
        self.nombre = nombre
        self.curso = curso

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
    curso = Curso("","")
    opc = ""

    while opc != "9":
        opc = input("************ Estructuras de datos (Pilas y Colas) ***************\n"
                    "1. Adicionar un curso\n"
                    "2. Adicionar un estudiante al curso"
                    "3. Adicionar el curso a la pila\n"
                    "4. Sacar un curso de la pila y mostrar los datos\n"
                    "5. Listar todos los cursos de la pila sin sacarlos\n"
                    "6. Adicionar un curso a la cola\n"
                    "7. Sacar un curso de la cola y mostrar los datos\n"
                    "8. Listar todos los cursos de la cola sin sacarlos\n"
                    "9. Salir\n"
                    "Seleccione la opción que desea --> ")

        if opc == "1":
            curso = Curso(input("Ingrese el codigo del curso: "), input("Ingrese el nombre del curso: "))
            print("Curso agregado correctame")

        elif opc == "2":
            curso.estudiantes.append(input("Ingrese nombre del estudiante"))
            print("Estudiante agregado al curso.")

        if opc == "3":
            doc = input("Ingrese el documento del estudiante: ")
            nom = input("Ingrese los nombres del estudiante: ")
            ape = input("Ingrese los apellidos del estudiante: ")
            estudiante = Item(doc, nom, ape)
            pilaEstudiantes.push(estudiante)
            print("Estudiante agregado a la pila.\n")

        elif opc == "4":
            estudiante = pilaEstudiantes.pop()
            if estudiante:
                print(f"Estudiante sacado de la pila: {estudiante}\n")

        elif opc == "5":
            pilaEstudiantes.listar()
            print()

        elif opc == "6":
            doc = input("Ingrese el documento del estudiante: ")
            nom = input("Ingrese los nombres del estudiante: ")
            ape = input("Ingrese los apellidos del estudiante: ")
            estudiante = Item(doc, nom, ape)
            colaEstudiantes.enqueue(estudiante)
            print("Estudiante agregado a la cola.\n")

        elif opc == "7":
            estudiante = colaEstudiantes.dequeue()
            if estudiante:
                print(f"Estudiante sacado de la cola: {estudiante}\n")

        elif opc == "8":
            colaEstudiantes.listar()
            print()

        elif opc == "9":
            print("Saliendo del programa...")

        else:
            print("Opción no válida. Inténtelo de nuevo.\n")

if __name__ == "__main__":
    sys.exit(main())
