class Estudiante:
    estudiantes = []

    def __init__(self, tipoDocumento, numeroDocumento, nombres):
        self.tipoDocumento = tipoDocumento
        self.numeroDocumento = numeroDocumento
        self.nombres = nombres

    def __str__(self):
        return f"Tipo de Documento: {self.tipoDocumento}, Número: {self.numeroDocumento}, Nombres: {self.nombres}"

    @classmethod
    def agregarEstudiante(cls):
        print("\nSeleccione el tipo de documento:")
        print("1. Tarjeta de identidad")
        print("2. Cédula")
        opcion = input("Ingrese el número de opción --> ")

        if opcion == '1':
            tipoDocumento = "Tarjeta de identidad"
        elif opcion == '2':
            tipoDocumento = "Cédula"
        else:
            print("Opción no válida. Intente nuevamente.")
            return

        numeroDocumento = input("Ingrese el número de documento: ")
        nombres = input("Ingrese los nombres completos del estudiante: ")
        estudiante = cls(tipoDocumento, numeroDocumento, nombres)
        cls.estudiantes.append(estudiante)
        print("\nEstudiante agregado correctamente.")

    @classmethod
    def listarEstudiante(cls, numeroDocumento):
        filtrados = [estudiante for estudiante in cls.estudiantes if estudiante.numeroDocumento == numeroDocumento]
        if not filtrados:
            print(f"No hay estudiantes registrados con el documento: {numeroDocumento}.")
        else:
            for estudiante in filtrados:
                print(estudiante)
