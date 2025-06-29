"""
Autor: Sebastian Cardona, Henry Hincapié
Fecha: 01/06/2025
"""
class Video:
    """
    Representa un recurso de tipo video con información sobre producción y género.
    """

    def __init__(self, nom_productor="", nom_director="", year_grabacion=0, genero=0):
        """
        Inicializa un objeto Video con los datos básicos del recurso audiovisual.
        """
        self.nom_productor = nom_productor
        self.nom_director = nom_director
        self.year_grabacion = year_grabacion
        self.genero = genero

    def almacenar_datos(self):
        """
        Solicita al usuario los datos del video y valida el género.
        """
        self.nom_productor = input("Ingrese el nombre del productor: ")
        self.nom_director = input("Ingrese el nombre del director: ")
        self.año_grabacion = int(input("Ingrese el año de grabación del video: "))

        print("Ingrese el género del video: \n1. DOCUMENTAL \n2. COMEDIA \n3. TERROR \n4. ACCIÓN")
        self.genero = int(input("Seleccione una opción del menú: "))
        while self.genero not in [1, 2, 3, 4]:
            input("El género es incorrecto, intente nuevamente...")
            print("Ingrese el género del video: \n1. DOCUMENTAL \n2. COMEDIA \n3. TERROR \n4. ACCIÓN")
            self.genero = int(input("Seleccione una opción del menú: "))

    