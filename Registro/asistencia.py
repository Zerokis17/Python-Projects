from sesion import Sesion
from datetime import datetime

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

    @classmethod
    def listarTardanzasSesion(cls, codigo_sesion):
        tardanzas = [asistencia for asistencia in cls.asistencias if asistencia.codigo_sesion == codigo_sesion and asistencia.estado == '1']
        if not tardanzas:
            print(f"No hubo estudiantes que llegaron tarde en la sesión con código: {codigo_sesion}.")
        else:
            print(f"Estudiantes que llegaron tarde en la sesión {codigo_sesion}:")
            for asistencia in tardanzas:
                print("Numero de Identidad: " + asistencia.documento_estudiante)

    @classmethod
    def listarTardanzasCursoRango(cls, codigo_curso, fecha_inicio, fecha_fin):
        fecha_inicio = datetime.strptime(fecha_inicio, "%d/%m/%Y")
        fecha_fin = datetime.strptime(fecha_fin, "%d/%m/%Y")
        sesiones_curso = [sesion for sesion in Sesion.sesiones if sesion.codigo_curso == codigo_curso]

        
        if not sesiones_curso:
            print(f"No hay sesiones del curso {codigo_curso} en el rango de fechas dado.")
            return
        for sesion in sesiones_curso:
            tardanzas_sesion = [asistencia for asistencia in cls.asistencias 
                                if asistencia.codigo_sesion == sesion.codigo_curso and asistencia.estado == '1']
            print(f"Sesión {sesion.codigo_curso} del {sesion.fecha}: {len(tardanzas_sesion)} estudiantes llegaron tarde.")
