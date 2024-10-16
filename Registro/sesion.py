class Sesion:
    sesiones = []

    def __init__(self, codigo_curso, hora_inicio, hora_final, fecha):
        self.codigo_curso = codigo_curso
        self.hora_inicio = hora_inicio
        self.hora_final = hora_final
        self.fecha = fecha

    def __str__(self):
        return f"Código Curso: {self.codigo_curso}, Hora Inicio: {self.hora_inicio}, Hora Final: {self.hora_final}, Fecha: {self.fecha}"

    @classmethod
    def agregarSesion(cls):
        codigo_curso = input("Ingrese el código del curso: ")
        hora_inicio = input("Ingrese la hora de inicio (HH:MM): ")
        hora_final = input("Ingrese la hora final (HH:MM): ")
        fecha = input("Ingrese la fecha (DD/MM/YYYY): ")
        sesion = cls(codigo_curso, hora_inicio, hora_final, fecha)
        cls.sesiones.append(sesion)
        print("\nSesión agregada correctamente.")

    @classmethod
    def listarSesion(cls, codigo_sesion):
        filtrados = [sesion for sesion in cls.sesiones if sesion.codigo_curso == codigo_sesion]
        if not filtrados:
            print(f"No hay sesiones registradas con el código de sesión: {codigo_sesion}.")
        else:
            for sesion in filtrados:
                print(sesion)
