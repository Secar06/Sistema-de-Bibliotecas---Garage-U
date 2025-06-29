"""
Autor: Sebastian Cardona, Henry Hincapié
Fecha: 01/06/2025
"""
class Audio:
    """
    Representa un recurso de tipo audio, como canciones o grabaciones musicales.
    """

    def __init__(self, nom_cantante="", nom_productor="", year_grabacion=0):
        """
        Inicializa un objeto Audio con información básica sobre la grabación.
        """
        self.nom_cantante = nom_cantante
        self.nom_productor = nom_productor
        self.year_grabacion = year_grabacion

    def almacenar_datos(self):
        """
        Solicita al usuario los datos del recurso de audio.
        """
        self.nom_cantante = input("Escriba el nombre del cantante: ")
        self.nom_productor = input("Escriba el nombre del productor: ")
        self.year_grabacion = int(input("Digíte el año en que se grabó el audio: "))
