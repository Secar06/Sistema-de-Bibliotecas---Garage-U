import numpy as np
from Audio import Audio
from Libro import Libro
from Revista import Revista
from Video import Video 
from Usuario import Usuario
from Prestamo import Prestamo
from Recurso import Recurso
from Historial_usuarios import Historial_usuarios
from datetime import date, timedelta
from collections import Counter
import funcionalidades as func

class AppGarageU:
    """ En esta clase llamada AppGarageU se lleva a cabo las funcionalidades del programa, como registrar un nuevo usuario, verificar el usuario,
    añadir nuevos recursos, entre otros
    00
    Autor: Sebastián Cardona, Elkin Alejandro López, Henry Hincapié
    Fecha: 01/05/2025
    """
    #ATRIBUTOS
    arreglo_recursos = np.ndarray
    arreglo_usuarios = np.ndarray
    arreglo_prestamos = np.ndarray
    historial_recursos = np.ndarray
    historial_usuarios = np.ndarray
    contador_historial_usuarios = np.ndarray
    contador_historial_recursos = np.ndarray
    contador_usuarios = int
    contador_recursos = int
    contador_prestamos = int
    usuario_autenticado = Usuario

    # CONSTANTES
    TIPO_ESTUDIANTE = 1
    TIPO_EMPLEADO = 2
    PERFIL_ADMIN = 1
    PERFIL_BIBLIO = 2
    PERFIL_USUARIO = 3
    MAX_RECURSOS = 100
    MAX_USUARIOS = 100
    MAX_PRESTAMOS = 100
    MAX_HISTORIAL_USUARIOS = 100
    MAX_HISTORIAL_RECURSOS = 100

    def __init__(self):
        # Carga los usuarios almacenados en el archivo de usuarios
        self.arreglo_usuarios, self.contador_usuarios = self.cargar_datos(Usuario.ARCHIVO, self.MAX_USUARIOS)

        self.arreglo_recursos, self.contador_recursos = self.cargar_datos(Recurso.ARCHIVO, self.MAX_RECURSOS)

        self.arreglo_prestamos, self.contador_prestamos = self.cargar_datos(Prestamo.ARCHIVO, self.MAX_PRESTAMOS)

        self.historial_recursos, self.contador_historial_recursos = self.cargar_datos("historial_recursos.npy", self.MAX_HISTORIAL_RECURSOS)

        self.historial_usuarios, self.contador_historial_usuarios = self.cargar_datos("historial_usuarios.npy", self.MAX_HISTORIAL_USUARIOS)
        if self.contador_usuarios == 0:
            self.arreglo_usuarios[0] = Usuario(nombre = "User Admin", identificacion=000, contrasenna='000')
            self.arreglo_usuarios[0].cambiar_perfil(self.PERFIL_ADMIN)
            self.contador_usuarios = 1

        self.usuario_autenticado = None

    def cargar_datos(self, archivo, num_max_datos):
        """ Este método carga los datos de un archivo, en un arreglo específico

            PARAMS
                archivo = URL relativa del archivo a abrir
                num_max_datos = indica el tamaño máximo de datos que almacena el arreglo

            RETURNS
                arreglo_de_datos = arreglo con los datos cargados
                num_datos = cantidad de datos cargados en el arreglo
        """
        try:
            arreglo_de_datos = np.load(archivo, allow_pickle=True)
            i = 0
            while arreglo_de_datos[i] is not None:
                i += 1
            return arreglo_de_datos, i
        except (FileNotFoundError, EOFError):
            print (f"No se pudo cargar el archivo {archivo}. Se creó un arreglo de datos vacío!")
            arreglo_de_datos = np.full(num_max_datos, fill_value=None, dtype=object)
            return arreglo_de_datos, 0

    def guardar_datos(self, arreglo_de_datos, archivo):
        """ Este método almacena los datos de un arreglo en un archivo

            PARAMS
                arreglo_de_datos = arreglo Numpy con los datos a alamcenar
                archivo = URL relativa del archivo en el que se almacenarán los datos

            RETURNS
                True si almacena los datos correctamente en el archivo
                False si no logra almacenar los datos en el archivo
        """
        try:
            np.save(archivo, arreglo_de_datos)
            return True
        except (FileNotFoundError, EOFError):
            print (f"Error: no se pudieron almacenar los  datos en el archivo {archivo}.")
            return False

    def registrar_usuario(self):
        """
        En este método es donde se realiza el registro de usuarios en el sistema. Esto se hace por medio de un arreglo, el cual es el que
        almacena los nuevos usuarios registrados en el sistema, y por medio de un match case se identifica qué tipo de usuario se registra
        """
        if self.contador_usuarios <= self.MAX_USUARIOS:
            nuevo_usuario = Usuario()
            while True:
                input_identificacion = input("\nIngrese el número de identificación del nuevo usuario o presione Enter para cancelar: ")
                if input_identificacion == "":
                    return
                try:
                    input_identificacion = int(input_identificacion)
                except ValueError:
                    print("\nNúmero de identificación no válido. Por favor inténtelo nuevamente.")
                else:
                    while self.validar_usuario(input_identificacion):
                        print(
                            f"\n[ADMIN] Se encontró un usuario con la identificación {input_identificacion}."
                            f" Por favor ingrese una identificación diferente.")
                        break
                    else:
                        # nuevo_usuario.almacenar_datos()
                        nuevo_usuario.identificacion = input_identificacion
                        nuevo_usuario.contrasenna = input("Ingrese una contraseña para el usuario: ")
                        self.actualizar_datos_usuario(nuevo_usuario)
                        self.arreglo_usuarios[self.contador_usuarios] = nuevo_usuario
                        self.contador_usuarios += 1

                        # Guarda en el archivo los datos de los usuarios
                        if not self.guardar_datos(self.arreglo_usuarios, Usuario.ARCHIVO):
                            print("No se pudo guardar el archivo de usaurios")
                        else:
                            print("\n[ADMIN] ¡Usuario Registrado Exitosamente!")

                        print(nuevo_usuario.mostrar_datos())
                        input("\nPresione Enter para volver al menú principal...")
                        return
        else:
            print("No se puede realizar el registro del usuario.\nCausa: almacenamiento insuficiente en el sistema.")

    def validar_usuario(self, id_a_buscar):
        for i in range(self.contador_usuarios):
            if self.arreglo_usuarios[i].identificacion == id_a_buscar:
                return True
        return False

    def determinar_perfil_usuario(self, usuario_actualizar : Usuario):
        """
        Pide al usuario que seleccione su perfil: Administrador o Bibliotecario.
        Se repite hasta que la entrada sea válida.
        """
        while True:
            # Menú de ppciones para determinar el perfil del usuario.
            print(
            "=============================\n"
            "      Perfil de Usuario      \n"
            "=============================\n"
            "1. Administrador\n"
            "2. Bibliotecario")
            opcion_perfil_usuario = input("Seleccione el perfil de usuario o presione Enter para volver atrás: ")
            if opcion_perfil_usuario == "":
                return None
            try:
                opcion_perfil_usuario = int(opcion_perfil_usuario)
            except ValueError:
                input("\n[ADMIN] Tipo de dato erroneo. Presione Enter e intente nuevamente...")
            else:
                if opcion_perfil_usuario not in [1, 2]:
                    input("\n[ADMIN] Opción incorrecta. Por favor presione Enter para intentar nuevamente...")
                else:
                    # Según sea el caso, se le asigna el valor correspondiente al perfil de usuario seleccionado
                    match opcion_perfil_usuario:
                        case 1:
                            usuario_actualizar.perfil_usuario = self.PERFIL_ADMIN
                            usuario_actualizar.tipo_usuario = self.TIPO_EMPLEADO
                        case 2:
                            usuario_actualizar.perfil_usuario = self.PERFIL_BIBLIO
                            usuario_actualizar.tipo_usuario = self.TIPO_EMPLEADO
                    return True

    def actualizar_datos_usuario(self, usuario_a_actualizar : Usuario):
        """
        Permite al usuario (o a un administrador) modificar sus datos personales.
        """
        mensaje_exitoso = "\n¡Información actualizada exitosamente! Presione Enter para continuar..."

        while True:
            # Se verifica el tipo de usuario y perfil para mostrarlo entre las opciones
            user_type = usuario_a_actualizar.get_tipo_usuario()
            user_profile = usuario_a_actualizar.get_perfil_usuario()

            # Menú de opciones
            lista_opciones = [1, 2, 3, 4, 5, 6, 7]
            menu = (
                "\n===========================\n"
                "  ACTUALIZACIÓN DE DATOS   \n"
                "===========================\n"
                f"USUARIO: {usuario_a_actualizar.identificacion}\n"
                f"1. Tipo de Usuario: {user_type}\n"
                f"2. Perfil de Usuario: {user_profile}\n"
                f"3. (*) Nombre: {usuario_a_actualizar.nombre}\n"
                f"4. (*) Dirección: {usuario_a_actualizar.direccion}\n"
                f"5. (*) Teléfono: {usuario_a_actualizar.telefono}\n"
                f"6. (*) Correo Electrónico: {usuario_a_actualizar.email}\n"
                f"7. Guardar datos.\n"
                "Tenga en cuenta que los campos marcados con * son obligatorios.")

            option = func.solicitar_opcion_menu(menu, lista_opciones, False)
            if option is None:
                return None
            elif option not in lista_opciones:
                input("Opción incorrecta. Inténtelo nuevamente. Presione enter para continuar...")
            elif not option in [1, 2]:
                match option:
                    case 3:
                        while True:
                            nombre_nuevo = input("Ingrese el nombre completo o presione Enter para cancelar: ")
                            if nombre_nuevo == "":
                                break
                            try:
                                usuario_a_actualizar.nombre = nombre_nuevo
                            except ValueError:
                                print("\nDebe ingresar al menos un nombre y un apellido. Por favor intente nuevamente.\n")
                            else:
                                input(mensaje_exitoso)
                                break
                    case 4:
                        usuario_a_actualizar.direccion = input("Ingrese la dirección de residencia: ")
                    case 5:
                        usuario_a_actualizar.telefono = input("Ingrese el número de teléfono: ")
                    case 6:
                        usuario_a_actualizar.email = input("Ingrese el correo electrónico: ").lower()
                    case 7:
                        if self.arrancar_verificaciones(usuario_a_actualizar):
                            input("\nParece que uno o varios campos obligatorios se encuentran vacíos. Presione Enter para intentar nuevamente...")
                        else:
                            input(mensaje_exitoso)
                            return None
            else:
                if self.usuario_autenticado.perfil_usuario != self.PERFIL_ADMIN:
                    input(
                        "[ERROR] No cuenta con el acceso para editar su tipo de usuario."
                        " Presione Enter para volver al menú anterior...")
                elif option == 1:
                    while True:
                        print(
                            "===================\n"
                            "   Tipo de Usuario  \n"
                            "===================\n"
                            "1. Estudiante\n"
                            "2. Empleado")
                        opcion_tipo_usuario = input("Seleccione el tipo de usuario o presione Enter para volver atrás: ")
                        if opcion_tipo_usuario == "":
                            break
                        try:
                            opcion_tipo_usuario = int(opcion_tipo_usuario)
                        except ValueError:
                            print("\n[ADMIN] Tipo de dato erroneo. Presione Enter e intente nuevamente...")
                        else:
                            if opcion_tipo_usuario not in [1, 2]:
                                input(
                                    "\n[ADMIN] Opción incorrecta. Por favor presione Enter para intentar nuevamente...")
                            else:
                                # Cuando el usuario selecciona empleado,
                                # se le pide determinar su perfil llamando al metodo determinar_perfil_usuario.
                                match opcion_tipo_usuario:
                                    case 1:
                                        usuario_a_actualizar.tipo_usuario = self.TIPO_ESTUDIANTE
                                        usuario_a_actualizar.perfil_usuario = self.PERFIL_USUARIO
                                        input(mensaje_exitoso)
                                        break
                                    case 2:
                                        if self.determinar_perfil_usuario(usuario_a_actualizar) is not None:
                                            usuario_a_actualizar.tipo_usuario = self.TIPO_EMPLEADO
                                            input(mensaje_exitoso)
                                            break

                elif option == 2:
                    if self.determinar_perfil_usuario(usuario_a_actualizar) is not None:
                        input(mensaje_exitoso)

    def arrancar_verificaciones(self, usuario: Usuario):
        """
        Verifica que cada campo de los datos del usuario no se dejen vacío. En tal caso retornará False.
        """
        bandera = False
        for i in range(1, 5):
            match i:
                case 1:
                    if usuario.nombre == "":
                        bandera = True
                        break
                case 2:
                    if usuario.direccion == "":
                        bandera = True
                        break
                case 3:
                    if usuario.telefono == 0:
                        bandera = True
                        break
                case 4:
                    if usuario.email == "":
                        bandera = True
                        break
        return bandera

    def eliminar_usuario(self, indice_usuario : int):
        """
        Elimina un usario del arreglo, actualiaza el contador y ordena los usuarios para rellenar los espacios vacios. Guarda los cambios realizados.
        PARAMS:
            indice_usuario: Indice del usuario a ser eliminado del arreglo.
        RETORNA:
            booleano: Verdadero si se eliminó el usuario con éxito.
        """
        while True:
            continuar = input("\n¿Seguro que desea eliminar el usuario? (S/N): ").upper()
            match continuar:
                case 'S':
                    self.arreglo_usuarios[indice_usuario] = None
                    self.contador_usuarios -= 1
                    for i in range(len(self.arreglo_usuarios)):
                        if self.arreglo_usuarios[i] is None:
                            for j in range(len(self.arreglo_usuarios) - i - 1):
                                self.arreglo_usuarios[i] = self.arreglo_usuarios[i + 1]
                                i += 1
                    if not self.guardar_datos(self.arreglo_usuarios, Usuario.ARCHIVO):
                        print("\nNo se pudo guardar el archivo de usaurios")
                    else:
                        input("\n[ADMIN] ¡Usuario Eliminado Exitosamente! Presione Enter para continuar...")
                    return True
                case 'N':
                    return False
                case _:
                    input("\n[ADMIN] Opción incorrecta. Intente nuevamente...")


    def verificar_usuario(self):
        """
        Es por medio de este método que el sistema podrá verificar si un usuario existe y poder iniciar la sesión del mismo,
        esto por medio de un ciclo for, el cual se encarga de recorrer el arreglo que almacena los datos de los usuarios y
        pide así la identificación y la contraseña del usuario con el fin de verificarlo.
        """
        print("\n" + "=" * 50)
        print("                INICIO DE SESIÓN             ")
        print("=" * 50)
        identificacion = int(input("Ingrese su número de identificación: "))
        for i in range(self.contador_usuarios):
            usuario = self.arreglo_usuarios[i]
            if usuario.identificacion == identificacion:
                contrasenna = input("Ingrese su contraseña: ")
                if usuario.contrasenna == contrasenna:
                    self.usuario_autenticado = self.arreglo_usuarios[i]
                    return True
                else:
                    print("\nIdentificación o contraseña incorrecta. Acceso denegado.")
                    return False
        input(f"El usuario con identificación {identificacion} no está registrado. Presione enter para continuar...")
        return False

    def crear_recurso(self, tipo_recurso):
        """Crea una instancia de un recurso y lo almacena en el arreglo de recursos.

            PARAMS:
                tipo_recurso: instancia de un recurso.
                arreglo: arreglo de recursos donde se almancenará el nuevo recurso.
                i: contador de recursos en el arreglo.
            RETURNS
                recurso: nueva instancia creada.
        """
        recurso = tipo_recurso
        recurso.almacenar_datos()
        recurso.numero_inventario = self.contador_recursos + 1
        self.arreglo_recursos[self.contador_recursos] = recurso
        self.contador_recursos += 1
        if not self.guardar_datos(self.arreglo_recursos, Recurso.ARCHIVO):
            print("No se pudo guardar el archivo de recursos")
            return None
        else:
            print(f"\n¡El recurso con número de inventario {recurso.numero_inventario} ha sido registrado correctamente!")
            print("=" * 50)
            print(f"Titulo: {recurso.titulo}")
        return recurso

    def registrar_recurso(self):
        """
        Por medio de este método es que un usuario bibliotecario puede registrar nuevos recursos
        gracias a un condicional if que analiza si aún hay espacio para añadir un nuevo recurso
        y en caso de que sí se cumpla esta condición, se pedirán los datos necesarios para añadir
        el recurso nuevo y se mostrará un mensaje avisando que se registró correctamente el recurso,
        junto con su número de inventario.
        """

        if self.contador_recursos >= self.MAX_RECURSOS:
            print("No se puede realizar el registro del recurso.\n Causa: almacenamiento insuficiente en el sistema.")
        else:
            if self.usuario_autenticado.perfil_usuario == self.PERFIL_BIBLIO:
                print(
                "\n==============================\n"
                "     MENÚ DE BIBLIOTECARIO    \n"
                "==============================")
            else:
                "\n==============================\n"
                "     MENÚ DE ADMINISTRADOR    \n"
                "=============================="
            while True:
                try:
                    tipo_recurso = int(input(
                            "      Registro de Recurso    \n"
                            "\nIngrese el tipo de recurso:\n"
                            "1. Libro\n"
                            "2. Revista\n"
                            "3. Video\n"
                            "4. Audio: "))
                    break
                except ValueError:
                    print("Error. intente nuevamente.")

            if tipo_recurso is None:
                return
            else:
                match tipo_recurso:
                    case 1:
                        recurso = Libro()
                        recurso = self.crear_recurso(Libro())
                        recurso.tipo_recurso = tipo_recurso
                    case 2:
                        recurso = Revista()
                        recurso = self.crear_recurso(Revista())
                        recurso.tipo_recurso = tipo_recurso
                    case 3:
                        recurso = Video()
                        recurso = self.crear_recurso(Video())
                        recurso.tipo_recurso = tipo_recurso
                    case 4:
                        recurso = Audio()
                        recurso  = self.crear_recurso(Audio())
                        recurso.tipo_recurso = tipo_recurso
                
                recurso.mostrar_datos()

                coleccion = recurso.get_coleccion()
                print(f"Colección del recurso: {coleccion}")

                estado = recurso.get_estado()
                print(f"Estado del recurso: {estado}")

                tipo_recurso = recurso.get_tipo_recurso()
                print(f"Tipo de recurso: {tipo_recurso}")
                input("Recurso registrado. Presione Enter para continuar...")
                print("=" * 50)

    # MÉTODO INICIAR MENÚ USUARIO DUPLICADO
    # def iniciar_menu_usuario(self):
    #     """
    #     En este método se mostrará el menú del usuario regular, el cual por el momento solo
    #     tiene permitido actualizar sus datos.
    #     """
    #     opcion_usuario = -1
    #     while opcion_usuario != 2:
    #         while True:
    #             menu = (
    #                     "==============================\n"
    #                     "         MENÚ DE USUARIO      \n"
    #                     "==============================\n"
    #                     "1. Actualizar datos\n"
    #                     "2. Cerrar sesión")
    #             opcion_usuario = func.solicitar_opcion_menu(menu,[1, 2])
    #             if opcion_usuario is None:
    #                 return
    #             else:
    #                 match opcion_usuario:
    #                     case 1:
    #                         self.usuario_autenticado.actualizar_datos(self.usuario_autenticado)
    #
    #                         indice = self.usuario_autenticado.consultar_indice(arreglo=self.arreglo_usuarios)
    #
    #                         self.arreglo_usuarios[indice] = self.usuario_autenticado
    #
    #                         # Guarda en el archivo los datos de los usuarios
    #                         if not self.guardar_datos(self.arreglo_usuarios, Usuario.ARCHIVO):
    #                             print("No se pudo guardar el archivo de usaurios")
    #                         else:
    #                             print("\nSe actualizó el archivo de usuarios")
    #                     case 2:
    #                         input("\nSe ha cerrado la sesión correctamente. Presione Enter para continuar...")
    #                     case _:
    #                         input("\nOpción incorrecta. Inténtelo nuevamente. Presione Enter para continuar...") #

    def modificar_recurso(self):
        if self.contador_recursos > 0:
            print(f"Hay un total de {self.contador_recursos} recursos")
            numero_recurso_arreglo = int(input("Ingrese el numero de inventario del recurso que desea modificar")) 
            place_holder_recurso = self.arreglo_recursos[numero_recurso_arreglo - 1]
            place_holder_recurso.modificar_datos()
            self.arreglo_recursos[numero_recurso_arreglo - 1] = place_holder_recurso
            if not self.guardar_datos(self.arreglo_recursos, Recurso.ARCHIVO):
                print("No se pudo guardar el archivo de recursos")
            else:
                print(f"\n¡El recurso con número de inventario {place_holder_recurso.numero_inventario} ha sido registrado correctamente!")
                print("=" * 50)
                print(f"Titulo: {place_holder_recurso.titulo}")
        else:
            print("No hay recursos registrados")

    def puede_prestar_usuario(self, id_usuario):
        persona = func.buscar_entidad(self.arreglo_usuarios, id_usuario)
        if persona == None:
            print("El usuario no fue encontrado en la base de datos")
        elif persona.multa != 0:
            return False
        else:
            return True
            
    def es_prestable(self, cod_recurso):
        recurso = func.buscar_entidad(self.arreglo_recursos, cod_recurso)
        if recurso == None:
            print("El recurso no fue encontrado en la base de datos")
        elif recurso.estado != 2:
            return False
        else:
            return True
    
    def calcular_fecha_devolucion(self,cod_recurso, id_usuario):
        recurso = func.buscar_entidad(self.arreglo_recursos, cod_recurso)
        usuario = func.buscar_entidad(self.arreglo_usuarios, id_usuario)
        if usuario.tipo_usuario == 1:
            match recurso.coleccion:
                case 1:
                    fecha_devolucion = date.today() + timedelta(days=15)
                    print(f"La fecha de devolución es: {fecha_devolucion.strftime("%d") + " " + fecha_devolucion.strftime("%B") + " " + fecha_devolucion.strftime("%Y")}")
                    return fecha_devolucion
                case 2:
                    fecha_devolucion = date.today() + timedelta(days=1)
                    print(f"La fecha de devolución es: {fecha_devolucion.strftime("%d") + " " + fecha_devolucion.strftime("%B") + " " + fecha_devolucion.strftime("%Y")}")
                    return fecha_devolucion
                case 3:
                    fecha_devolucion = date.today() + timedelta(days=3)
                    print(f"La fecha de devolución es: {fecha_devolucion.strftime("%d") + " " + fecha_devolucion.strftime("%B") + " " + fecha_devolucion.strftime("%Y")}")
                    return fecha_devolucion
        else:
            match recurso.coleccion:
                case 1:
                    fecha_devolucion = date.today() + timedelta(days=30)
                    print(f"La fecha de devolución es: {fecha_devolucion.strftime("%d") + " " + fecha_devolucion.strftime("%B") + " " + fecha_devolucion.strftime("%Y")}")
                    return fecha_devolucion
                case 2:
                    fecha_devolucion = date.today() + timedelta(days=15)
                    print(f"La fecha de devolución es: {fecha_devolucion.strftime("%d") + " " + fecha_devolucion.strftime("%B") + " " + fecha_devolucion.strftime("%Y")}")
                    return fecha_devolucion
                case 3:
                    fecha_devolucion = date.today() + timedelta(days=22)
                    print(f"La fecha de devolución es: {fecha_devolucion.strftime("%d") + " " + fecha_devolucion.strftime("%B") + " " + fecha_devolucion.strftime("%Y")}")
                    return fecha_devolucion
                
    def registrar_prestamo(self):
        if self.contador_prestamos >= self.MAX_PRESTAMOS:
            print("No se puede realizar el registro del prestamo.\n Causa: almacenamiento insuficiente en el sistema.")
            return
        else:
            while True:
                try:
                    buscar_id = int(input("Ingrese la id del usuario al cual se le va generar el prestamo: "))
                    break
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número entero.")
            while True:
                try:
                    buscar_cod = int(input("Ingrese el codigo de inventario del recurso que va a ser prestado: "))
                    break
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número entero.")
            if not self.puede_prestar_usuario(buscar_id):
                print("El usuario no puede hacer prestamos.")
            elif not self.es_prestable(buscar_cod):
                print("El recurso no esta disponible para prestamos.")
            else:
                prestamo = Prestamo()
                prestamo.indice_prestamo = self.contador_prestamos + 1
                prestamo.cod_recurso = buscar_cod
                prestamo.id_usuario = buscar_id
                usuario = func.buscar_entidad(self.arreglo_usuarios,buscar_id)
                prestamo.fecha_prestamo = date.today()
                prestamo.fecha_devolucion_estimada = self.calcular_fecha_devolucion(buscar_cod, buscar_id)
                self.arreglo_prestamos[self.contador_prestamos] = prestamo
                self.contador_prestamos += 1
                recurso = func.buscar_entidad(self.arreglo_recursos, buscar_cod)
                if not self.guardar_datos(self.arreglo_prestamos, Prestamo.ARCHIVO):
                    print("No se pudo guardar el archivo de prestamos")
                else:
                    if self.contador_historial_usuarios < self.MAX_HISTORIAL_USUARIOS:
                        historial_usuarios = Historial_usuarios()
                        historial_usuarios.fecha = date.today()
                        historial_usuarios.accion = "prestado"
                        historial_usuarios.usuario = usuario.nombre
                        historial_usuarios.id_usuario = usuario.identificacion
                        historial_usuarios.nombre_recurso = recurso.titulo
                        self.historial_usuarios[self.contador_historial_usuarios] = historial_usuarios
                        self.contador_historial_usuarios += 1
                        self.guardar_datos(self.historial_usuarios, "historial_usuarios.npy")
                        """ historial_recurso = Historial_recursos()
                        historial_recurso.accion = "PRESTADO"
                        historial_recurso.fecha = 
                        historial_recurso.usuario_nombre = Historial_recursos.usuario_nombre"""
                    print(f"La fecha del prestamo es: {prestamo.fecha_prestamo.strftime("%d") + " " + prestamo.fecha_prestamo.strftime("%B") + " " + prestamo.fecha_prestamo.strftime("%Y")}")
                    print(f"\n¡El prestamo con id {prestamo.indice_prestamo} ha sido registrado correctamente!")
                    input("Presione Enter para continuar...")
                    print("=" * 50)

    def buscar_recurso_titulo(self):
        if self.contador_recursos > 0:
            print(
                "=============================\n"
                "  BUSCAR RECURSO POR TITÚLO \n"
                "============================="
            )
            texto = input("\nIngrese el título o parte de él del recurso a buscar: ")
            cont = 0
            for i in range(self.MAX_RECURSOS):
                recurso = self.arreglo_recursos[i]
                if recurso == None:
                    break
                titulo = recurso.titulo
                if texto in titulo:
                    cont += 1
                    recurso.mostrar_datos()
                    coleccion = recurso.get_coleccion()
                    print(f"Colección del recurso: {coleccion}")

                    estado = recurso.get_estado()
                    print(f"Estado del recurso: {estado}")
                
                    tipo_recurso = recurso.get_tipo_recurso()
                    print(f"Tipo de recurso: {tipo_recurso}")
                    print("=" * 50)
                    print("\n")
                if cont == 0:
                    print(f"No se encontró ningún resultado con '{texto}'.\n")
        else:
            input("\n No se encuentra ningún recurso guardado. Presione Enter para continuar")


    def buscar_recurso_codigo(self):
        if self.contador_recursos > 0:
            print(
                "==================================\n"
                "  BUSCADOR DE RECURSO POR CÓDIGO \n"
                "=================================="
            )
            while True:
                try:
                    cod = int(input("\nIngrese el código de inventario del recurso a buscar: "))
                    break
                except ValueError:
                    print("Error, intente nuevamente.")
            recurso = func.buscar_entidad(self.arreglo_recursos, cod)
            if recurso is not None:
                recurso.mostrar_datos()
                coleccion = recurso.get_coleccion()
                print(f"Colección del recurso: {coleccion}")

                estado = recurso.get_estado()
                print(f"Estado del recurso: {estado}")

                tipo_recurso = recurso.get_tipo_recurso()
                print(f"Tipo de recurso: {tipo_recurso}")
                print("=" * 50)
                print("\n")
            else:
                print(f"No se encontró ningún resultado con '{cod}'.\n")
        else:
            input("\n No se encuentra ningún recurso guardado. Presione Enter para continuar")

    def mostrar_historial_recurso(self):
        contador_prestamo_usuario = 0
        while True:
            try:
                cod = int(input(f"Ingrese el código de inventario al cual necesita ver su historial: "))
                break
            except ValueError:
                print("Error. Intente de nuevo")    
        print(f"El recurso con código {cod} fue prestado por:\n")
        for i in range(self.MAX_HISTORIAL_USUARIOS):
            historial = self.historial_usuarios[i]
            if cod == historial.recursoid: 
                contador_prestamo_usuario +=1
                print(f"Préstamo {contador_prestamo_usuario}")
                historial.mostrar_datos_recurso()

    def veces_prestado(self):
        return sum(1 for evento in self.historial_recursos if evento["accion"] == "prestado")

    def mostrar_top5(self):
        print("\n Top 5 recursos más prestados: \n")
        top = sorted(self.arreglo_recursos, key=lambda recurso: recurso.titulo, reverse=True)

        if not top:
            print("No hay registros de prestamos")
            return
        print(f"{'Código':<10} {'Título':<40} {'# Préstamos'}")
        print("-" * 65)
        for Libro in top:
            print(f"{Libro.codigo:<10} {Libro.titulo:<40} {Libro.veces_prestado():>10}")
        contador = Counter(top)
        return contador.most_common(5)
        
    def mostrar_historial_usuario(self):
        contador_prestamo_usuario = 0
        while True:
            try:
                id = int(input(f"Ingrese el ID del usuario al cual necesita ver su historial: "))
                break
            except ValueError:
                print("Error. Intente de nuevo")    
        print(f"El usuario con ID {id} prestó:\n")
        for i in range(self.MAX_HISTORIAL_USUARIOS):
            historial = self.historial_usuarios[i]
            if id == historial.id_usuario: 
                contador_prestamo_usuario +=1
                print(f"Préstamo {contador_prestamo_usuario}")
                historial.mostrar_datos_usuario()
    def registrar_devolucion(self):
        while True:
            try:
                buscar_cod = int(input("Ingrese el codigo de inventario del recurso prestado: "))
                break
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número entero")
        while True:
            try:
                buscar_id = int(input("Ingrese la identificación del usuario: "))
                break
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número entero")
        for i in range(self.MAX_PRESTAMOS):
            prestamo = self.arreglo_prestamos[i]
            if buscar_cod == prestamo.cod_recurso and buscar_id == prestamo.id_usuario:
                while True:
                    fecha_str = input("Ingrese la fecha de devolución (en formato AAAA-MM-DD): ").strip()
                    try:
                        fecha_ingresada = date.fromisoformat(fecha_str)
                        prestamo.fecha_devolucion = fecha_ingresada
                        break
                    except ValueError:
                        print("Formato incorrecto. Por favor ingrese la fecha en formato AAAA-MM-DD.")
                mora = self.calcular_mora(prestamo.fecha_devolucion_estimada, fecha_ingresada)
                if mora > 0:
                    print(f"El usuario debe {mora} pesos por retraso en la devolucion")
                    input("Presione Enter para continuar...")
                else:
                    print("El recurso fue devuelto a tiempo, no se generó recargo por mora")
                    input("Presione Enter para continuar...")
                flag = True
                while flag == True:
                    for i in range(self.MAX_USUARIOS):
                        persona = self.arreglo_usuarios[i]
                        if persona.identificacion == buscar_id:
                            persona.multa = mora
                            self.arreglo_usuarios[i] = persona
                            for i in range (self.MAX_HISTORIAL_USUARIOS): 
                                historial = self.historial_usuarios[i]
                                if buscar_id == historial.id_usuario and buscar_cod == historial.recursoid and historial.fecha == prestamo.fecha_prestamo:
                                    historial.fecha_devolucion = fecha_ingresada
                                    historial.multa = mora
                                    self.historial_usuarios[i] = historial
                            if not self.guardar_datos(self.arreglo_usuarios, Usuario.ARCHIVO):
                                print("No se pudo guardar el archivo de usaurios")
                            else:
                                print("\n¡Datos del usuario actualizados correctamente!")
                            flag = False
                            return flag
                flag = True
                while flag == True:
                    for i in range(self.MAX_RECURSOS):
                        recurso = self.arreglo_recursos[i]
                        if recurso.numero_inventario == buscar_cod:
                            recurso.estado = 2
                            self.arreglo_recursos[i] = recurso
                            if not self.guardar_datos(self.arreglo_recursos, Recurso.ARCHIVO):
                                print("No se pudo guardar el archivo de recursos")
                            else:
                                print("\n¡Datos del recurso actualizados correctamente!")
                            flag = False
                            return flag
                print("La devolución fue registrada de manera exitosa")
            else:
                print("Error. El usuario y/o el recurso son incorrectos o no tienen un prestamo registrado.")
        input("Presione Enter para continuar...")
    
    def calcular_mora(self, fecha_devolucion_estimada, fecha_real_devolucion):
        dias_atraso = (fecha_real_devolucion - fecha_devolucion_estimada).days
        if dias_atraso > 0:
            mora = dias_atraso * 1000
        else:
            mora = 0
        return mora


    def listado_morosos(self):
        for j in range(self.MAX_PRESTAMOS):
            prestamo = self.arreglo_prestamos[j]
            usuario = func.buscar_entidad(self.arreglo_usuarios, prestamo.id_usuario)
            if usuario.identificacion == prestamo.id_usuario and usuario.multa > 0:
                tiempo_atraso = (date.today() - prestamo.fecha_devolucion_estimada).days
                recurso = func.buscar_entidad(self.arreglo_recursos, prestamo.cod_recurso)
                print("=" * 50)
                print(f"el usuario {usuario.nombre}, con identidificacion {usuario.identificacion} \ntiene una multa por mora de:{usuario.multa} pesos ya que tiene {tiempo_atraso} dias atrasados\nRecurso prestado: {recurso.titulo} \n Numero de inventario {recurso.numero_inventario}")

    def modificar_recurso(self):
        if self.contador_recursos > 0:
            print(f"Hay un total de {self.contador_recursos} recursos")
            numero_recurso_arreglo = int(input("Ingrese el numero de inventario del recurso que desea modificar"))
            place_holder_recurso = self.arreglo_recursos[numero_recurso_arreglo - 1]
            place_holder_recurso.modificar_datos()

    def iniciar_menu_usuario(self):
        """
        En este método se mostrará el menú del usuario regular, el cual por el momento solo
        tiene permitido actualizar sus datos.
        """
        opcion_usuario = -1
        while opcion_usuario != 2:
            while True:
                menu = (
                    "==============================\n"
                    "         MENÚ DE USUARIO      \n"
                    "==============================\n"
                    "1. Actualizar datos\n"
                    "2. Cerrar sesión")
                opcion_usuario = func.solicitar_opcion_menu(menu,[1, 2])
                if opcion_usuario is None:
                    return
                else:
                    match opcion_usuario:
                        case 1:
                            self.actualizar_datos_usuario(self.usuario_autenticado)
                            indice = self.usuario_autenticado.consultar_indice(arreglo=self.arreglo_usuarios)

                            self.arreglo_usuarios[indice] = self.usuario_autenticado

                            # Guarda en el archivo los datos de los usuarios
                            if not self.guardar_datos(self.arreglo_usuarios, Usuario.ARCHIVO):
                                print("No se pudo guardar el archivo de usaurios")
                            else:
                                print("\nSe actualizó el archivo de usuarios")
                        case 2:
                            input("\nSe ha cerrado la sesión correctamente. Presione Enter para continuar...")
                        case _:
                            input("\nOpción incorrecta. Inténtelo nuevamente. Presione Enter para continuar...")

    def iniciar_menu_admin(self):
        """
        En este método se mostrará el menú del usuario administrador, el cual por medio de un ciclo while
        permite al usuario escoger entre 3 opciones qué desea hacer, si registrar un usuario nuevo o
        modificar uno ya existente. Al escoger una opción, gracias al match case se podrá ejecutar sin
        problemas la opción elegida por el usuario administrador.
        """
        opcion_admin = -1
        while opcion_admin != 10:
            menu = (
                    "\n==============================\n"
                    "     MENÚ DE ADMINISTRADOR    \n"
                    "==============================\n"
                    "1. Registrar un nuevo usuario\n"
                    "2. Eliminar un usuario\n"
                    "3. Modificar un usuario\n" 
                    "4. Registrar un nuevo recurso\n"
                    "5. Inhabilitar un recurso\n"
                    "6. Modificar un recurso\n"
                    "7. Buscar recurso\n"
                    "8. Generar préstamo\n"
                    "9. Generar devolución\n"
                    "10. Consultar historial de prestamos de un recurso\n"
                    "11. Consultar historial de prestamos de un usuario\n"
                    "12. Cerrar sesión")

            opcion_admin = func.solicitar_opcion_menu(menu,[1,2,3,4,5,6,7,8,9,10,11,12], False)
            if opcion_admin not in [1,2,3,4,5,6,7,8,9,10,11,12]:
                print("Opción no válida. Por favor inténtelo nuevamente...")
            else:
                match opcion_admin:
                    case 1:
                        input("\n[ADMIN] Ha seleccionado la opción 1. Presione Enter para continuar...")
                        print("\n" + "=" * 50)
                        print("   MENÚ DE ADMINISTRADOR - REGISTRO DE USUARIO ")
                        print("=" * 50)
                        self.registrar_usuario()
                    case 2:
                        while True:
                            input("\n[ADMIN] Ha seleccionado la opción 2. Presione Enter para continuar...")
                            print(
                                "\n============================================\n"
                                " MENÚ DE ADMINISTRADOR - ELIMINAR USUSARIO \n"
                                "============================================"
                            )
                            id_usuario_eliminar = input(
                                "Ingrese la identificación del usuario que desea eliminar o presione Enter para cancelar: ")
                            if id_usuario_eliminar == "":
                                break
                            try:
                                id_usuario_eliminar = int(id_usuario_eliminar)
                            except ValueError:
                                print("Error con la identificación ingresada. Por favor intente de nuevo...")
                            else:
                                indice_usuario = func.buscar_usuario(self.arreglo_usuarios, id_usuario_eliminar)
                                if indice_usuario is not None:
                                    if self.eliminar_usuario(indice_usuario):
                                        break
                                else:
                                    print("\nNo se encontró un usuario con la identificación ingresada.")
                    case 3:
                        if self.contador_usuarios == 0:
                            print("No hay usuarios registrados en el sistema.")
                        else:
                            while True:
                                print("\n" + "=" * 50)
                                print(" MENÚ DE ADMINISTRADOR - MODIFICACIÓN DE USUARIO ")
                                print("=" * 50)
                                try:
                                    user_id = int(input("\nDigite el número de documento del usuario: "))
                                except ValueError:
                                    print("\nError en la entrada de datos. Por favor intente de nuevo...")
                                else:
                                    usuario_encontrado = self.arreglo_usuarios[func.buscar_usuario(self.arreglo_usuarios, user_id)]
                                    if not usuario_encontrado:
                                        input("El usuario con número de documento '' no se encuentra registrado en el sistema. "
                                              " Por favor, intente de nuevo. Presione Enter para volver al menú anterior...")
                                    else:
                                        if self.actualizar_datos_usuario(usuario_encontrado) is None:
                                            break
                    case 4:
                        print("\n" + "=" * 50)
                        print(" MENÚ DE ADMINISTRADOR - REGISTRO DE RECURSO ")
                        print("=" * 50)
                        input("\n[ADMIN] Ha seleccionado la opción 4. Presione Enter para continuar...")
                        self.registrar_recurso()
                        print("\n" + "=" * 50)
                        print(" MENÚ DE ADMINISTRADOR - INHABILITACIÓN DE RECURSO ")
                        print("=" * 50)
                        input("\n[ADMIN] Ha seleccionado la opción 5. Presione Enter para continuar...")
                        self.inhabilitar_recurso()
                    case 6:
                        input("\n[ADMIN] Ha seleccionado la opción 6. Presione Enter para continuar...")
                        print("\n" + "=" * 50)
                        print(" MENÚ DE ADMINISTRADOR - MODIFICACIÓN DE RECURSO ")
                        print("=" * 50)
                        input("\n[ADMIN] Ha seleccionado la opción 6. Presione Enter para continuar...")
                        self.modificar_recurso()
                    case 7:
                        input("\n[ADMIN] Ha seleccionado la opción 7. Presione Enter para continuar...")
                        print("\n" + "=" * 50)
                        print(" MENÚ DE ADMINISTRADOR - BUSCADOR DE RECURSOS ")
                        print("=" * 50)
                        while True:
                            try:
                                menu = int(input(
                                    "1. Buscar por título"
                                    "\n2. Buscar por código de inventario: "))
                                break
                            except ValueError:
                                print("Error, intente nuevamente.")

                        menu
                        if menu is not None:
                            match menu:
                                case 1:
                                    self.buscar_recurso_titulo()
                                case 2:
                                    self.buscar_recurso_codigo()
                    case 8:
                        print("\n" + "=" * 50)
                        print(" MENÚ DE ADMINISTRADOR - GENERAR PRESTAMO ")
                        print("=" * 50)
                        input("\n[ADMIN] Ha seleccionado la opción 8. Presione Enter para continuar...")
                        self.registrar_prestamo()
                    case 9:
                        print("\n" + "=" * 50)
                        print(" MENÚ DE ADMINISTRADOR - GENERAR DEVOLUCIÓN ")
                        print("=" * 50)
                        input("\n[ADMIN] Ha seleccionado la opción 9. Presione Enter para continuar...")
                        self.registrar_devolucion() 
                    case 10:
                        print("\n" + "=" * 50)
                        print(" MENÚ DE ADMINISTRADOR - CONSULTAR HISTORIAL DE PRESTAMOS RECURSO ")
                        input("\n[ADMIN] Ha seleccionado la opción 10. Presione Enter para continuar...")                        
                        print("=" * 50)
                        self.mostrar_historial_recurso() 
                    case 11:
                        print("\n" + "=" * 50)
                        print(" MENÚ DE ADMINISTRADOR - CONSULTAR HISTORIAL DE PRESTAMOS USUARIO ")
                        input("\n[ADMIN] Ha seleccionado la opción 11. Presione Enter para continuar...")
                        print("=" * 50)
                        self.mostrar_historial_usuario() 
                    case 12:
                        input("\n[ADMIN] Se ha cerrado la sesión correctamente. Presione Enter para continuar...")
                        return
                    case _:
                        input("\n[ADMIN] Opción incorrecta. Inténtelo nuevamente. Presione Enter para continuar...")


    def iniciar_menu_biblio(self):
        """
        Por medio de este método es que el usuario bibliotecario podrá escoger si desea registrar
        un recurso nuevo o si desea inhabilitarlo. Este método de menú funciona igual que los dos
        anteriores, por medio de un ciclo while se mostrará el menú para que el usuario eliga qué
        quiere hacer y por medio de un match case se ejecutará la funcionalidad correspondiente.
        """
        opcion_biblio = -1
        while opcion_biblio != 3:
            menu = (
                    "\n==============================\n"
                    "     MENÚ DE BIBLIOTECARIO    \n"
                    "==============================\n"
                    "1. Registrar un nuevo recurso\n"
                    "2. Inhabilitar Recurso\n"
                    "3. Cerrar sesión\n")
            opcion_biblio = func.solicitar_opcion_menu(menu,[1,2,3], False)
            match opcion_biblio:
                case 1:
                    self.registrar_recurso()
                case 2:
                    self.inhabilitar_recurso()
                case 3:
                    input("\nSe ha cerrado la sesión correctamente. Presione Enter para continuar...")
                    return
                case _:
                    input("\n[ADMIN] Opción incorrecta. Inténtelo nuevamente. Presione Enter para continuar...")

    def inhabilitar_recurso(self):
        """
        Es por medio de este método que los usuarios administradores pueden inhabilitar recursos;
        por medio de un ciclo for el cual recorre el arreglo que almacena los recursos luego de
        haber ingresado el numero de inventario del recurso, el sistema analiza si el recurso ya
        se encuentra inhabilitado y en caso de no estarlo se emitirá un mensaje mostrando el número
        de inventario del recurso avisando que ya se ha inhabilitado correctamente.
        """
        numero = int
        while True:
            print("\n" + "=" * 50)
            print("      ADMINISTRACIÓN - INHABILITAR RECURSO")
            print("=" * 50)
            numero = (input(
                    "Ingrese el número de inventario del recurso que desea inhabilitar o presione Enter para cancelar: "
                    ))
            if numero == "":
                return None
            try:
                numero = int(numero)
            except ValueError:
                print("Número de inventario no válido. Por favor inténtelo nuevamente")
            else:
                continuar = input("\n¿Seguro que desea inhabilitar el recurso? (S/N): ?").upper()
                match continuar:
                    case 'S':
                        for i in range(self.contador_recursos):
                            recurso = self.arreglo_recursos[i]
                            if recurso.numero_inventario == numero:
                                if recurso.estado == 4:
                                    print("Este recurso ya está inhabilitado.")
                                    return False
                                recurso.estado = 4
                                if not self.guardar_datos(self.arreglo_recursos, Recurso.ARCHIVO):
                                    print("No se pudo guardar el archivo de recursos")
                                else:
                                    print(
                                        f"\n¡El recurso con número de inventario {recurso.numero_inventario} ha sido inhabilitado correctamente!")
                                    print("=" * 50)
                                    print(f"Titulo: {recurso.titulo}")
                                    estado = recurso.get_estado()
                                    print(f"Estado del recurso: {estado}")
                                    return True
                        input("No se encontró un recurso con ese número de inventario. Presione Enter para continuar...")
                        return False
                    case 'N':
                        return False
                    case _:
                        input("\nOpción incorrecta. Por favor vuelva a intentarlo...")




        
    
    def main(self):
        opc = 0
        while opc != 2:
            menu = (
                    "\n============================\n"
                    "       MENÚ PRINCIPAL       \n"
                    "============================\n"
                    "1. Autenticarse\n"
                    "2. Salir de la app")
            opcion_menu = func.solicitar_opcion_menu(menu,[1,2], False)
            match opcion_menu:
                case 1:
                    if self.verificar_usuario():
                        print(f"\n¡Inicio de sesión exitoso! Bienvenid@ {self.usuario_autenticado.nombre.title()}")
                        if self.usuario_autenticado.perfil_usuario == self.PERFIL_ADMIN:
                            self.iniciar_menu_admin()
                        elif self.usuario_autenticado.perfil_usuario == self.PERFIL_BIBLIO:
                            self.iniciar_menu_biblio()
                        elif self.usuario_autenticado.perfil_usuario == self.PERFIL_USUARIO:
                            self.iniciar_menu_usuario()
                        else:
                            print("PERFIL NO RECONOCIDO")
                case 2:
                    self.usuario_autenticado = None
                    print("\nAPLICACIÓN FINALIZADA CORRECTAMENTE.")
                    break
                case _:
                    print("\nOpción incorrecta")

app = AppGarageU()
app.main()
