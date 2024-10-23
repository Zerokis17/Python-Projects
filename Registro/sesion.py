class Sesion:
    sesiones = []

    def __init__(self, codigoSesion, codigoCurso, horaInicio, horaFinal, fecha):
        self.codigoSesion = codigoSesion
        self.codigoCurso = codigoCurso
        self.horaInicio = horaInicio
        self.horaFinal = horaFinal
        self.fecha = fecha

    def __str__(self):
        return f"Código Sesión: {self.codigoSesion}, Código Curso: {self.codigoCurso}, Hora Inicio: {self.horaInicio}, Hora Final: {self.horaFinal}, Fecha: {self.fecha}"

    @classmethod
    def agregarSesion(cls):
        codigoSesion = input("Ingrese el código de la sesión: ")
        codigoCurso = input("Ingrese el código del curso: ")
        horaInicio = input("Ingrese la hora de inicio (HH:MM): ")
        horaFinal = input("Ingrese la hora final (HH:MM): ")
        fecha = input("Ingrese la fecha (DD/MM/YYYY): ")
        sesion = cls(codigoSesion, codigoCurso, horaInicio, horaFinal, fecha)
        cls.sesiones.append(sesion)
        print("\nSesión agregada correctamente.")

    @classmethod
    def listarSesion(cls, codigoSesion):
        filtrados = [sesion for sesion in cls.sesiones if sesion.codigoSesion == codigoSesion]
        if not filtrados:
            print(f"No hay sesiones registradas con el código de sesión: {codigoSesion}.")
        else:
            for sesion in filtrados:
                print(sesion)
