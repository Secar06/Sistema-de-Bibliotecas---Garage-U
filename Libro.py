"""
Autor: Sebastian Cardona, Henry Hincapié
Fecha: 01/06/2025
"""
class Libro:
    """
    Representa un recurso de tipo libro con sus atributos bibliográficos básicos.

    """

    def __init__(self, autor="", isbn=0, editorial="", edicion=0):
        """
        Inicializa un objeto Libro con los atributos proporcionados.
        """
        self.autor = autor
        self.isbn = isbn
        self.editorial = editorial
        self.edicion = edicion

    def almacenar_datos(self):
        """
        Solicita al usuario los datos del libro mediante entrada por consola.
        """
        self.autor = input("Ingrese el nombre del autor: ")
        self.isbn = int(input("Ingrese el número ISBN: "))
        self.editorial = input("Ingrese la editorial del libro: ")
        self.edicion = int(input("Ingrese el número de edición del libro: "))
