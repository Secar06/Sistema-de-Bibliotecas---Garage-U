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
        self.isbn = int(input("Ingrese el número ISBN: "))
        self.editorial = input("Ingrese la editorial del libro: ")
        self.edicion = int(input("Ingrese el número de edición del libro: "))
        