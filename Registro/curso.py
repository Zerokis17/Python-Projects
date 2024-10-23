class Curso:
    cursos = []

    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre

    def __str__(self):
        return f"Código: {self.codigo}, Nombre: {self.nombre}"

    @classmethod
    def agregarCurso(cls):
        codigo = input("Ingrese el código del curso: ")
        nombre = input("Ingrese el nombre del curso: ")
        curso = cls(codigo, nombre)
        cls.cursos.append(curso)
        print("\nCurso agregado correctamente.")

    @classmethod
    def listarCurso(cls, codigo):
        filtrados = [curso for curso in cls.cursos if curso.codigo == codigo]
        if not filtrados:
            print(f"No hay cursos registrados con el código: {codigo}.")
        else:
            for curso in filtrados:
                print(curso)
                