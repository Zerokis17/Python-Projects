class Asistencia:
    asistencias = []

    def __init__(self, codigo_sesion, documento_estudiante, estado):
        self.codigo_sesion = codigo_sesion
        self.documento_estudiante = documento_estudiante
        self.estado = estado

    def __str__(self):
        return f"Código Sesión: {self.codigo_sesion}, Documento Estudiante: {self.documento_estudiante}, Estado: {self.estado}"

    @classmethod
    def agregarAsistencia(cls):
        codigo_sesion = input("Ingrese el código de la sesión: ")
        documento_estudiante = input("Ingrese el documento del estudiante: ")
        
        estado = input("Ingrese el estado (0: Si llegó, 1: Llegó tarde, 2: No llegó): ")
        while estado not in ['0', '1', '2']:
            print("Estado no válido. Debe ser 0, 1 o 2.")
            estado = input("Ingrese el estado (0: Si llegó, 1: Llegó tarde, 2: No llegó): ")

        asistencia = cls(codigo_sesion, documento_estudiante, estado)
        cls.asistencias.append(asistencia)
        print("\nAsistencia agregada correctamente.")

    @classmethod
    def listarAsistencia(cls, codigo_sesion, documento_estudiante):
        filtradas = [asistencia for asistencia in cls.asistencias 
                     if asistencia.codigo_sesion == codigo_sesion and asistencia.documento_estudiante == documento_estudiante]
        
        if not filtradas:
            print(f"No hay asistencias registradas para el código de sesión: {codigo_sesion} y documento: {documento_estudiante}.")
        else:
            for asistencia in filtradas:
                print(asistencia)
