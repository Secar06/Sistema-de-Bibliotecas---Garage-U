"""
Autor: Sebastian Cardona, Henry Hincapié
Fecha: 01/06/2025
"""
class Revista:
        """
        Representa una revista como recurso bibliográfico, con sus datos editoriales.
        """

        def __init__(self, ISSN=0, editorial="", volumen=0, numero=0, anno_publicacion=0):
            """
            Inicializa un objeto Revista con los campos bibliográficos requeridos.
            """
            self.ISSN = ISSN
            self.editorial = editorial
            self.volumen = volumen
            self.numero = numero
            self.año_publicacion = anno_publicacion

        def almacenar_datos(self):
            """
            Solicita al usuario los datos de la revista, incluyendo ISSN y año de publicación.
            """
            self.ISSN = int(input("Digíte el número ISSN de la revista: "))
            self.editorial = input("Escriba el nombre de la editorial de la revista: ")
            self.volumen = int(input("Digíte el volúmen de la revista: "))
            self.numero = int(input("Digíte el número de revista: "))
            self.año_publicacion = int(input("Digíte el año en que se publicó la revista: "))