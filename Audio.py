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
        while True:
            try:
                self.year_grabacion = int(input("Digíte el año en que se grabó el audio: "))
                break
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número entero para el año.")
    def mostrar_datos(self):
        print(f"Titulo: {self.titulo} \nCódigo alfanumérico: {self.codigo_alfnum} \nNombre del cantante: {self.nom_cantante} \nNombre del productor: {self.nom_productor} \nAño de grabación: {self.year_grabacion}")
    
    def modificar_datos(self):
        """
        Permite modificar los datos del recurso tipo audio,
        validando entradas vacías y tipos numéricos.
        """
        print("\n--- Modificar datos del recurso de audio ---")

        print(f"Código actual: {self.codigo_alfnum}")
        if input("¿Desea modificar el código? (s/n): ").lower() == "s":
            while True:
                nuevo_codigo = input("Nuevo código alfanumérico: ").strip()
                if nuevo_codigo:
                    self.codigo_alfnum = nuevo_codigo
                    break
                else:
                    print("El código no puede estar vacío.")

        print(f"Título actual: {self.titulo}")
        if input("¿Desea modificar el título? (s/n): ").lower() == "s":
            while True:
                nuevo_titulo = input("Nuevo título: ").strip()
                if nuevo_titulo:
                    self.titulo = nuevo_titulo
                    break
                else:
                    print("El título no puede estar vacío.")

        print(f"Cantante actual: {self.nom_cantante}")
        if input("¿Desea modificar el nombre del cantante? (s/n): ").lower() == "s":
            while True:
                nuevo_cantante = input("Nuevo nombre del cantante: ").strip()
                if nuevo_cantante:
                    self.nom_cantante = nuevo_cantante
                    break
                else:
                    print("El nombre del cantante no puede estar vacío.")

        print(f"Productor actual: {self.nom_productor}")
        if input("¿Desea modificar el nombre del productor? (s/n): ").lower() == "s":
            while True:
                nuevo_productor = input("Nuevo nombre del productor: ").strip()
                if nuevo_productor:
                    self.nom_productor = nuevo_productor
                    break
                else:
                    print("El nombre del productor no puede estar vacío.")

        print(f"Año de grabación actual: {self.year_grabacion}")
        if input("¿Desea modificar el año de grabación? (s/n): ").lower() == "s":
            while True:
                try:
                    self.year_grabacion = int(input("Nuevo año de grabación: "))
                    break
                except ValueError:
                    print("Por favor, ingrese un número válido para el año.")