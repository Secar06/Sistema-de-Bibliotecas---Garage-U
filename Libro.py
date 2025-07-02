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