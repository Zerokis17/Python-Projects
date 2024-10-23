from sesion import Sesion
from datetime import datetime

class Asistencia:
    asistencias = []

    def __init__(self, codigoSesion, documentoEstudiante, estado):
        self.codigoSesion = codigoSesion
        self.documentoEstudiante = documentoEstudiante
        self.estado = estado

    def __str__(self):
        return f"Código Sesión: {self.codigoSesion}, Documento Estudiante: {self.documentoEstudiante}, Estado: {self.estado}"

    @classmethod
    def agregarAsistencia(cls):
        codigoSesion = input("Ingrese el código de la sesión: ")
        documentoEstudiante = input("Ingrese el documento del estudiante: ")

        estado = input("Ingrese el estado (0: Si llegó, 1: Llegó tarde, 2: No llegó): ")
        while estado not in ['0', '1', '2']:
            print("Estado no válido. Debe ser 0, 1 o 2.")
            estado = input("Ingrese el estado (0: Si llegó, 1: Llegó tarde, 2: No llegó): ")

        asistencia = cls(codigoSesion, documentoEstudiante, estado)
        cls.asistencias.append(asistencia)
        print("\nAsistencia agregada correctamente.")

    @classmethod
    def listarAsistencia(cls, codigoSesion, documentoEstudiante):
        filtradas = [asistencia for asistencia in cls.asistencias 
                     if asistencia.codigoSesion == codigoSesion and asistencia.documentoEstudiante == documentoEstudiante]
        
        if not filtradas:
            print(f"No hay asistencias registradas para el código de sesión: {codigoSesion} y documento: {documentoEstudiante}.")
        else:
            for asistencia in filtradas:
                print(asistencia)

    @classmethod
    def listarTardanzasSesion(cls, codigoSesion):
        tardanzas = [asistencia for asistencia in cls.asistencias if asistencia.codigoSesion == codigoSesion and asistencia.estado == '1']
        if not tardanzas:
            print(f"No hubo estudiantes que llegaron tarde en la sesión con código: {codigoSesion}.")
        else:
            print(f"Estudiantes que llegaron tarde en la sesión {codigoSesion}:")
            for asistencia in tardanzas:
                print("Número de Identidad: " + asistencia.documentoEstudiante)

    @classmethod
    def listarTardanzasRango(cls, codigoCurso, fechaInicio, fechaFin):
        fechaInicio = datetime.strptime(fechaInicio, "%d/%m/%Y")
        fechaFin = datetime.strptime(fechaFin, "%d/%m/%Y")
        sesionesCurso = [sesion for sesion in Sesion.sesiones if sesion.codigoCurso == codigoCurso]

        if not sesionesCurso:
            print(f"No hay sesiones del curso {codigoCurso} en el rango de fechas dado.")
            return
        
        estudiantesTardanzas = {}
        
        for sesion in sesionesCurso:
            if fechaInicio <= datetime.strptime(sesion.fecha, "%d/%m/%Y") <= fechaFin:
                tardanzasSesion = [asistencia.documentoEstudiante for asistencia in cls.asistencias 
                                    if asistencia.codigoSesion == sesion.codigoSesion and asistencia.estado == '1']
                for estudiante in tardanzasSesion:
                    if estudiante in estudiantesTardanzas:
                        estudiantesTardanzas[estudiante] += 1
                    else:
                        estudiantesTardanzas[estudiante] = 1
        
        if not estudiantesTardanzas:
            print(f"No hubo estudiantes que llegaron tarde en el curso {codigoCurso} entre las fechas {fechaInicio.strftime('%d/%m/%Y')} y {fechaFin.strftime('%d/%m/%Y')}.")
        else:
            print(f"Cantidad de tardanzas por estudiante en el curso {codigoCurso}:")
            for estudiante, cantidad in estudiantesTardanzas.items():
                print(f"{estudiante}: {cantidad} veces")
