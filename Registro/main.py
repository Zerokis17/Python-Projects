from estudiante import Estudiante
from curso import Curso
from sesion import Sesion
from asistencia import Asistencia

while True:
    print("_- Menú Principal -_")
    print("\n1. Agregar estudiante")
    print("2. Agregar curso")
    print("3. Agregar sesión")
    print("4. Registrar asistencia")
    print("5. Listar datos de un estudiante")
    print("6. Listar datos de un curso")
    print("7. Listar datos de una sesión")
    print("8. Listar datos de una asistencia")
    print("9. Salir")

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
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intente nuevamente.")
