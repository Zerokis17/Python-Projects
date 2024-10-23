from estudiante import Estudiante
from curso import Curso
from sesion import Sesion
from asistencia import Asistencia

while True:
    print("_- Menú Principal -_")
    print("\n1.  Agregar estudiante")
    print("2.  Agregar curso")
    print("3.  Agregar sesión")
    print("4.  Registrar asistencia")
    print("5.  Listar datos de un estudiante")
    print("6.  Listar datos de un curso")
    print("7.  Listar datos de una sesión")
    print("8.  Listar datos de una asistencia")
    print("9.  Consultar estudiantes que llegaron tarde")
    print("10. Consultar veces de llegadas tardias de un estudiante")
    print("11. Salir")

    opcion = input("Seleccione una opción --> ")

    if opcion == '1':
        Estudiante.agregarEstudiante()
    elif opcion == '2':
        Curso.agregarCurso()
    elif opcion == '3':
        Sesion.agregarSesion()
    elif opcion == '4':
        Asistencia.agregarAsistencia()
    elif opcion == '5':
        documentoID = input("Ingrese el documento del estudiante: ")
        Estudiante.listarEstudiante(documentoID)
    elif opcion == '6':
        codigoCurso = input("Ingrese el código del curso: ")
        Curso.listarCurso(codigoCurso)
    elif opcion == '7':
        codigoSesion = input("Ingrese el código de la sesión: ")
        Sesion.listarSesion(codigoSesion)
    elif opcion == '8':
        codigoSesion = input("Ingrese el código de la sesión: ")
        documentoEstudiante = input("Ingrese el documento del estudiante: ")
        Asistencia.listarAsistencia(codigoSesion, documentoEstudiante)
    elif opcion == '9':
        codigoSesion = input("Ingrese el código de la sesión: ")
        Asistencia.listarTardanzasSesion(codigoSesion)
    elif opcion == '10':
        codigoCurso = input("Ingrese el código del curso: ")
        fechaInicio = input("Ingrese la fecha de inicio (DD/MM/YYYY): ")
        fechaFin = input("Ingrese la fecha final (DD/MM/YYYY): ")
        Asistencia.listarTardanzasRango(codigoCurso, fechaInicio, fechaFin)
    elif opcion == '11':
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intente nuevamente.")
