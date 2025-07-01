from Recurso import Recurso
"""
Autor: Sebastian Cardona, Henry Hincapié
Fecha: 01/06/2025
"""
class Audio(Recurso):
    """
    Representa un recurso de tipo audio, como canciones o grabaciones musicales.
    """

    def __init__(self, nom_cantante="", nom_productor="", year_grabacion=0, numero_inventario=-1, titulo="", coleccion=0,
                 estado=0, tipo_recurso=0, codigo_alfnum=""):
        """
        Inicializa un objeto Audio con información básica sobre la grabación.
        """
        super().__init__(numero_inventario, titulo, coleccion,
                 estado, tipo_recurso, codigo_alfnum)
        self.nom_cantante = nom_cantante
        self.nom_productor = nom_productor
        self.year_grabacion = year_grabacion

    def almacenar_datos(self):
        """
        Solicita al usuario los datos del recurso de audio.
        """
        super().solicitar_datos()
        self.nom_cantante = input("Escriba el nombre del cantante: ")
        self.nom_productor = input("Escriba el nombre del productor: ")
        self.year_grabacion = int(input("Digíte el año en que se grabó el audio: "))
