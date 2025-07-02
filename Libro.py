from Recurso import Recurso
"""
Autor: Sebastian Cardona, Henry Hincapié
Fecha: 01/06/2025
"""
class Libro(Recurso):
    """
    Representa un recurso de tipo libro con sus atributos bibliográficos básicos.

    """

    def __init__(self, autor="", isbn=0, editorial="", edicion=0, numero_inventario=-1, titulo="", coleccion=0,
                 estado=0, tipo_recurso=0, codigo_alfnum=""):
        """
        Inicializa un objeto Libro con los atributos proporcionados.
        """
        super().__init__(numero_inventario, titulo, coleccion,
                 estado, tipo_recurso, codigo_alfnum)
        self.autor = autor
        self.isbn = isbn
        self.editorial = editorial
        self.edicion = edicion

    def almacenar_datos(self):
        """
        Solicita al usuario los datos del libro mediante entrada por consola.
        """
        super().solicitar_datos()
        self.autor = input("Ingrese el nombre del autor: ")
        while True:
            try:
                self.isbn = int(input("Ingrese el número ISBN: "))
                break
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número entero para el ISBN.")
        self.editorial = input("Ingrese la editorial del libro: ")
        while True:
            try:
                self.edicion = int(input("Ingrese el número de edición del libro: "))
                break
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número entero para la edición.")
                
    def mostrar_datos(self):
         print(f"Titulo: {self.titulo} \nCódigo alfanumérico: {self.codigo_alfnum} \nAutor: {self.autor} \nISBN: {self.isbn} \nEditorial {self.editorial} \nEdición: {self.edicion}")
    
    def modificar_datos(self):
        """
        Permite modificar los datos del libro validando las entradas y asegurando que no queden vacías.
        """
        print("\n--- Modificar datos del libro ---")

        print(f"Código actual: {self.codigo_alfnum}")
        if input("¿Desea modificar el código? (s/n): ").lower() == "s":
            while True:
                nuevo_codigo = input("Nuevo código alfanumérico: ").strip()
                if nuevo_codigo:
                    self.codigo_alfnum = nuevo_codigo
                    break
                else:
                    print("El código no puede estar vacío.")

        print(f"Título actual: {self.titulo}")
        if input("¿Desea modificar el título? (s/n): ").lower() == "s":
            while True:
                nuevo_titulo = input("Nuevo título: ").strip()
                if nuevo_titulo:
                    self.titulo = nuevo_titulo
                    break
                else:
                    print("El título no puede estar vacío.")

        print(f"Autor actual: {self.autor}")
        if input("¿Desea modificar el autor? (s/n): ").lower() == "s":
            while True:
                nuevo_autor = input("Nuevo autor: ").strip()
                if nuevo_autor:
                    self.autor = nuevo_autor
                    break
                else:
                    print("El autor no puede estar vacío.")

        print(f"ISBN actual: {self.isbn}")
        if input("¿Desea modificar el ISBN? (s/n): ").lower() == "s":
            while True:
                try:
                    self.isbn = int(input("Nuevo ISBN: "))
                    break
                except ValueError:
                    print("Por favor, ingrese un número válido.")

        print(f"Editorial actual: {self.editorial}")
        if input("¿Desea modificar la editorial? (s/n): ").lower() == "s":
            while True:
                nueva_editorial = input("Nueva editorial: ").strip()
                if nueva_editorial:
                    self.editorial = nueva_editorial
                    break
                else:
                    print("La editorial no puede estar vacía.")

        print(f"Edición actual: {self.edicion}")
        if input("¿Desea modificar la edición? (s/n): ").lower() == "s":
            while True:
                try:
                    self.edicion = int(input("Nueva edición: "))
                    break
                except ValueError:
                    print("Por favor, ingrese un número válido.")
