class Curso:
    def __init__(self, codigoCurso, nombreCurso):
        self.codigoCurso = codigoCurso
        self.nombreCurso = nombreCurso
        self.estudiantes = []

    def __str__(self):
        return f"Código: {self.codigoCurso}, Nombre: {self.nombreCurso}, Estudiantes: {len(self.estudiantes)}"


class Estudiante:
    def __init__(self, documentoIdentidad, nombre, curso):
        self.documentoIdentidad = documentoIdentidad
        self.nombre = nombre
        self.curso = curso

    def __str__(self):
        return f"Nombre: {self.nombre}, Documento: {self.documentoIdentidad}, Curso: {self.curso.codigoCurso}"


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
            return self.items[-1]
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
    cursos = []
    pilaCurso = Pila()
    colaCurso = Queue()
    opc = ""

    while opc != "9":
        opc = input("************ Estructuras de datos (Pilas y Colas) ***************\n"
                    "1. Adicionar un curso\n"
                    "2. Adicionar un estudiante al curso\n"
                    "3. Adicionar el curso a la pila\n"
                    "4. Sacar un curso de la pila y mostrar los datos\n"
                    "5. Listar todos los cursos de la pila sin sacarlos\n"
                    "6. Adicionar un curso a la cola\n"
                    "7. Sacar un curso de la cola y mostrar los datos\n"
                    "8. Listar todos los cursos de la cola sin sacarlos\n"
                    "9. Salir\n"
                    "Seleccione la opción que desea --> ")

        if opc == "1":
            curso = Curso(input("Ingrese el código del curso: "), input("Ingrese el nombre del curso: "))
            cursos.append(curso)
            print("Curso agregado correctamente.\n")

        elif opc == "2":
            codigoCurso = input("Ingrese el código del curso al que desea agregar el estudiante: ")
            cursoEncontrado = None
            for curso in cursos:
                if curso.codigoCurso == codigoCurso:
                    cursoEncontrado = curso
                    break

            if cursoEncontrado:
                documentoIdentidad = input("Ingrese documento de identidad del estudiante: ")
                nombreEstudiante = input("Ingrese el nombre del estudiante: ")
                estudiante = Estudiante(documentoIdentidad, nombreEstudiante, cursoEncontrado)
                cursoEncontrado.estudiantes.append(estudiante)
                print("Estudiante agregado al curso.\n")
            else:
                print("Curso no encontrado. Asegúrese de que el código sea correcto.\n")

        elif opc == "3":
            for curso in cursos:
                pilaCurso.push(curso)
            print("Cursos agregados a la pila.\n")

        elif opc == "4":
            cursoExtraido = pilaCurso.pop()
            if cursoExtraido:
                print(f"Curso sacado de la pila: {cursoExtraido}\n")

        elif opc == "5":
            pilaCurso.listar()

        elif opc == "6":
            for curso in cursos:
                colaCurso.enqueue(curso)
            print("Cursos agregados a la cola.\n")

        elif opc == "7":
            cursoExtraido = colaCurso.dequeue()
            if cursoExtraido:
                print(f"Curso removido de la cola: {cursoExtraido}\n")

        elif opc == "8":
            colaCurso.listar()

        elif opc == "9":
            print("Saliendo del programa...")

        else:
            print("Opción no válida. Inténtelo de nuevo.\n")


if __name__ == "__main__":
    main()
