"""
Autor: Sebastian Cardona, Henry Hincapié
Fecha: 01/06/2025
"""
class Recurso:
    """
    Clase base que representa un recurso general de la biblioteca.
    Puede ser un libro, video, audio o revista.
    """
    ARCHIVO = "datos_recursos.npy"
    
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

    def get_coleccion(self):
        match self.coleccion:
            case 1:
                return "GENERAL"
            case 2:
                return "RESERVA"
            case 3:
                return "HEMEROTECA"

    def get_estado(self):
        match self.estado:
            case 1:
                return "PRESTADO"
            case 2:
                return "DISPONIBLE"
            case 3:
                return "REPARACIÓN"
            case 4:
                return "INACTIVO"

    def get_tipo_recurso(self):
        match self.tipo_recurso:
            case 1:
                return "Libro"
            case 2:
                return "Video"
            case 3:
                return "Audio"
            case 4:
                return "Revista"


    def get_id(self):
        return self.numero_inventario

    def solicitar_datos(self):
        """
        Solicita y valida los datos generales del recurso.
        Luego solicita los datos específicos según el tipo de recurso.
        """
        self.codigo_alfnum = input("Ingrese el código alfanumérico del recurso: ")
        self.titulo = input("Ingrese el título del recurso: ")

        print("\nIngrese la colección a la que pertenece el recurso:\n1. GENERAL\n2. RESERVA\n3. HEMEROTECA")
        while True:
            try:
                self.coleccion = int(input("Seleccione una opción del menú: "))
                if self.coleccion in [1, 2, 3]:
                    break  
                else:
                    print("El tipo de colección ingresado es incorrecto, por favor intente nuevamente...")
            except ValueError:
                print("El tipo de dato ingresado es erróneo, por favor ingrese un número (1, 2 o 3).")

        print("Ingrese el estado del recurso:\n1. PRESTADO\n2. DISPONIBLE\n3. REPARACION\n4. INACTIVO")
        while True:
            try:
                self.estado = int(input("Seleccione una opción del menú: "))
                if self.estado in [1, 2, 3, 4]:
                    break
                else:
                    print("El estado ingresado es incorrecto, por favor intente nuevamente...")
            except ValueError:
                print("El tipo de dato ingresado es erróneo, por favor ingrese un número (1, 2, 3 o 4).")

