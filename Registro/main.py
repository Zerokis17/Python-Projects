from estudiante import Estudiante
from curso import Curso
from sesion import Sesion
from asistencia import Asistencia

while True:
    print("\n--- Menú Principal ---")
    print("1. Agregar estudiante")
    print("2. Agregar curso")
    print("3. Agregar sesión")
    print("4. Registrar asistencia")
    print("5. Listar estudiantes")
    print("6. Listar cursos")
    print("7. Listar sesiones")
    print("8. Listar asistencias")
    print("9. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        Estudiante.agregar_estudiante()
    elif opcion == '2':
        Curso.agregar_curso()
    elif opcion == '3':
        Sesion.agregar_sesion()
    elif opcion == '4':
        Asistencia.agregar_asistencia()
    elif opcion == '5':
        Estudiante.listar_estudiantes()
    elif opcion == '6':
        Curso.listar_cursos()
    elif opcion == '7':
        Sesion.listar_sesiones()
    elif opcion == '8':
        Asistencia.listar_asistencias()
    elif opcion == '9':
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intente nuevamente.")