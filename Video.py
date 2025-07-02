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
        while True:
            try:
                self.year_grabacion = int(input("Ingrese el año de grabación del video: "))
                break
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número entero para el año de grabación.")

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

    def mostrar_datos(self):
        print(f"Titulo: {self.titulo} \nCódigo alfanumérico: {self.codigo_alfnum} \nNombre del productor: {self.nom_productor} \nNombre del director: {self.nom_director} \nAño de grabación: {self.year_grabacion}")
        match self.genero:
            case 1:
                print("Genero: Documental")
            case 2:
                print("Genero: Comedia")
            case 3:
                print("Genero: Terror")
            case 4:
                print("Genero: Acción")
    