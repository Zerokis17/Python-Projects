class Estudiante:
    estudiantes = []

    def __init__(self, tipo_documento, numero_documento, nombres):
        self.tipo_documento = tipo_documento
        self.numero_documento = numero_documento
        self.nombres = nombres

    def __str__(self):
        return f"Tipo de Documento: {self.tipo_documento}, Número: {self.numero_documento}, Nombres: {self.nombres}"

    @classmethod
    def agregarEstudiante(cls):
        print("\nSeleccione el tipo de documento:")
        print("1. Tarjeta de identidad")
        print("2. Cédula")
        opcion = input("Ingrese el número de opción --> ")

        if opcion == '1':
            tipo_documento = "Tarjeta de identidad"
        elif opcion == '2':
            tipo_documento = "Cédula"
        else:
            print("Opción no válida. Intente nuevamente.")
            return

        numero_documento = input("Ingrese el número de documento: ")
        nombres = input("Ingrese los nombres completos del estudiante: ")
        estudiante = cls(tipo_documento, numero_documento, nombres)
        cls.estudiantes.append(estudiante)
        print("\nEstudiante agregado correctamente.")

    @classmethod
    def listarEstudiante(cls, numero_documento):
        filtrados = [estudiante for estudiante in cls.estudiantes if estudiante.numero_documento == numero_documento]
        if not filtrados:
            print(f"No hay estudiantes registrados con el documento: {numero_documento}.")
        else:
            for estudiante in filtrados:
                print(estudiante)
