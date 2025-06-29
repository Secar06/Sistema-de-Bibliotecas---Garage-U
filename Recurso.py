from Libro import Libro
from Audio import Audio
from Revista import Revista
from Video import Video
"""
Autor: Sebastian Cardona, Henry Hincapié
Fecha: 01/06/2025
"""
class Recurso:
    """
    Clase base que representa un recurso general de la biblioteca.
    Puede ser un libro, video, audio o revista.
    """
    def __init__(self, numero_inventario=-1, titulo="", coleccion=0,
                 estado=0, tipo_recurso=0, codigo_alfnum=""):
        """
        Inicializa un objeto Recurso con sus atributos principales.
        """
        self.numero_inventario = numero_inventario
        self.titulo = titulo
        self.coleccion = coleccion
        self.estado = estado
        self.tipo_recurso = tipo_recurso
        self.codigo_alfnum = codigo_alfnum

    def solicitar_datos(self):
        """
        Solicita y valida los datos generales del recurso.
        Luego solicita los datos específicos según el tipo de recurso.
        """
        self.codigo_alfnum = input("Ingrese el código alfanumérico del recurso: ")
        self.titulo = input("Ingrese el título del recurso: ")

        print("\nIngrese la colección a la que pertenece el recurso:\n1. GENERAL\n2. RESERVA\n3. HEMEROTECA")
        self.coleccion = int(input("Seleccione una opción del menú: "))
        while self.coleccion not in [1, 2, 3]:
            input("El tipo de colección ingresado es incorrecto, por favor intente nuevamente...")
            print("\n1. GENERAL\n2. RESERVA\n3. HEMEROTECA")
            self.coleccion = int(input("Seleccione una opción del menú: "))

        print("Ingrese el estado del recurso:\n1. PRESTADO\n2. DISPONIBLE\n3. REPARACION\n4. INACTIVO")
        self.estado = int(input("Seleccione una opción del menú: "))
        while self.estado not in [1, 2, 3, 4]:
            input("El estado del recurso ingresado es incorrecto, por favor intente nuevamente...")
            print("\n1. PRESTADO\n2. DISPONIBLE\n3. REPARACION\n4. INACTIVO")
            self.estado = int(input("Seleccione una opción del menú: "))

        print("\n1. Libro\n2. Video\n3. Audio\n4. Revista")
        self.tipo_recurso = int(input("Ingrese el tipo de recurso: "))
        while self.tipo_recurso not in [1, 2, 3, 4]:
            input("El tipo de recurso es incorrecto, intente nuevamente...")
            print("\n1. Libro\n2. Video\n3. Audio\n4. Revista")
            self.tipo_recurso = int(input("Ingrese el tipo de recurso: "))

        # Cargar datos específicos según el tipo
        if self.tipo_recurso == 1:
            resource = Libro()
            resource.almacenar_datos()
        elif self.tipo_recurso == 2:
            resource = Video()
            resource.almacenar_datos()
        elif self.tipo_recurso == 3:
            resource = Audio()
            resource.almacenar_datos()
        elif self.tipo_recurso == 4:
            resource = Revista()
            resource.almacenar_datos()
