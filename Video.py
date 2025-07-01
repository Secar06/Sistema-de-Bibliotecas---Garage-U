from Recurso import Recurso
"""
Autor: Sebastian Cardona, Henry Hincapié
Fecha: 01/06/2025
"""
class Video(Recurso):
    """
    Representa un recurso de tipo video con información sobre producción y género.
    """

    def __init__(self, nom_productor="", nom_director="", year_grabacion=0, genero=0, numero_inventario=-1, titulo="", coleccion=0,
                 estado=0, tipo_recurso=0, codigo_alfnum=""):
        """
        Inicializa un objeto Video con los datos básicos del recurso audiovisual.
        """
        super().__init__(numero_inventario, titulo, coleccion,
                 estado, tipo_recurso, codigo_alfnum)
        self.nom_productor = nom_productor
        self.nom_director = nom_director
        self.year_grabacion = year_grabacion
        self.genero = genero

    def almacenar_datos(self):
        """
        Solicita al usuario los datos del video y valida el género.
        """
        super().solicitar_datos()
        self.nom_productor = input("Ingrese el nombre del productor: ")
        self.nom_director = input("Ingrese el nombre del director: ")
        self.año_grabacion = int(input("Ingrese el año de grabación del video: "))

        print("Ingrese el género del video: \n1. DOCUMENTAL \n2. COMEDIA \n3. TERROR \n4. ACCIÓN")
        while True:
            try:
                self.genero = int(input("Seleccione una opción del menú: "))
                if self.genero in [1, 2, 3, 4]:
                    break
                else:
                    print("El genero ingresado es incorrecto, por favor intente nuevamente...")
            except ValueError:
                print("El tipo de dato ingresado es erróneo, por favor ingrese un número (1, 2, 3 o 4).")

        """while self.genero not in [1, 2, 3, 4]:
            input("El género es incorrecto, intente nuevamente...")
            print("Ingrese el género del video: \n1. DOCUMENTAL \n2. COMEDIA \n3. TERROR \n4. ACCIÓN")
            self.genero = int(input("Seleccione una opción del menú: "))"""

    