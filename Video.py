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
    
    def modificar_datos(self):
        """
        Permite modificar los datos del recurso tipo video, validando las entradas y evitando campos vacíos.
        """
        print("\n--- Modificar datos del recurso de video ---")

        print(f"Código actual: {self.codigo_alfnum}")
        while True:
            opcion = input("¿Desea modificar el código? (s/n): ").lower()
            if opcion == "s":
                while True:
                    nuevo_codigo = input("Nuevo código alfanumérico: ").strip()
                    if nuevo_codigo:
                        self.codigo_alfnum = nuevo_codigo
                        break
                    else:
                        print("El código no puede estar vacío.")
                break
            elif opcion == "n":
                break
            else:
                print("Respuesta inválida. Responda con 's' o 'n'.")

        print(f"Título actual: {self.titulo}")
        while True:
            opcion = input("¿Desea modificar el título? (s/n): ").lower()
            if opcion == "s":
                while True:
                    nuevo_titulo = input("Nuevo título: ").strip()
                    if nuevo_titulo:
                        self.titulo = nuevo_titulo
                        break
                    else:
                        print("El título no puede estar vacío.")
                break
            elif opcion == "n":
                break
            else:
                print("Respuesta inválida. Responda con 's' o 'n'.")

        print(f"Productor actual: {self.nom_productor}")
        while True:
            opcion = input("¿Desea modificar el nombre del productor? (s/n): ").lower()
            if opcion == "s":
                while True:
                    nuevo_productor = input("Nuevo nombre del productor: ").strip()
                    if nuevo_productor:
                        self.nom_productor = nuevo_productor
                        break
                    else:
                        print("El nombre del productor no puede estar vacío.")
                break
            elif opcion == "n":
                break
            else:
                print("Respuesta inválida. Responda con 's' o 'n'.")

        print(f"Director actual: {self.nom_director}")
        while True:
            opcion = input("¿Desea modificar el nombre del director? (s/n): ").lower()
            if opcion == "s":
                while True:
                    nuevo_director = input("Nuevo nombre del director: ").strip()
                    if nuevo_director:
                        self.nom_director = nuevo_director
                        break
                    else:
                        print("El nombre del director no puede estar vacío.")
                break
            elif opcion == "n":
                break
            else:
                print("Respuesta inválida. Responda con 's' o 'n'.")

        print(f"Año de grabación actual: {self.year_grabacion}")
        while True:
            opcion = input("¿Desea modificar el año de grabación? (s/n): ").lower()
            if opcion == "s":
                while True:
                    try:
                        self.year_grabacion = int(input("Nuevo año de grabación: "))
                        break
                    except ValueError:
                        print("Por favor, ingrese un número válido.")
                break
            elif opcion == "n":
                break
            else:
                print("Respuesta inválida. Responda con 's' o 'n'.")

        print(f"Género actual: {self.genero}")
        while True:
            opcion = input("¿Desea modificar el género? (s/n): ").lower()
            if opcion == "s":
                print("Opciones: \n1. DOCUMENTAL \n2. COMEDIA \n3. TERROR \n4. ACCIÓN")
                while True:
                    try:
                        nuevo_genero = int(input("Seleccione una opción del menú: "))
                        if nuevo_genero in [1, 2, 3, 4]:
                            self.genero = nuevo_genero
                            break
                        else:
                            print("El género ingresado es incorrecto, intente nuevamente.")
                    except ValueError:
                        print("Entrada inválida. Ingrese un número (1, 2, 3 o 4).")
                break
            elif opcion == "n":
                break
            else:
                print("Respuesta inválida. Responda con 's' o 'n'.")
