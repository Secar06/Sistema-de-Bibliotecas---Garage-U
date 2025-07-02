from Recurso import Recurso
"""
Autor: Sebastian Cardona, Henry Hincapié
Fecha: 01/06/2025
"""
class Revista(Recurso):
          """
          Representa una revista como recurso bibliográfico, con sus datos editoriales.
          """

          def __init__(self, ISSN=0, editorial="", volumen=0, numero=0, anno_publicacion=0, numero_inventario=-1, titulo="", coleccion=0,
                    estado=0, tipo_recurso=0, codigo_alfnum=""):
               """
               Inicializa un objeto Revista con los campos bibliográficos requeridos.
               """
               super().__init__(numero_inventario, titulo, coleccion,
                    estado, tipo_recurso, codigo_alfnum)
               self.ISSN = ISSN
               self.editorial = editorial
               self.volumen = volumen
               self.numero = numero
               self.anno_publicacion = anno_publicacion

          def almacenar_datos(self):
               """
               Solicita al usuario los datos de la revista, incluyendo ISSN y año de publicación.
               """
               super().solicitar_datos()
               while True:
                    try:
                         self.ISSN = int(input("Digíte el número ISSN de la revista: "))
                         break
                    except ValueError:
                         print("Entrada inválida. Por favor, ingrese un número entero para el ISSN.")

               self.editorial = input("Escriba el nombre de la editorial de la revista: ")

               while True:
                    try:
                         self.volumen = int(input("Digíte el volúmen de la revista: "))
                         break
                    except ValueError:
                         print("Entrada inválida. Por favor, ingrese un número entero para el volumen.")

               while True:
                    try:
                         self.numero = int(input("Digíte el número de revista: "))
                         break
                    except ValueError:
                         print("Entrada inválida. Por favor, ingrese un número entero para el número de revista.")

               while True:
                    try:
                         self.anno_publicacion = int(input("Digíte el año en que se publicó la revista: "))
                         break
                    except ValueError:
                         print("Entrada inválida. Por favor, ingrese un número entero para el año de publicación.")

          def mostrar_datos(self):
               print(f"Titulo: {self.titulo} \nCódigo alfanumérico: {self.codigo_alfnum} \nISSN: {self.ISSN} \nEditorial {self.editorial} \nVolumen: {self.volumen} \nNumero: {self.numero} \nAño de publicación: {self.anno_publicacion}")
          
          def modificar_datos(self):
               """
               Permite modificar los datos existentes del recurso tipo revista.
               """
               print("\n--- Modificar datos del recurso ---")

               print(f"Código alfanumerico actual: {self.codigo_alfnum}")
               if input("¿Desea modificar el código? (s/n): ").lower() == "s":
                    self.codigo_alfnum = input("Nuevo código alfanumérico: ")

               print(f"Título actual: {self.titulo}")
               if input("¿Desea modificar el título? (s/n): ").lower() == "s":
                    self.titulo = input("Nuevo título: ")

               print(f"Editorial actual: {self.editorial}")
               if input("¿Desea modificar la editorial? (s/n): ").lower() == "s":
                    self.editorial = input("Nueva editorial: ")

               print(f"ISSN actual: {self.ISSN}")
               if input("¿Desea modificar el ISSN? (s/n): ").lower() == "s":
                    while True:
                         try:
                              self.ISSN = int(input("Nuevo ISSN: "))
                              break
                         except ValueError:
                              print("Por favor, ingrese un número válido.")

               print(f"Volumen actual: {self.volumen}")
               if input("¿Desea modificar el volumen? (s/n): ").lower() == "s":
                    while True:
                         try:
                              self.volumen = int(input("Nuevo volumen: "))
                              break
                         except ValueError:
                              print("Por favor, ingrese un número válido.")

               print(f"Número actual: {self.numero}")
               if input("¿Desea modificar el número de revista? (s/n): ").lower() == "s":
                    while True:
                         try:
                              self.numero = int(input("Nuevo número de revista: "))
                              break
                         except ValueError:
                              print("Por favor, ingrese un número válido.")

               print(f"Año de publicación actual: {self.anno_publicacion}")
               if input("¿Desea modificar el año de publicación? (s/n): ").lower() == "s":
                    while True:
                         try:
                              self.anno_publicacion = int(input("Nuevo año de publicación: "))
                              break
                         except ValueError:
                              print("Por favor, ingrese un número válido.")

