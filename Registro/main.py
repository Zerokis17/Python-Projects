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
        documento_id = input("Ingrese el documento del estudiante: ")
        Estudiante.listarEstudiante(documento_id)
    elif opcion == '6':
        codigo_curso = input("Ingrese el código del curso: ")
        Curso.listarCurso(codigo_curso)
    elif opcion == '7':
        codigo_sesion = input("Ingrese el código de la sesión: ")
        Sesion.listarSesion(codigo_sesion)
    elif opcion == '8':
        codigo_sesion = input("Ingrese el código de la sesión: ")
        documento_estudiante = input("Ingrese el documento del estudiante: ")
        Asistencia.listarAsistencia(codigo_sesion, documento_estudiante)
    elif opcion == '9':
        codigo_sesion = input("Ingrese el código de la sesión: ")
        Asistencia.listarTardanzasSesion(codigo_sesion)
    elif opcion == '10':
        codigo_curso = input("Ingrese el código del curso: ")
        fecha_inicio = input("Ingrese la fecha de inicio (DD/MM/YYYY): ")
        fecha_fin = input("Ingrese la fecha final (DD/MM/YYYY): ")
        Asistencia.listarTardanzasCursoRango(codigo_curso, fecha_inicio, fecha_fin)
    elif opcion == '11':
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intente nuevamente.")
